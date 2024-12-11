# Git Notes

## Summary

I can't remember all this voodoo so maybe this will help.

## Commands

### force accept remote changes

```script
git checkout --theirs . && git add .
```

### delete remote tag

```script
git push origin :tagname
```

### Commit count (current)

```shell
git rev-list --all --count
```

### Commit count (head)

```shell
git rev-list HEAD --count
```

### Current Branch Name

```shell
git branch --show-current
```

### Commits per user

```shell
git shortlog -s -n
```


### Set User Name and Email per Repo

https://stackoverflow.com/questions/42167345/git-set-local-user-name-and-user-email-different-for-each-repo

```shell
git config user.name "Matthew Whited"
git config user.email matt@whited.us
```