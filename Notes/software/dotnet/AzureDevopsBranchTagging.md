# Azure DevOps Pipeline Branch Tagging 

## Summary 

It is possible to git repositories in Azure Devops as part of your automated build process.  

## Build Scripts

Manually checkout your git repository need the beginning of your job.  Ensure to persist 
credentials so you can authenticate against git later.  

```yaml
  - checkout: self
    clean: true
    persistCredentials: true
    
```

Near the end if your build process you can add a script to add a tag to git.

```yaml
  - script: |
            git config --global user.name "AzureDevOps Agent"
            git tag "$(buildVersionTag)" --force
            git push origin "$(buildVersionTag)" --force
            echo "Tagging $(Build.Repository.Name) with $(buildVersionTag)"
    displayName: 'Tag Branch'
    condition: and(succeeded(), ne(variables['Build.Reason'], 'PullRequest'))
```

Make sure to configure the security in your project to allow the build to add tags and contibute

1. Project Settings
2. Repos/Repositories
3. Select chosen repository (or global build account)
4. Navigate to Security to build user
5. Set "Contribute" and "Create tag" to "Allow"  
