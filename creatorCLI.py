import creatorCLI_IMPORTS

def saga_commands(commands):
    global current_directory
    try:
        sp.run(commands, shell=True, check=True, text=True, cwd=current_directory)
    except Exception as e:
        print(f"❌ Error: {e}")


def saga():
    global script_directory
    try:
        # Define the commands to be run
        commands = f"py {__file__} .b backend -g"
        # Run the commands
        saga_commands(commands)
    except Exception as e:
        print(f"❌ Error: {e}")


# Call the saga function when the script is executed with "SAGA" argument
def copyUtility(src, des):
    global directory_name
    global script_directory

    source_file_path = os.path.join(script_directory, src)
    destination_file_path = os.path.join(current_directory, directory_name, des)

    try:
        # Ensure the source file exists
        if not os.path.exists(source_file_path):
            print(f"❌ Error: Source file '{src}' not found.")
            return

        # Ensure the destination directory exists
        destination_dir = os.path.dirname(destination_file_path)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Copy the content from source to destination
        with open(source_file_path, "r") as sourceFile:
            src_content = sourceFile.read()

        with open(destination_file_path, "a") as destFile:
            destFile.write(src_content)

        print(f"✨ {des} Updated ✨")
    except Exception as e:
        print(f"❌ Error: {e}")

def configUpdater():
    global directory_name
    global current_directory

    package_json_path = os.path.join(current_directory, directory_name, 'package.json')
    try:
        with open(package_json_path, 'r+') as package_file:
            package_data = json.load(package_file)
            package_data['scripts'] = {'dev': 'nodemon index.js'}
            package_data['type'] = 'module'  # Add the 'type' field
            package_file.seek(0)
            json.dump(package_data, package_file, indent=4)
            package_file.truncate()

        print("✨ Package.json updated successfully ✨")
    except Exception as e:
        print(f"❌ Error: {e}")


def gitHandler():
    copyUtility("ignoreContent_doc.txt", ".gitignore")


def singleDirGen(opt):
    global current_directory
    global directory_name
    global dirOptions

    try:
        # Check if the specified option exists in dirOptions
        if opt in dirOptions:
            dir_name = dirOptions[opt]
            # Create the directory
            create_directory(os.path.join(current_directory, directory_name), f"src\\{dir_name}")
            print(f"✨ Directory '{dir_name}' created ✨")
        else:
            print(f"❌ Error: Unknown option '{opt}' 🥶")
    except Exception as e:
        print(f"❌ Error: {e}")


def extractor():
    global directory_name
    global current_directory

    current_directory = os.getcwd()  # Get the current working directory
    total_args = len(sys.argv)
    i = 1
    no_install = False  # Flag to indicate whether installation should be skipped
    while i < total_args:
        if sys.argv[i] == ".b" and i + 1 < total_args:
            directory_name = sys.argv[i + 1]
            try:
                # Check if the no-i flag is provided
                if "no-i" in sys.argv[i + 2:]:
                    no_install = True
                    # Skip to the next argument
                    i += 1

                # Create the directory relative to the current working directory
                create_directory(current_directory, directory_name)

                # Run node commands if installation is not skipped
                if not no_install:
                    run_node_commands(current_directory, directory_name)

                # Run backend commands
                run_backend_commands(current_directory, directory_name)

                # Update the config after running commands if no_install is false
                if not no_install:
                    print("Updating configuration files...")
                    configUpdater()
                    update_file(directory_name, current_directory, script_directory, "env_file_content",
                                ".env")  # Update .env file
                    print("Updated .env file")
                    update_file(directory_name, current_directory, script_directory, "apiResponse_file_content",
                                "src/utils/ApiResponse.js")  # Update ApiResponse.js
                    print("Updated ApiResponse.js")
                    update_file(directory_name, current_directory, script_directory, "index_file_content",
                                "index.js")  # Update index.js
                    print("Updated index.js")
                    update_file(directory_name, current_directory, script_directory, "app_file_content",
                                "app.js")  # Update app.js
                    print("Updated app.js")

                i += 2  # Skip both ".b" and directory name arguments
            except Exception as e:
                print(f"❌ Error: {e}")
                break

        elif sys.argv[i] == "-g":
            try:
                run_git_commands(current_directory, directory_name)
                gitHandler()
                i += 1
            except Exception as e:
                print("❌ Error in git command.")

        elif sys.argv[i].startswith("-d"):
            # Extract the option from the argument
            opt = sys.argv[i][2:]
            single_dir_gen(current_directory, directory_name, opt)
            i += 1
        elif sys.argv[i].startswith("SAGA"):
            # Call saga function
            saga()
            break  # Exit loop after executing SAGA command
        elif sys.argv[i] == "--getuser":
            run_user_model_commands(current_directory, directory_name, script_directory)
            update_file(directory_name, current_directory, script_directory, "user_model_content", "src/models/user.model.js")
            print("Updated user.model.js")
            break
        else:
            i += 1
            break

extractor()