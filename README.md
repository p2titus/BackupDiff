# BackupDiff
a small python script to aid with incremental backups

## Are you tired of manually copying over your files?
## Losing track of what does and doesn't need updating?
## Backup got you feeling the blues?

**LOOK NO FURTHER!**
With BackupDiff, you can worry no more!

Simply replace the src and dest tags in the params.json file and ensure there is no time field.
Once this is done, simply run the program. It will only update files that have been modified or created since the last backup.

Disclaimer: this has not been exhaustive tested so I would recommend doing a
dummy run before using for the first time.
This also requires both the source and backup directories to be identical. This may not be ideal for all users. A more practical (read: overblown) idea may be to use Git(tm) and treat the backup as a remote repo. If you're browsing this on github, that's probably not the worst idea in the world.

