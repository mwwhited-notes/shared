
```shell
# see https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-1---enable-the-windows-subsystem-for-linux

# Open a Powershell Terminal (Administrator) 
dism /online /disable-feature /FeatureName:Microsoft-Windows-Subsystem-Linux
dism /online /disable-feature /featurename:VirtualMachinePlatform
dism /online /disable-feature /FeatureName:Microsoft-Hyper-V
rm "$env:userprofile\.wslconfig"

# reboot

# Open a Powershell Terminal (Administrator) 
dism /online /enable-Feature /All /FeatureName:Microsoft-Windows-Subsystem-Linux /norestart
dism /online /enable-feature /All /Featurename:VirtualMachinePlatform /norestart
dism /online /enable-Feature /All /FeatureName:Microsoft-Hyper-V /norestart
bcdedit /set hypervisorlaunchtype auto

# reboot

# Open a Powershell Terminal (Administrator) 
wsl --install
```