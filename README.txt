# Git instructions

To check the changes do
git status

To add the files do
git add <file_name>

If you want to add all the files, do
git add . 

Then you need to commit using
git commit -m "<commit_message>"

Then push the changes
git push

If there is a conflict while pushing,
it is probably because you have not
pulled the lastest changes on the repo.

Try to do
git pull

You might need to resolve merge conflicts.

For going back to an initial version of your repo:
1) Delete the repo and do git pull
or,
2) git reset --hard HEAD