# sudo-git-wrapper

## Ugly hack warning

This is an ugly hack I am not proud of. If somebody comes up with a better solution, I would be extremely happy.

## How it works

Allows for using git as root with git config of user who has sudo-ed to root. It does this by getting the real user name using `logname`. It then gets home folder of the real user, and sets `HOME` variable for `git` process, which in turn then uses `.gitconfig` of the given user.

## Where it works

This script was tested on FreeBSD 10.2.
