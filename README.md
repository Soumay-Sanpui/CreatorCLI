🚀 Welcome to the CreatorCLI Documentation! 🚀
===========================================

CreatorCLI is a versatile command-line interface (CLI) tool designed to simplify project setup and streamline development workflows. Whether you're starting a new project or maintaining an existing one, CreatorCLI automates repetitive tasks, saving you time and effort.

🛠️ Setup 🛠️
---------

To get started with CreatorCLI, follow these steps:

1. **Installation**: Clone the CreatorCLI repository to your local machine by executing the following command in your terminal:

    ```
    git clone https://github.com/your-username/CreatorCLI.git
    ```

2. **Setup**: Navigate to the directory containing CreatorCLI files in your terminal:

    ```
    cd /path/to/CreatorCLI
    ```

3. **Execution**: Run the `creatorCLI.py` script along with the desired command-line arguments to perform various tasks. The syntax for running the script is:

    ```
    python creatorCLI.py [project_directory] [options]
    ```

    Here, `project_directory` specifies the name of the project directory, and `options` include flags and parameters for specific actions.

> __NOTE: in normal installation if you try to create projcet using creator cli you have to specify the full path of creator cli installation folder.__

## 🌏 Steps for Global install 🛠️

1. **Installation**: Clone the CreatorCLI repository to your local machine by executing the following command in your terminal:

    ```
    git clone https://github.com/your-username/CreatorCLI.git
    ```

2. **Setup**: Navigate to the directory containing CreatorCLI files in your terminal:

    ```
    cd /path/to/CreatorCLI
    ```
3. **Alias configuration (WINDOWS)**: 
    1. Go to Edit System Env.
    2. Go to path.
    3. click on Edit
    4. In creator cli installation folder look for the file
    ``` cc.bat ```.
    5. copy the file path and paste it in the new field of system env. variables.

4. **Creating project**: 
    ```cc .b project_name [options]```

> __NOTE: After gloabal install there is no need to write 'python CreatorCLI' every time you create a project.__

🚩 Flags 🚩
--------

CreatorCLI supports the following flags:

* `.b`: Indicates backend setup.
* `no-i`: Skips dependency installation.
* `-g`: Performs Git-related operations.
* `-d`: Generate custom directory.
* `--get`: Generate custom model with full code 👩‍💻.
* `-h / --help / -? / --info`: get help text on console.
* `base`: get a base setup of express mongodb with all the boiler plate.
* `SAGA`: will generate everything you need.


🧠 BASICS
------------
1. __'.b'__ : This is the most important and starting flag in the CreatorCLI tool, it marks that you want to create a backend project in the current directory.

1. __'no-i'__ : If you just want the code without the installion process use this flag, this flag will skip all the dependency installation but creatorCLI will still generate all the code and folders, any manual dependency installtion will be automatically handled by CreatorCLI and other configuration will be updated according to that.

1. __'base'__ : If you just need basic configuration like a simple express application with mongodb support this flag will help you in that.

1. __'SAGA'__ : This is a heavy command to run as it will not only generate code but will also generate directories and will do the configuration stuff with all the depency being installed at the same time, once completed you will be having everything you need on your plate to build a full fledge backend of any kind of application with git already initialized for you.
```
    WHAT THE SAGA COMMAND WILL GENERATE ?
    1. Directories:
        1.1 ROUTES
        1.2 PUBLIC -> with .gitkeep file
        1.3 MIDDLEWARES
        1.4 UTILS
        1.5 CONTROLLERS
    2. MODELS:
        2.1 USERS
    3. FILES:
        3.1 .env
        3.2 .gitignore (pre written)
        3.3 server.js (entry point)
        3.4 app.js (express file)
        3.5 router/index.js (routing file)
        3.6 user.model.js
        3.7 post.model.js
        3.8 ApiError.js
        3.9 utils.js
        3.10 constants.js
    4. DEPENDENCIES:
        4.1 dotenv 
        4.2 express 
        4.3 mongoose 
        4.4 cors 
        4.5 bcrypt 
        4.6 jsonwebtoken 
        4.7 multer 
        4.8 cloudinary
        4.9 nodemon (as development dependency)
```
🌟 Features 🌟
-----------

### Directory Generation 📁

CreatorCLI simplifies directory creation with the `singleDirGen()` function, allowing you to create single directories within the project structure based on specified options:

* `--mdl`: Creates a 'models' directory.
* `--db`: Creates a 'db' directory.
* `--rts`: Creates a 'routes' directory.
* `--mdw`: Creates a 'middlewares' directory.
* `--api`: Creates an 'apis' directory.
* `--pg`: Creates a 'pages' directory.
* `--tst`: Creates a 'test' directory.
* `--pub`: Creates a 'public' directory.
* `--tmp`: Creates a 'temp' directory.
* `--utl`: Creates a 'utils' directory.
* `--vw`: Creates a 'views' directory.
* `--stc`: Creates a 'static' directory.
* `--ctr`: Creates a 'controllers' directory.

To use single directory generation, execute the CreatorCLI script with the desired option. 

For example:
```python creatorCLI.py [project_directory] --mdl```

-----------------------------------------------------
### Model Generation 🗃️

CreatorCLI facilitates model generation for various components of your application:

* **User Model**: Generates a user model with fields such as full name, username, email, password, avatar, and more.
* **Post Model**: Creates a post model with fields like title, content, photos, comments, likes, tags, location, and more.
* **Product Catalog Model**: Generates a product catalog model with attributes including name, description, price, category, quantity, images, and ratings.
* **Messaging Model**: Creates a messaging model for handling messages between users, including sender, receiver, message content, and attachments.
* **Event Scheduling Model**: Generates a model for event scheduling, including fields like title, description, date, location, organizer, and participants.
* **Location-Based Model**: Creates a model for storing location data, including latitude, longitude, address, city, and country.
* **Content Management Model**: Generates a model for managing content, including fields for title, content, author, tags, likes, comments, and timestamps.
* **Financial Transaction Model**: Creates a model for financial transactions, including amount, description, sender, receiver, and status.
* **Analytics Model**: Generates a model for tracking analytics data, including event type, user, device, browser, IP address, location, platform, and timestamp.
* **Social Network Model**: Creates a model for managing social network connections between users, including user1, user2, status, actionBy, message, and lastInteractionAt.

To generate a specific model, use the corresponding command-line option. For example:

```python creatorCLI.py .b folder_name --getuser```

 This above command will generate a user model in your project directory.
## List of Model Commands:
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getuser<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getpost<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getproductcatalog<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getmessaging<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --geteventscheduling<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getlocationbased<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getcontentmanagement<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getfinancialtransaction<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getanalytics<br>
1. > python [full_path_of_installation_folder]/creatorCLI.py .b project_name --getsocialnetwork<br>

## List of Model Commands for GLOBAL INSTALL
1. > cc .b project_name --getuser<br>
1. > cc .b project_name --getpost<br>
1. > cc .b project_name --getproductcatalog<br>
1. > cc .b project_name --getmessaging<br>
1. > cc .b project_name --geteventscheduling<br>
1. > cc .b project_name --getlocationbased<br>
1. > cc .b project_name --getcontentmanagement<br>
1. > cc .b project_name --getfinancialtransaction<br>
1. > cc .b project_name --getanalytics<br>
1. > cc .b project_name --getsocialnetwork<br>

----------------------------------------------------

### SAGA [super admin generate all] Command ⚔️

CreatorCLI includes support for generating all the major folders and boiler-plate code in just 4 words.

* **Super Admin Generate All**: Generates SAGA commands for super admin functionalities, including user management, permissions, and more.

To generate super admin SAGA commands, use the following command-line option:

```
    python [full_path_to_creatorCLI_installation]/creatorCLI.py .b folder_name SAGA
```

### For Globally installed CLI.
```
    cc .b project_name SAGA
```

This command will generate all the required things from dependencies to models to get you started with the project without any extra overhead and configuration.

-------------
🎉 Conclusion 🎉

With CreatorCLI, project setup and management are streamlined, allowing you to focus on development tasks more efficiently. Explore the various features and functionalities to enhance your development workflow and accelerate project delivery. Happy coding! 🛠️
