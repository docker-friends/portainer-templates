import os
import json

def update_templates_array(input_folder, existing_file):

    try:
        if os.path.exists(existing_file):
            with open(existing_file, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
                if not isinstance(existing_data, dict):
                    print(f"Warning: {existing_file} does not contain a JSON object. Starting fresh.")
                    existing_data = {}
                existing_data["templates"] = []
        else:
            existing_data = {"templates": []}
    except Exception as e:
        print(f"Error reading {existing_file}: {e}")
        existing_data = {"templates": []}

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(input_folder, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        existing_data["templates"].extend(data)
                    else:
                        existing_data["templates"].append(data)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    try:
        with open(existing_file, 'w', encoding='utf-8') as outfile:
            json.dump(existing_data, outfile, indent=4)
        print(f"Successfully updated the templates array in {existing_file}")
    except Exception as e:
        print(f"Error writing to {existing_file}: {e}")

def sort_json_keys(file_path):
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, sort_keys=True)
        
        print(f"Successfully sorted JSON keys in {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    input_folder = "../sources"
    existing_file = "../app-templates.json"

    update_templates_array(input_folder, existing_file)
    sort_json_keys(existing_file)