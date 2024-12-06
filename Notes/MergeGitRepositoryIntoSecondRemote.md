# Merge Git repository into second remote  

Some times you need to move or merge git repositories... here is the general list of commands

```batch
git remote rename origin upstream
git pull upstream master
git remote add origin NEW_URL_HERE
git pull origin master --allow-unrelated-histories
…do merge voodoo…
git push upstream master
git push origin master
```

## Based on Links 

* https://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server
* https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase