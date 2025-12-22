import json

def parse_json_file(filename):
    try:
        with open(filename,'r') as f:
            return json.load(f)
    except:
        return None

if __name__ == "__main__":
    numbers = [1,2,3,5]
    print(parse_json_file("data.json"))