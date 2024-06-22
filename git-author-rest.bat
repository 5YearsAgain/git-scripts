rem git config --global user.name "New Author Name"
rem git config --global user.email "<email@address.example>"

git rebase -r --root --exec "git commit --amend --no-edit --reset-author"