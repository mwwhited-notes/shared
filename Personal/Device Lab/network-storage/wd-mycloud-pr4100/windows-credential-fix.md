# Windows Credential Persistence Issue - PR4100

## Problem

Windows does not persist credentials for WD My Cloud PR4100 network shares. Requires re-entering password on every connection or reboot.

## Solutions

### Solution 1: Persistent Network Drive Mapping

**Map drive with explicit credential storage:**

1. Open Command Prompt as Administrator
2. Map drive with persistent flag:
   ```cmd
   net use Z: \\MYCLOUD-PR4100\sharename /user:username password /persistent:yes
   ```

3. Verify mapping persists:
   ```cmd
   net use
   ```

**Alternative: PowerShell method:**
```powershell
New-PSDrive -Name "Z" -PSProvider "FileSystem" -Root "\\MYCLOUD-PR4100\sharename" -Credential (Get-Credential) -Persist
```

---

### Solution 2: Windows Credential Manager

**Manually add credential:**

1. Open **Control Panel** → **Credential Manager**
2. Click **Windows Credentials**
3. Click **Add a Windows credential**
4. Enter:
   - Internet or network address: `MYCLOUD-PR4100` (or IP address)
   - User name: `username`
   - Password: `your-password`
5. Click **OK**

**Verify stored credentials:**
```cmd
cmdkey /list
```

**If credential exists but not working, delete and re-add:**
```cmd
cmdkey /delete:MYCLOUD-PR4100
cmdkey /add:MYCLOUD-PR4100 /user:username /pass:password
```

---

### Solution 3: Registry Fix for SMB Credential Persistence

**Warning: Requires registry edit**

1. Open Registry Editor (`regedit`)
2. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa`
3. Find or create DWORD: `TokenLeakDetectDelaySecs`
4. Set value: `86400` (24 hours in seconds)
5. Reboot

**Alternative registry fix for NAS-specific issues:**

Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters`

Create/modify DWORD values:
- `AllowInsecureGuestAuth` = `1` (if PR4100 uses guest auth)
- `EnableSecuritySignature` = `0` (disable SMB signing if causing issues)

Reboot after changes.

---

### Solution 4: Group Policy (Windows Pro/Enterprise)

1. Open **Local Group Policy Editor** (`gpedit.msc`)
2. Navigate to: **Computer Configuration** → **Windows Settings** → **Security Settings** → **Local Policies** → **Security Options**
3. Find: **Network security: LAN Manager authentication level**
4. Set to: **Send LM & NTLM - use NTLMv2 session security if negotiated**
5. Run `gpupdate /force`

---

### Solution 5: Use IP Address Instead of Hostname

Sometimes hostname resolution causes credential issues.

**Find PR4100 IP address:**
```cmd
ping MYCLOUD-PR4100
```

**Map using IP:**
```cmd
net use Z: \\192.168.x.x\sharename /user:username password /persistent:yes
```

---

### Solution 6: Check PR4100 SMB Settings

**On PR4100 web interface:**

1. Go to **Settings** → **Network**
2. Check SMB version (should be SMB 2.0+ for Windows 10/11)
3. Ensure **Windows File Service** is enabled
4. Check user permissions are correct

**SSH into PR4100 (if enabled):**
```bash
# Check Samba configuration
cat /etc/samba/smb.conf

# Check user authentication
pdbedit -L
```

---

## Verification Steps

After applying fix:

1. **Reboot Windows PC**
2. **Test automatic connection:**
   ```cmd
   dir Z:
   ```
3. **Check if credential persists after reboot**
4. **Verify credential in manager:**
   ```cmd
   cmdkey /list | findstr MYCLOUD
   ```

---

## Why This Happens

**Common causes:**

1. **SMB version mismatch** - Windows 10/11 defaults to SMB 3.0, older NAS may use SMB 1.0/2.0
2. **Credential leak detection** - Windows security feature that clears credentials
3. **Hostname vs IP resolution** - DNS cache issues
4. **Group policy restrictions** - Corporate or home network policies
5. **PR4100 authentication method** - Guest auth, local auth, or AD integration

---

## Alternative: Nextcloud Eliminates This Problem

**Consider deploying Nextcloud on PR4100:**

- Uses web authentication (OAuth)
- Desktop client syncs files locally (no constant network auth)
- Mobile app uses app password (stored once)
- No Windows credential manager involved
- Better cross-platform support

See: [Self-Hosted Cloud Services Project](../../../projects/self-hosted-cloud-services/) (if created)

---

## Troubleshooting

### Still not working?

**Check Windows event logs:**
```
Event Viewer → Windows Logs → System
Filter: Source = LanmanWorkstation or LanmanServer
```

**Test SMB connection manually:**
```cmd
net use \\MYCLOUD-PR4100\IPC$ /user:username password
```

**Check if SMB1 is disabled (Windows 10+):**
```powershell
Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
```

**Enable if needed (not recommended for security):**
```powershell
Enable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
```

---

*Last updated: 2026-01-07*
