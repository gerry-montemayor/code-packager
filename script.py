import os
import pyperclip as pc

# FILES TO IGNORE
ignore_files = ["main.py", "package.txt"]

# DIRECTORIES TO IGNORE
ignore_directories = []


# Get the current working directory
project_dir = os.getcwd()

# Print project folder structure
with open("package.txt", "w") as script:

    def get_file_structure(directory, count):
        entries = os.listdir(directory)

        # prune files to ignore
        temp_files = [
            entry for entry in entries if os.path.isfile(os.path.join(directory, entry))
        ]
        files = [file for file in temp_files if file not in ignore_files]

        # prune directories to ignore
        temp_directories = [
            entry for entry in entries if os.path.isdir(os.path.join(directory, entry))
        ]

        directories = [
            directory
            for directory in temp_directories
            if directory not in ignore_directories
        ]

        if len(files) > 0:
            for file in files:
                script.write("    " * count + "|-- " + file + "\n")

        for subdir in directories:
            script.write("    " * count + "+-- " + subdir + "\n")
            get_file_structure(os.path.join(directory, subdir), count + 1)

    # Prints out file structure
    script.write("Project Structure \n\n")
    get_file_structure(project_dir, 0)
    script.write("\n\n\n")

    # # List all directories in the project directory
    # directories = [
    #     name
    #     for name in os.listdir(project_dir)
    #     if os.path.isdir(os.path.join(project_dir, name))
    # ]

    def recurseFiles(directory, count):
        entries = os.listdir(directory)

        # Separate entries into files and directories
        temp_files = [
            entry for entry in entries if os.path.isfile(os.path.join(directory, entry))
        ]

        # prune files to ignore
        files = [file for file in temp_files if file not in ignore_files]

        temp_directories = [
            entry for entry in entries if os.path.isdir(os.path.join(directory, entry))
        ]
        directories = [
            directory
            for directory in temp_directories
            if directory not in ignore_directories
        ]
        if len(files) > 0:
            for f in files:
                file_path = os.path.join(directory, f)
                script.write(
                    "|----------------------------------------- "
                    + f
                    + " -----------------------------------------| \n"
                )

                with open(file_path, "r") as fi:
                    content = fi.read()
                    script.write(content + "\n\n")
        for subdir in directories:
            script.write("    " * count + "+--Directory:  " + subdir + "\n\n")
            recurseFiles(os.path.join(directory, subdir), count + 1)

    recurseFiles(project_dir, 0)
    print("\033[92m" + "Copied packaged project to package.txt!" + "\033[0m")


