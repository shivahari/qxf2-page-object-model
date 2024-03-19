from optparse import OptionParser
from loguru import logger
import os
import pathlib
import shutil

DIRS = ["conf", "endpoints", "log", "utils"]

def create_repo() -> None:
    "Create the Test Framework repo locally"
    try:
        for dir in DIRS:
            dir = "tests" + os.path.sep + dir
            path = pathlib.Path(dir)
            path.mkdir(parents=True, exist_ok=True)
            logger.success(f"Successfully create dir - {dir}")

        # Copy files/folders
        file_dir = os.path.dirname(__file__)
        repo_dir = "tests"
        files_folders = ["conf", "conftest.py", "requirements.txt", "utils", "Base_API.py"]
        for file_folder in files_folders:
            source_location = file_dir + os.path.sep + "templates" + os.path.sep + file_folder
            if file_folder == "Base_API.py":
                dest_location = repo_dir + os.path.sep + "endpoints" + os.path.sep + file_folder
            else:
                dest_location = repo_dir + os.path.sep + file_folder
            copy_file_folder(source_location, dest_location)

    except Exception as err:
        logger.error(f"Unable to create dirs due to {err}")

def copy_file_folder(source_location: str, dest_location: str) -> None:
    "Copy file from package location to repo"
    try:
        if os.path.isdir(source_location):
            logger.info(f"Copying folder - {source_location}")
            shutil.copytree(source_location, dest_location, dirs_exist_ok=True)
        else:
            logger.info(f"Copying file - {source_location}")
            shutil.copy(source_location, dest_location)
        logger.success(f"Successfully copied file {source_location} to {dest_location}")
    except Exception as err:
        logger.error(f"Unable to copy file from {source_location} to {dest_location}, due to {err}")

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--api",
                      action="store_true",
                      dest="if_api_repo",
                      help="Pass --api option if you want to create an API repo")
    (options, args) = parser.parse_args()
    if options.if_api_repo:
        logger.info("Creating an API repo")
        create_repo()
    else:
        parser.print_help()
