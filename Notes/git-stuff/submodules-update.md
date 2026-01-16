To make sure your **submodules are updated to the latest commit on their tracked branch** (not just the commit pinned in the superproject), use:

```bash
git submodule update --remote
```

### Commonly useful variants

**Update all submodules to the latest commit of their configured branch**

```bash
git submodule update --remote --recursive
```

**Initialize missing submodules and update them**

```bash
git submodule update --init --remote --recursive
```

### How this works

* Each submodule can be configured to track a branch (instead of a fixed commit).
* Git reads this from `.gitmodules`, for example:

  ```ini
  [submodule "libs/foo"]
      path = libs/foo
      url = https://github.com/example/foo.git
      branch = main
  ```
* `--remote` tells Git to fetch from the submodule’s remote and checkout the **latest commit on that branch**.

### If the branch is not configured

If no branch is set, Git defaults to `HEAD`. To set one:

```bash
git config -f .gitmodules submodule.<name>.branch main
git submodule sync
```

### After updating

Remember: updating submodules changes their commit pointer in the parent repo, so you must commit it:

```bash
git status
git commit -am "Update submodules"
```

If you want, I can also explain:

* how this differs from `git pull --recurse-submodules`
* how to force all submodules to track `main`
* or how CI should handle submodules consistently
