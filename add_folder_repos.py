# import os
# from github import Github
# import subprocess





# def update_remote_urls(root_directory, username):
#     # Iterate over each folder in the root directory
#     for folder in os.listdir(root_directory):
#         # Check if the path is a directory
#         repo_path = os.path.join(root_directory, folder)
#         if os.path.isdir(repo_path):
#             try:
#                 # Change directory to the repository
#                 os.chdir(repo_path)

#                 # Update remote URL to point to your GitHub repository
#                 subprocess.run(["git", "remote", "set-url", "origin", f"https://github.com/{username}/{folder}.git"])

#                 print(f"Remote URL updated successfully for '{folder}' repository.")
#             except Exception as e:
#                 print(f"Failed to update remote URL for '{folder}' repository: {e}")

# # Root directory containing subfolders (repositories)
# root_directory = os.path.dirname(__file__)

# # Your GitHub username

# # Update remote URLs for all subfolders
# update_remote_urls(root_directory, username)

# # GitHub credentials

# # Root directory containing folders to convert to repositories

# # Initialize GitHub instance
# g = Github(token)

# # Get the authenticated user (you)
# user = g.get_user()

# # Iterate over each folder in the root directory
# for folder in os.listdir(root_directory):
#     # Check if the path is a directory
#     if os.path.isdir(os.path.join(root_directory, folder)):
#         try:
#             # Create repository
#             repo = user.create_repo(folder)
#             print(f"Repository '{folder}' created successfully.")

#             # Change directory to the folder
#             os.chdir(os.path.join(root_directory, folder))

#             # Initialize Git repository locally
#             subprocess.run(["git", "init"])

#             # Add GitHub repository as remote origin
#             subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{username}/{folder}.git"])

#             # Push to GitHub
#             subprocess.run(["git", "push", "-u", "origin", "master"])

#             print(f"Repository '{folder}' pushed successfully.")

#         except Exception as e:
#             print(f"Failed to create or push repository '{folder}': {e}")