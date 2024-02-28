# creatorCLI_IMPORTS.py
import os
import sys
import json
import subprocess as sp
from creatorCLI_Updators import update_file
from creatorCLI_OptionsList import backend_commandList, dirOptions, git_commandList, node_commandList, UsermodelGeneration_commandList
from creatorCLI_Extractor_Commands import (
    create_directory,
    run_node_commands,
    run_backend_commands,
    update_configuration_files,
    run_git_commands,
    single_dir_gen,
    run_user_model_commands
)

# Global variables
script_directory = os.path.dirname(os.path.abspath(__file__))
directory_name = ""
current_directory = ""
