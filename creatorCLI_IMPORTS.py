# creatorCLI_IMPORTS.py
import os
import sys
import json
import subprocess as sp
from creatorCLI_Updators import update_file
from creatorCLI_OptionsList import (
    backend_commandList, 
    dirOptions, 
    git_commandList, 
    node_commandList, 
    base_installation_commandList,
    UsermodelGeneration_commandList, 
    PostmodelGeneration_commandList,
    ProductCatalogmodelGeneration_commandList,
    MessagingmodelGeneration_commandList,
    EventSchedulingmodelGeneration_commandList,
    LocationBasedmodelGeneration_commandList,
    ContentManagementmodelGeneration_commandList,
    FinancialTransactionmodelGeneration_commandList,
    AnalyticsmodelGeneration_commandList,
    SocialNetworkmodelGeneration_commandList,
)

from creatorCLI_Extractor_Commands import (
    create_directory,
    commands_executor,
    update_configuration_files,
    single_dir_gen,
    run_model_commands,
    showHelpText,
)

# Global variables
script_directory = os.path.dirname(os.path.abspath(__file__))
directory_name = ""
current_directory = ""
