# Using GitVersion

## Summary

[Gitversion](https://gitversion.net/docs/) is a tool to generate version numbers based on your git
repository commit history.

## Configure

To customize GitVersion create a `GitVersion.yml` file at the root of your repository.  Use this file to configure your repository.  For framework libraries it is suggested to use `Continuous Deliver` for
applications such as native tools, uis and website use `Mainline Development`

* [Versioning Modes](https://gitversion.net/docs/reference/versioning-modes/versioning-mode)

## Install and Use locally

`GitVersion` is a `dotnet tool`.  This tool allows you you see and test what GitVersion will calculate for your CI/CD pipeline.  

### Install Globally

```shellcommand
dotnet tool install --global gitversion.tool
```

### Display Current Version Options

From within a directory for a git repository

```shellcommand
dotnet gitversion
```

### Show current configuration

```shellcommand
dotnet gitverion --showconfig
```

## Use in CI/CD Pipelines

### Local Batch Files

```batch
git fetch --prune
FOR /F "tokens=* USEBACKQ" %%g IN (`dotnet gitversion /output json /showvariable FullSemVer`) DO (SET BUILD_VERSION=%%g)
ECHO Building Version=  "%BUILD_VERSION%"
```

### Local Linux Scripts
```bash
git fetch --prune
buildVersion=`dotnet gitversion /output json /showvariable FullSemVer`
echo GitVersion= $buildVersion
```

### Azure Devops

Add these to under the `steps` of the job you want to version.

```yaml
- task: gitversion/setup@0
  displayName: Install GitVersion
  inputs:
    versionSpec: '5.1.3'
- task: gitversion/execute@0
  displayName: Use GitVersion
  inputs:
    useConfigFile: true
    configFilePath: 'GitVersion.yml'
- script: |
          echo FullSemVer=$(fullSemVer)
          echo ##vso[build.updatebuildnumber]$(fullSemVer)
          echo ##vso[task.setvariable variable=fullSemVer]$(fullSemVer)
```
