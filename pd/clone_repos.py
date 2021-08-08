import pd.dict_repo_list
import sys
import os
from git import Repo


def main(argv):
    if len(argv) != 1:
        print_help()
        exit()
    output_directory = argv[0]

    if not os.path.exists(output_directory):
        print_help()
        exit()

    output_directory_abspath = os.path.abspath(output_directory)
    projects_list = list(pd.dict_repo_list.projects.keys())
    number_of_projects = str(len(projects_list))
    print("Cloning "+number_of_projects+" projects to "+output_directory_abspath)

    counter = 1
    for project in projects_list:
        repositories_info = pd.dict_repo_list.projects[project]
        remote_address = repositories_info["remote"]
        print("("+str(counter)+"/"+number_of_projects+") project: "+project+" - Remote: "+remote_address)
        project_output_directory = os.path.join(output_directory_abspath, project)

        if os.path.exists(project_output_directory):
            print("Warning: "+project_output_directory+" already exists. Removing the directory ...")
            os.rmdir(project_output_directory)
        
        os.makedirs(project_output_directory)

        Repo.clone_from(remote_address, project_output_directory)

        counter += 1
    

def print_help():
    """
    Print help text for wrong user input.
    """
    print("Expected: one input argument indicating a directory for saving the cloned repositories.")
    print("This directory should already exist.")


if __name__ == "__main__":
    main(sys.argv[1:])
