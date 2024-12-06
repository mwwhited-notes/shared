# Create Network Backup for HomeSeer

## Summary

This is a simplified set of instructions to mount a network share that can be used to backup HS4-pi

## Details

1. Create NFS share on desired server.
2. log into the terminal on HS4 and mount the NFS share
   a. mkdir /mnt/sharepoint
   b. mount <ipaddress>:/nfs/sharepoint /mnt/sharepoint
   b. mkdir /mnt/sharepoint/backups
3. Add the NFS share to `/etc/fstab` on the HS4
4. Update the backup `send to` on HS4 web console to new path `/mnt/sharepoint/backups`
5. Test backup by running manual backup
6. ensure new backup exists



sudo rsync -azh --no-perms --no-owner --no-group /usr/local/HomeSeer /mnt/sharepoint/HomeSeer