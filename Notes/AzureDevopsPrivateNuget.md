# Create Private NuGet feed for use with Azure Devops

## Summary

It is possible to host and publish to a private NuGet feed within Azure DevOps

## Process

* Under `Artifacts` click `Create Feed`
  * Name the feed as desired
  * select user visilibity (probably "Azure AD" or at least members of Project
  * upstream is optional.  
  * set scope (probably for your project)
* Within your project create a `nuget.config` file as below
  * set `NameOfYourFeed` as desired
  * set `PathToYourFeed` as shown under the `connect to feed` in the artifact from above

```nuget.config
<configuration>
    <packageSources>
        <add key="NameOfYourFeed" value="PathToYourFeed" />
        <add key="nuget.org" value="https://api.nuget.org/v3/index.json" protocolVersion="3" />
    </packageSources>
</configuration>
```

* Add steps to build pipeline
  * Authentication Pipeline to NuGet
  * Add `dotnet nuget push`
  * Ensure `dotnet pack` includes versioning

### Pipeline NuGet Authentication
  
```yaml.azuredevops
    - task: NuGetAuthenticate@0
      displayName: 'NuGet Authenticate'
```

### Pipeline Nuget Push

```yaml.azuredevops  
    - task: DotNetCoreCLI@2
      displayName: Push Packages to Private NuGet
      inputs:
        command: 'push'
        packagesToPush: '$(build.artifactStagingDirectory)/**/*.nupkg'
        nuGetFeedType: 'internal'
        publishVstsFeed: 'FEED-ID'
```  

### Pipeline Dotnet Pack Versioning

```yaml.azuredevops  
    - task: DotNetCoreCLI@2
      displayName: Package to Staging directory
      inputs:
        command: custom
        custom: 'pack'
        arguments: 'yoursolution.slnproj -c=$(BUILD_CONFIGURATION) -o $(Build.ArtifactStagingDirectory) /p:Version=$(fullSemVer)'
        verbosityRestore: Minimal
        verbosityPack: Minimal
        feedsToUse: select
        vstsFeed: personalnugetfeed
        nuGetFeedType: internal
        includeNuGetOrg: true
```


## Notes

* https://docs.microsoft.com/en-us/azure/devops/artifacts/concepts/feeds?view=azure-devops
* https://www.mallibone.com/post/private-nuget-feed-azure-devops
* https://medium.com/@ginomessmer/get-started-with-private-nuget-feeds-in-azure-devops-8c7b5f022a68
* https://newsignature.com/articles/want-to-host-your-private-nuget-feed-use-azure-devops/
* https://stackoverflow.com/questions/54621893/push-nuget-package-to-azure-devops