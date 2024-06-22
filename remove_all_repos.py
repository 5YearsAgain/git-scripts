# from github import Github


# # GitHub credentials

# # Initialize GitHub instance
# g = Github(token)

# # Get the authenticated user (you)
# user = g.get_user()

# # List all repositories
# repos = user.get_repos()

# # Iterate over repositories and delete them
# for repo in repos:
#     try:
#         # Delete repository
#         repo.delete()
#         print(f"Repository '{repo.full_name}' deleted successfully.")
#     except Exception as e:
#         print(f"Failed to delete repository '{repo.full_name}': {e}")