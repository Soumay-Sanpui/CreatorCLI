# creatorCLI_Extractor_Commands.py
from creatorCLI_IMPORTS import *

def create_directory(current_directory, directory_name):
    """
    Creates a new directory within the current directory.

    Parameters:
        current_directory (str): The current working directory.
            This is the directory where the new directory will be created.
        directory_name (str): The name of the directory to create.
            This should be a valid directory name without any path components.

    Raises:
        subprocess.CalledProcessError: If the 'mkdir' command fails to create the directory.

    Notes:
        This function executes the 'mkdir' command using the subprocess module to create a new directory.
        It is assumed that the 'mkdir' command is available in the system environment.

    Example:
        To create a directory named 'project', use the following command:
            create_directory('/path/to/current_directory', 'project')
    """
    try:
        sp.run(f"mkdir {directory_name}", shell=True, check=True, cwd=current_directory)
    except Exception as e:
        print(f"❌ Error: {e}")

def commands_executor(current_directory, target_directory, command_list):
    """
    Executes a list of commands in the specified target directory.

    Args:
        current_directory (str): The current working directory.
        target_directory (str): The directory in which commands will be executed.
        command_list (list): A list of shell commands to execute.
    """
    try:
        for command in command_list:
            sp.run(command, shell=True, check=True, text=True, cwd=os.path.join(current_directory, target_directory))
    except Exception as e:
        print(f"❌ Error: {e}")

def update_configuration_files(directory_name, current_directory, script_directory):
    """
    Updates configuration files within the project directory.

    Parameters:
        directory_name (str): The name of the project directory.
        current_directory (str): The current working directory.
        script_directory (str): The directory containing the CreatorCLI script.

    Outputs:
        None

    Description:
        This function updates various configuration files within the project directory based on the provided content 
        from the CreatorCLI script.
    """
    try:
        configUpdater(directory_name, current_directory, script_directory)
        update_file(directory_name, current_directory, script_directory, "env_file_content", ".env")
        update_file(directory_name, current_directory, script_directory, "apiResponse_file_content", "src/utils/ApiResponse.js")
        update_file(directory_name, current_directory, script_directory, "index_file_content", "index.js")
        update_file(directory_name, current_directory, script_directory, "app_file_content", "app.js")
    except Exception as e:
        print(f"❌ Error: {e}")

def single_dir_gen(opt):
    """
    Generates a single directory within the project structure based on the specified option.

    Parameters:
        opt (str): The option specifying the type of directory to create.

    Outputs:
        None

    Description:
        This function creates a single directory within the project structure based on the provided option.
    """
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
    """
    Runs model generation commands for the specified directory.

    Parameters:
        current_directory (str): The current working directory.
        directory_name (str): The name of the project directory.
        script_directory (str): The directory containing the script files.
        model_commands (list): A list of model generation commands.

    Outputs:
        None

    Description:
        This function executes model generation commands for the specified directory,
        creating models based on the provided commands.

    Supported Models:
        - User Model: Generates a model for user data with fields like full name, username, email, password, avatar, etc.
        - Post Model: Creates a model for posts with fields including title, content, photos, comments, likes, tags, location, etc.
        - Product Catalog Model: Generates a model for product catalog with attributes such as name, description, price, category, quantity, images, ratings, etc.
        - Messaging Model: Creates a model for handling messages between users, including sender, receiver, message content, attachments, etc.
        - Event Scheduling Model: Generates a model for event scheduling with fields like title, description, date, location, organizer, participants, etc.
        - Location-Based Model: Creates a model for storing location data, including latitude, longitude, address, city, country, etc.
        - Content Management Model: Generates a model for managing content, including fields for title, content, author, tags, likes, comments, timestamps, etc.
        - Financial Transaction Model: Creates a model for financial transactions, including amount, description, sender, receiver, status, etc.
        - Analytics Model: Generates a model for tracking analytics data, including event type, user, device, browser, IP address, location, platform, timestamp, etc.
        - Social Network Model: Creates a model for managing social network connections between users, including user1, user2, status, actionBy, message, lastInteractionAt, etc.

    Example:
    run_model_commands(current_directory, directory_name, script_directory, model_commands)
    """
    try:
        for user_model_command in model_commands:
            sp.run(user_model_command, shell=True, check=True, text=True,
                   cwd=os.path.join(current_directory, directory_name))

        print("Generated USER Model ✨")
    except Exception as e:
        print(f"❌ Error: {e}")

def showHelpText():

    print(" $$$$$$\                                 $$\                          $$$$$$\  $$\       $$$$$$\ ")
    print("$$  __$$\                                $$ |                        $$  __$$\ $$ |      \_$$  _|")
    print("$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  $$ /  \__|$$ |        $$ |  ")
    print("$$ |      $$  __$$\ $$  __$$\  \____$$\\_$$  _|  $$  __$$\ $$  __$$\ $$ |      $$ |        $$ |  ")
    print("$$ |      $$ |  \__|$$$$$$$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|$$ |      $$ |        $$ |  ")
    print("$$ |  $$\ $$ |      $$   ____|$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      $$ |  $$\ $$ |        $$ |  ")
    print("\$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      \$$$$$$  |$$$$$$$$\ $$$$$$\ ")
    print(" \______/ \__|       \_______| \_______|  \____/  \______/ \__|       \______/ \________|\______|")

# CreatorCLI Help Message

# Link to Documentation (replace with actual URL)
DOCS_URL = "https://replace_with_actual_docs_url"
print(f"For detailed documentation, visit: {DOCS_URL}")

print("\nUsage: cc .b [project_name] [options]")
print("\nCommands:")
print("  * cc -h or -? or --help or --info       : Display this help message.")
print("  * .b project_name                       : Create a backend project in the specified directory.")
print("  * (Currently not supported) .f project_name: (Not yet implemented) Create a frontend project in the specified directory.")  # Indicate frontend functionality not yet available

print("\nOptions:")
print("  * -g                                    : Perform Git-related operations (e.g., initialize repository).")
print("  * --getuser                             : Generate a user model for your project.")
print("  * --getpost                              : Generate a post model for your project.")
print("  * --getproduct                          : Generate a product catalog model for your project.")
print("  * --getmessage                           : Generate a messaging model for your project.")
print("  * --getevent                            : Generate an event scheduling model for your project.")
print("  * --getlocation                          : Generate a location-based model for your project.")
print("  * --getcontent                           : Generate a content management model for your project.")
print("  * --gettransaction                       : Generate a financial transaction model for your project.")
print("  * --getanalytics                         : Generate an analytics model for your project.")
print("  * --getsocial                            : Generate a social network model for your project.")
print("  * -d<option>                             : Create a single directory within the project structure (options: mdl, db, rts, mdw, api, pg, tst, pub, tmp, utl, vw, stc, ctr).")
print("  * no-i                                   : Skip dependency installation during project creation.")
print("  * base                                   : Set up a basic Express.js application with MongoDB support.")
print("  * SAGA                                   : Generate a comprehensive backend project structure with dependencies, models, and configuration (includes Git initialization).")

    