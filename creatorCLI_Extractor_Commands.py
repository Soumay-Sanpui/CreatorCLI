# creatorCLI_Extractor_Commands.py
from creatorCLI_IMPORTS import *

def create_directory(current_directory, directory_name):
    try:
        sp.run(f"mkdir {directory_name}", shell=True, check=True, cwd=current_directory)
    except Exception as e:
        print(f"❌ Error: {e}")

def run_node_commands(current_directory, directory_name):
    try:
        for node_command in node_commandList:
            sp.run(node_command, shell=True, check=True, text=True, cwd=os.path.join(current_directory, directory_name))
    except Exception as e:
        print(f"❌ Error: {e}")

def run_backend_commands(current_directory, directory_name):
    try:
        for backend_command in backend_commandList:
            sp.run(backend_command, shell=True, check=True, text=True, cwd=os.path.join(current_directory, directory_name))
    except Exception as e:
        print(f"❌ Error: {e}")

def update_configuration_files(directory_name, current_directory, script_directory):
    try:
        configUpdater(directory_name, current_directory, script_directory)
        update_file(directory_name, current_directory, script_directory, "env_file_content", ".env")
        update_file(directory_name, current_directory, script_directory, "apiResponse_file_content", "src/utils/ApiResponse.js")
        update_file(directory_name, current_directory, script_directory, "index_file_content", "index.js")
        update_file(directory_name, current_directory, script_directory, "app_file_content", "app.js")
    except Exception as e:
        print(f"❌ Error: {e}")

def run_git_commands(current_directory, directory_name):
    try:
        for git_command in git_commandList:
            sp.run(git_command, shell=True, check=True, text=True, cwd=os.path.join(current_directory, directory_name))
    except Exception as e:
        print(f"❌ Error: {e}")

def single_dir_gen(opt):
    global current_directory
    global directory_name
    global dirOptions

    try:
        if opt in dirOptions:
            dir_name = dirOptions[opt]
            sp.run(f"mkdir src\\{dir_name}", shell=True, check=True,
                   cwd=os.path.join(current_directory, directory_name))
            print(f"✨ Directory '{dir_name}' created ✨")
        else:
            print(f"❌ Error: Unknown option '{opt}' 🥶")
    except Exception as e:
        print(f"❌ Error: {e}")

def run_model_commands(current_directory, directory_name, script_directory,model_commands):
    try:
        for user_model_command in model_commands:
            sp.run(user_model_command, shell=True, check=True, text=True,
                   cwd=os.path.join(current_directory, directory_name))

        print("Generated USER Model ✨")
    except Exception as e:
        print(f"❌ Error: {e}")

