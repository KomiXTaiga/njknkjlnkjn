import sys
import clipboard
import json
def save(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)
        
def load(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.dump(f)
            return data
    except:
        return {}
saved_data = "clipboard.json"
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load(saved_data)
    if command == "save":
        key = input("Enter a key \n")
        data[key] = clipboard.paste()
        save(saved_data, data)
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("Unowkn command")
else:
    print("please pass a command")


