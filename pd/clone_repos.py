import pathlib
import os
import shutil
import argparse
import stat
from git import Repo
import pd.dict_repo_list


def clone_repositories(output_directory: pathlib.Path):
    """
    Clone repositories from pd.dict_repo_list to given location.

    Args:
        output_directory: Location to clone repositories to.
    """
    projects_list = pd.dict_repo_list.projects.keys()
    number_of_projects = len(projects_list)

    print(f"Cloning {number_of_projects} projects to {output_directory}")
    for index, project in enumerate(projects_list, start=1):
        repositories_info = pd.dict_repo_list.projects[project]
        remote_address = repositories_info["remote"]
        print(f"({index}/{number_of_projects}) project: {project} - Remote: {remote_address}")
        project_output_directory = output_directory.joinpath(project)

        if project_output_directory.exists():
            print(f"Warning: {project_output_directory} already exists. Removing the directory and re-cloning...")
            try:
                shutil.rmtree(project_output_directory, onerror=remove_readonly)
            except OSError as e:
                print(f"Error project: {project_output_directory} : {e.strerror}")
        os.makedirs(project_output_directory)
        Repo.clone_from(remote_address, project_output_directory)


def remove_readonly(func, path, _):
    """
    Removing a directory containing files caused an issue when the read-only bit has been set on some of the files.
    Clears the read-only bit, so the removal can be retried.
    Args:
        func: The function that triggered the exception.
        path: The path to the file that triggered the exception.
        _: Exception information, not used here but `remove_readonly` needs to accept 3 parameters.
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def main():
    parser = argparse.ArgumentParser(description='Repository cloning utility.')
    parser.add_argument('output_directory', type=pathlib.Path, help='Path to save the repositories to.')
    args = parser.parse_args()

    output_directory = args.output_directory.absolute()

    if not output_directory.exists():
        try:
            os.makedirs(output_directory)
        except OSError as e:
            print(f"Could not create directory at location: {output_directory}; Error: {e}")

    clone_repositories(output_directory)


if __name__ == "__main__":
    main()
