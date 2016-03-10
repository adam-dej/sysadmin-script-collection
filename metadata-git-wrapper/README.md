# metadata-git-wrapper

Simple wrapper around git which keeps tracks of metadata of files and folders. For FreeBSD.

This script generates metadata of all files in a repository and restores them afterwards. Therefore it can be used for keeping `/etc` under git. It relies on BSDs `fmtree` utility.

This solution is extremely minimalistic, therefore it is really easy to customize and integrate to existing solutions or automation.

## Ugly hack warning

This is an ugly hack I am not proud of. If somebody comes up with a better solution, I would be extremely happy.
