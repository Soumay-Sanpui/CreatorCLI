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

🚩 Flags 🚩
--------

CreatorCLI supports the following flags:

* `.b`: Indicates backend setup.
* `.f`: Indicates frontend setup.
* `--no-i`: Skips dependency installation.
* `-g`: Performs Git-related operations.

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

To use single directory generation, execute the CreatorCLI script with the desired option. For example:

```python creatorCLI.py [project_directory] --mdl```

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

This command will generate a user model in your project directory.

### SAGA [super admin generate all] Command ⚔️

CreatorCLI includes support for generating all the major folders and boiler-plate code in just 4 words.

* **Super Admin Generate All**: Generates SAGA commands for super admin functionalities, including user management, permissions, and more.

To generate super admin SAGA commands, use the following command-line option:

```python creatorCLI.py .b folder_name SAGA```

This command will generate SAGA commands for super admin functionalities in your backend project.

🎉 Conclusion 🎉
-------------

With CreatorCLI, project setup and management are streamlined, allowing you to focus on development tasks more efficiently. Explore the various features and functionalities to enhance your development workflow and accelerate project delivery. Happy coding! 🛠️
