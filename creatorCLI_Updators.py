# creatorCLI_Updators.py
import creatorCLI_IMPORTS

def update_file(directory_name, current_directory, script_directory, source_key, destination_file):
  """Updates the content of a file based on a provided source key.

  Args:
      directory_name: Name of the directory where the file resides.
      current_directory: Absolute path of the current working directory.
      script_directory: Absolute path of the script's directory.
      source_key: Key used to retrieve the content from a JSON file.
      destination_file: Name of the file to be updated.
  """

  print(f"Updating file: {destination_file}")

  # Load the content from replacerContent.json
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
    # Ensure the destination file is writable before updating
    if not os.access(file_path, os.W_OK):
      os.chmod(file_path, os.stat(file_path).st_mode | 0o666)  # Make the file writable

    # Write the content to the destination file
    with open(file_path, 'w') as file:
      file.write(file_content)
    print(f"{destination_file} updated successfully in {file_path} ✨")

  except Exception as e:
    print(f"Error updating {destination_file}: {e}")

  # Update user.model.js in the src/models directory
  if destination_file == "user.model.js":
    src_model_path = os.path.join(current_directory, directory_name, 'src', 'models', 'user.model.js')

    try:
      # Ensure src/models/user.model.js is writable before updating
      if not os.access(src_model_path, os.W_OK):
        os.chmod(src_model_path, os.stat(src_model_path).st_mode | 0o666)

      with open(src_model_path, 'w') as src_model_file:
        src_model_file.write(file_content)
      print(f"{destination_file} updated successfully in src/models directory ✨")
    except Exception as e:
      print(f"Error updating {destination_file} in src/models directory: {e}")

# This line is only needed if you want to call the function directly for testing
# update_file("my_directory", os.getcwd(), "/path/to/script", "my_key", "my_file.txt")

