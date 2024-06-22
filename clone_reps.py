import requests
import subprocess

def get_repositories(username, access_token=None):
    headers = {'Authorization': f'token {access_token}'} if access_token else {}
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repositories = [repo["clone_url"] for repo in response.json()]
        return repositories
    else:
        print(f"Failed to fetch repositories: {response.status_code}")
        return []

def clone_repositories(repositories):
    for repo_url in repositories:
        subprocess.run(["git", "clone", repo_url])

if __name__ == "__main__":
    username = "supersmile0426"
   # access_token = "your_access_token"  # Optional if cloning private repositories
    repositories = get_repositories(username)
    if repositories:
        clone_repositories(repositories)
        print("Cloning complete.")
    else:
        print("No repositories found for the specified user.")