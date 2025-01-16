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

## Recover log commits

### 1. **Navigate to the Submodule Directory**
If you lost changes in a submodule, navigate to its directory:
```bash
cd path/to/submodule
```

### 2. **Check the Submodule's Reflog**
Each submodule has its own `.git` history. Run the reflog inside the submodule:
```bash
git reflog
```

Look for the commit where your changes were saved. You can restore it with:
```bash
git checkout <commit-hash>
```

### 3. **Check for Stashed Changes**
If you stashed changes in the submodule, list the stash entries inside the submodule directory:
```bash
git stash list
```

To recover the changes, apply the stash:
```bash
git stash apply stash@{0}  # Replace with the correct stash entry
```

### 4. **Look for Uncommitted Changes**
If you made changes in the submodule but didn’t commit them, you might still find them in the working directory or the index.

- **Recover uncommitted changes:**
  Run:
  ```bash
  git status
  ```
  If the changes are still in the working directory, you can commit them:
  ```bash
  git add .
  git commit -m "Recovered changes"
  ```

- **Check for staged changes:**
  If you staged but didn’t commit:
  ```bash
  git diff --cached
  ```

### 5. **Inspect the Parent Repository**
If the submodule pointer changed when you checked out another branch in the parent repository, it might no longer point to the commit containing your changes. To fix this:

1. **Find the submodule’s commit hash** in the parent repository’s reflog:
   ```bash
   git reflog
   ```
   Look for an entry like:
   ```
   HEAD@{n}: update submodule path/to/submodule
   ```

2. **Revert to the correct pointer:**
   In the submodule directory:
   ```bash
   git checkout <commit-hash>
   ```


### 6. **Check Git FSCK in the Submodule**
If all else fails, look for dangling commits in the submodule:
```bash
git fsck --lost-found
```

Inspect the dangling commits:
```bash
git show <commit-hash>
```

If you find the missing changes, create a branch:
```bash
git checkout -b recovered-branch <commit-hash>
```


### 7. **Update the Parent Repository**
Once you’ve recovered the changes in the submodule, commit the updated state in the parent repository:
```bash
cd /path/to/parent-repo
git add path/to/submodule
git commit -m "Updated submodule with recovered changes"
```
