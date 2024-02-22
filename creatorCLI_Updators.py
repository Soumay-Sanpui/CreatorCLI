# creatorCLI_Updators.py
import os
import json

def update_file(directory_name, current_directory, script_directory, source_key, destination_file):
    # Load the content from replacerContent.json
    print("Starting Update 🐣")
    replacer_file_path = os.path.join(script_directory, 'replacerContent.json')
    try:
        with open(replacer_file_path, 'r') as replacer_file:
            replacer_content = json.load(replacer_file)
            file_content = replacer_content.get(source_key, "")
    except Exception as e:
        print(f"Error loading content from replacerContent.json: {e}")
        return

    # Path to the destination file
    file_path = os.path.join(current_directory, directory_name, destination_file)
    try:
        # Write the content to the destination file
        with open(file_path, 'w') as file:
            file.write(file_content)
        print(f"{destination_file} updated successfully ✨")
    except Exception as e:
        print(f"Error updating {destination_file}: {e}")
