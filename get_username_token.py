
import requests

def get_github_username(token):
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("login")  # This is the GitHub username
    else:
        print(
            f"Failed to fetch user info: {response.status_code} - {response.json().get('message')}"
        )
        return None


# Example usage
if __name__ == "__main__":
    github_token = "YOUR_GITHUB_TOKEN"  # Replace with your token
    username = get_github_username(github_token)
    if username:
        print(f"GitHub Username: {username}")
