import requests

def get_users_emails(location):
    base_url = "https://api.github.com/search/users"
    params = {
        "q": f"location:{location}",
        "per_page": 100  # Adjust as needed
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        users_data = response.json()
        for user in users_data.get("items", []):
            username = user.get("login")
            email = get_user_email(username)
            if email is not None:
                print(f"Username: {username}, Email: {email}")
            # else:
                # print(f"Username: {username}, Email: Not available")
    else:
        print("Failed to retrieve user data")

def get_user_email(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get("email")
    else:
        return None

# Example usage
location = "San Francisco"  # Example location
get_users_emails(location)