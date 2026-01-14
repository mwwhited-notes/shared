The recursive pull command for Git submodules is:

```bash
git pull --recurse-submodules
```

If you want to **update submodules to the commits referenced by the superproject** (the most common and safest behavior), use:

```bash
git submodule update --init --recursive
```

### Common scenarios

**Pull main repo and update submodules automatically**

```bash
git pull --recurse-submodules
```

**After pulling, ensure all nested submodules are updated**

```bash
git submodule update --init --recursive
```

**Always recurse submodules when pulling (config option)**

```bash
git config --global submodule.recurse true
```

That last one makes a plain `git pull` behave as if `--recurse-submodules` were always set.

If you want submodules to pull the *latest commits from their tracked branches* (instead of the pinned commit), say the word—there’s a slightly different command for that.
