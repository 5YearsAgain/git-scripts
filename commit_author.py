import subprocess

def change_author(old_author_name, new_author_name, new_author_email):
    # Run git filter-branch to rewrite the author information
    subprocess.run(['git', 'filter-branch', '-f', '--env-filter',
                    f'if [ "$GIT_AUTHOR_NAME" = "{old_author_name}" ]; then\n'
                    f'    export GIT_AUTHOR_NAME="{new_author_name}"\n'
                    f'    export GIT_AUTHOR_EMAIL="{new_author_email}"\n'
                    'fi'], check=True)

    # Run git commit --amend to apply the changes
    subprocess.run(['git', 'commit', '--amend', '--no-edit', '--reset-author'], check=True)

if __name__ == "__main__":
    old_author_name = "Neeraj giri"
    new_author_name = "skystarxtogether"
    new_author_email = "skystarxtogether@gmail.com"

    change_author(old_author_name, new_author_name, new_author_email)