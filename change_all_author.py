import git
import os

def git_rebase_exec(directory, correct_name, correct_email):
    # Change working directory to the specified directory
    os.chdir(directory)

    # Open the Git repository
    repo = git.Repo()

    # Perform the rebase operation with exec command
    try:
        repo.git.rebase('-r', '--root', '--exec', f'git commit --amend --no-edit --author="{correct_name} <{correct_email}>"', '--keep-empty')
    except git.exc.GitCommandError as e:
        print(f"Error occurred during rebase in repository: {directory}")
        print(e)

def traverse_and_rebase(directory, correct_name, correct_email):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            repo_path = os.path.join(root, dir)
            if os.path.isdir(os.path.join(repo_path, '.git')):
                print(f"Performing rebase operation in repository: {repo_path}")
                git_rebase_exec(repo_path, correct_name, correct_email)

if __name__ == "__main__":
    # Use the current directory as the parent directory
    parent_directory = os.getcwd()

    # Replace these values with the correct name and correct email
    correct_name = 'web-senior-dev'
    correct_email = '164904348+web-senior-dev@users.noreply.github.com'

    traverse_and_rebase(parent_directory, correct_name, correct_email)