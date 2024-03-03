from creatorCLI_IMPORTS import *

# NOTE:
# print(f"{'\033[91m'}{'\033[1m'} ℹ NPM COMMANDS ARE DISABLED FOR TESTING........ ℹ \n{'\033[1m'}{'\033[91m'}" *10)

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
        commands = f"py {__file__} .b backend --getuser --getpost --getproductcatalog --getmessaging --getcontentmanagement --getsocialnetwork -g"
        # Run the commands
        saga_commands(commands)
    except Exception as e:
        print(f"❌ Error: {e}")

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
    """
    Generate a single directory within the project structure.

    Args:
        opt (str): Option specifying the directory to create.

    Returns:
        None

    Raises:
        Exception: If an error occurs during directory creation.

    Notes:
        The function retrieves the current directory and project name from global variables.
        It then checks if the specified option exists in the directory options dictionary.
        If the option is valid, it creates the corresponding directory within the 'src' directory.
        Otherwise, it raises an exception indicating an unknown option.

    Example:
        To create a 'models' directory, use:
        >>> singleDirGen('--mdl')

    """
    global current_directory
    global directory_name
    global dirOptions

    try:
        # Check if the specified option exists in dirOptions
        if opt in dirOptions:
            dir_name = dirOptions[opt]
            # Create the directory
            create_directory(os.path.join(current_directory, directory_name), f"src\\{dir_name}")
            print(f"✨ Directory '{dir_name}' created successfully! ✨")
        else:
            print(f"❌ Error: Unknown option '{opt}' 🥶")
    except Exception as e:
        # Handle any errors during directory creation
        print(f"❌ Error: {e}")

def modelGenerator(modelCommandList, modelContent, modelPath, modelFileName="model.js"):
    """
    Generate a model and update corresponding files.

    Args:
        modelCommandList (list): List of commands to generate the model.
        modelContent (str): Content to update the model file.
        modelPath (str): Path to the model file.
        modelFileName (str, optional): Name of the model file. Defaults to "model.js".

    Returns:
        None

    Raises:
        Exception: If any error occurs during model generation or file update.
    """
    try:
        # Execute model generation commands
        run_model_commands(current_directory, directory_name, script_directory, modelCommandList)
        
        # Update model file with provided content
        update_file(directory_name, current_directory, script_directory, modelContent, modelPath)
        
        # Print success message
        print(f"Updated {modelFileName} ✨")
    except Exception as e:
        # Handle any errors
        print(f"❌ Error: {e}")

def noInstallConfigUpdate():
    print("Updating configuration files...")
    configUpdater()
    update_file(directory_name, current_directory, script_directory, "env_file_content",".env")  # Update .env file
    print("Updated .env file")
    update_file(directory_name, current_directory, script_directory, "apiResponse_file_content","src/utils/ApiResponse.js")  # Update ApiResponse.js
    print("Updated ApiResponse.js")
    update_file(directory_name, current_directory, script_directory, "index_file_content","index.js")  # Update index.js
    print("Updated index.js")
    update_file(directory_name, current_directory, script_directory, "app_file_content","app.js")  # Update app.js
    print("Updated app.js")
    update_file(directory_name, current_directory, script_directory, "db_file_content","src/db/index.js")  # Update app.js
    print("Generated Db connector !")

def handle_model_command(sys_arg):
    """
    Handle model generation commands.

    Args:
        sys_arg (str): The command-line argument indicating the type of model to generate.

    Returns:
        None
    """
    model_commands = {
        "--getuser": (UsermodelGeneration_commandList, "user_model_content", "src/models/user.model.js", "user.model.js"),
        "--getpost": (PostmodelGeneration_commandList, "post_model_content", "src/models/post.model.js", "post.model.js"),
        "--getproductcatalog": (ProductCatalogmodelGeneration_commandList, "productCatalog_model_content", "src/models/productCatalog.model.js", "productCatalog.model.js"),
        "--getmessaging": (MessagingmodelGeneration_commandList, "messaging_model_content", "src/models/messaging.model.js", "messaging.model.js"),
        "--geteventscheduling": (EventSchedulingmodelGeneration_commandList, "eventScheduling_model_content", "src/models/eventScheduling.model.js", "event_scheduling.model.js"),
        "--getlocationbased": (LocationBasedmodelGeneration_commandList, "locationBased_model_content", "src/models/locationBased.model.js", "location_based.model.js"),
        "--getcontentmanagement": (ContentManagementmodelGeneration_commandList, "contentManagement_model_content", "src/models/contentManagement.model.js", "content_management.model.js"),
        "--getfinancialtransaction": (FinancialTransactionmodelGeneration_commandList, "financialTransaction_model_content", "src/models/financialTransaction.model.js", "financial_transaction.model.js"),
        "--getanalytics": (AnalyticsmodelGeneration_commandList, "analytics_model_content", "src/models/analytics.model.js", "analytics.model.js"),
        "--getsocialnetwork": (SocialNetworkmodelGeneration_commandList, "socialNetwork_model_content", "src/models/socialNetwork.model.js", "social_network.model.js")
    }

    if sys_arg in model_commands:
        modelGenerator(*model_commands[sys_arg])
    else:
        print(f"❌ Error: Unknown model command '{sys_arg}'")

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
                if "no-i" in sys.argv[i + 2:]:
                    no_install = True
                    i += 1
                create_directory(current_directory, directory_name)
                if not no_install:
                    commands_executor(current_directory, directory_name,node_commandList)
                commands_executor(current_directory, directory_name,backend_commandList)
                if not no_install:
                    noInstallConfigUpdate()
                i += 2
            except Exception as e:
                print(f"❌ Error: {e}")
                break

        elif sys.argv[i] == "-g":
            try:
                commands_executor(current_directory, directory_name,git_commandList)
                gitHandler()
                i += 1
            except Exception as e:
                print("❌ Error in git command.")

        elif sys.argv[i].startswith("-d"):
            opt = sys.argv[i][2:]
            single_dir_gen(current_directory, directory_name, opt)
            i += 1
        elif sys.argv[i].startswith("SAGA"):
            saga()
            break

        elif sys.argv[i].startswith("--get"):
           handle_model_command(sys.argv[i])
           i += 1
        elif sys.argv[i].startswith("-h" or "--help" or "-?" or "--info"):
            showHelpText()
            return
        elif sys.argv[i].startswith("base"):
            commands_executor(current_directory,directory_name,base_installation_commandList)
            configUpdater()
            break
        else:
            showHelpText()
            break
extractor()
