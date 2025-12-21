#!/usr/bin/env python3
"""Script simple para explorar los datos de MongoDB"""

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import sys

# Importar los modelos
sys.path.insert(0, 'rock-solid-python-with-type-hints-course/code/04-frameworks-built-on-typing/web_example')
from models.package import Package
from models.user import User
from models.release_analytics import ReleaseAnalytics


async def explore_data():
    # Conectar a MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    database = client["pypi"]
    
    # Inicializar Beanie
    await init_beanie(database=database, document_models=[Package, User, ReleaseAnalytics])
    
    print("=" * 60)
    print("EXPLORACIÓN DE DATOS DE PYPI")
    print("=" * 60)
    
    # Estadísticas generales
    package_count = await Package.count()
    user_count = await User.count()
    analytics_count = await ReleaseAnalytics.count()
    
    print(f"\n📦 Total de paquetes: {package_count}")
    print(f"👥 Total de usuarios: {user_count}")
    print(f"📊 Total de analytics: {analytics_count}")
    
    # Algunos paquetes recientes
    print("\n" + "=" * 60)
    print("PAQUETES MÁS RECIENTES (últimos 5)")
    print("=" * 60)
    recent_packages = await Package.find_all().sort(-Package.last_updated).limit(5).to_list()
    for pkg in recent_packages:
        print(f"\n📦 {pkg.id}")
        print(f"   Última actualización: {pkg.last_updated}")
        print(f"   Resumen: {pkg.summary[:80]}..." if pkg.summary and len(pkg.summary) > 80 else f"   Resumen: {pkg.summary}")
        print(f"   Releases: {len(pkg.releases)}")
    
    # Paquetes con más releases
    print("\n" + "=" * 60)
    print("PAQUETES CON MÁS RELEASES (top 5)")
    print("=" * 60)
    all_packages = await Package.find_all().to_list()
    packages_by_releases = sorted(all_packages, key=lambda x: len(x.releases), reverse=True)[:5]
    for pkg in packages_by_releases:
        print(f"\n📦 {pkg.id}: {len(pkg.releases)} releases")
        if pkg.releases:
            latest = max(pkg.releases, key=lambda r: r.created_date)
            print(f"   Última versión: {latest.major_ver}.{latest.minor_ver}.{latest.build_ver}")
    
    # Buscar un paquete específico (si se proporciona como argumento)
    if len(sys.argv) > 1:
        package_name = sys.argv[1]
        print("\n" + "=" * 60)
        print(f"BÚSQUEDA: {package_name}")
        print("=" * 60)
        package = await Package.get(package_name)
        if package:
            print(f"\n📦 {package.id}")
            print(f"   Creado: {package.created_date}")
            print(f"   Última actualización: {package.last_updated}")
            print(f"   Autor: {package.author_name} ({package.author_email})")
            print(f"   Homepage: {package.home_page}")
            print(f"   Releases: {len(package.releases)}")
            if package.releases:
                print("\n   Versiones:")
                for release in sorted(package.releases, key=lambda r: r.created_date, reverse=True)[:5]:
                    print(f"      {release.major_ver}.{release.minor_ver}.{release.build_ver} - {release.created_date}")
        else:
            print(f"❌ Paquete '{package_name}' no encontrado")
    
    client.close()


if __name__ == "__main__":
    asyncio.run(explore_data())

