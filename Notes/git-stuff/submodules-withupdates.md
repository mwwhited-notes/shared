By default, submodules are **pinned** to a specific commit recorded in the parent repo. To pull the **latest commit from a submodule’s target branch** instead, you need to explicitly tell Git to update submodules by branch.

Here are the correct ways to do it.

---

## One-time: pull latest from each submodule’s tracked branch

```bash
git submodule update --remote --merge
```

* `--remote` → fetches the latest commit from the submodule’s configured branch
* `--merge` → merges it into the checked-out submodule branch (safer than rebase)

If you want this for **nested submodules too**:

```bash
git submodule update --remote --merge --recursive
```

---

## Make sure each submodule has a target branch configured

Check `.gitmodules`:

```ini
[submodule "path/to/submodule"]
    path = path/to/submodule
    url = https://...
    branch = main   # or develop, etc.
```

If `branch` is missing, Git defaults to the submodule’s remote `HEAD`.

To set it:

```bash
git submodule set-branch --branch main path/to/submodule
```

Then commit the `.gitmodules` change.

---

## Full workflow (common pattern)

```bash
git pull
git submodule update --remote --merge --recursive
git status
```

If submodules advanced, you must commit the new submodule SHAs in the parent repo:

```bash
git add .
git commit -m "Update submodules to latest"
```

---

## Optional: make this the default behavior

```bash
git config --global submodule.recurse true
git config --global submodule.fetchJobs 0
```

> ⚠️ Important: Pulling latest submodule commits **changes the parent repo’s state**. That’s why Git does *not* do this automatically.

---

### Summary

| Goal                             | Command                                             |
| -------------------------------- | --------------------------------------------------- |
| Pull pinned submodule versions   | `git submodule update --init --recursive`           |
| Pull latest from target branches | `git submodule update --remote --merge --recursive` |
| One-time branch set              | `git submodule set-branch --branch main <path>`     |

If you want a **single alias command** that does all this in one shot, I can give you a clean one-liner.
