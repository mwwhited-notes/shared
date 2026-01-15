When you update `.gitmodules` directly, you need to synchronize those changes with your local repository. Here's how to do it:

**If you've already committed the changes to `.gitmodules`:**

```bash
git submodule sync
git submodule update --init --recursive
```

The `git submodule sync` command updates your local git configuration to match what's in `.gitmodules`, and then `update --init --recursive` fetches the submodules.

**If you haven't committed yet:**

First, stage and commit the `.gitmodules` changes:

```bash
git add .gitmodules
git commit -m "Update submodule configurations"
```

Then sync and update:

```bash
git submodule sync
git submodule update --init --recursive
```

**For specific scenarios:**

If you changed a submodule URL in `.gitmodules`, you might also need to update the remote:

```bash
git submodule sync --recursive
git submodule update --init --recursive
```

If submodules are already cloned but pointing to the wrong location, you can force the update:

```bash
git submodule sync --recursive
git submodule update --init --recursive --force
```

**To verify everything worked:**

```bash
git submodule status
```

This shows the commit hash, path, and branch of each submodule to confirm they match your `.gitmodules` settings.

Is there a specific issue you're running into with the submodule update, or did you change the URL/path of a submodule?