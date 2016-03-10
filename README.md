Sysadmin Scripts Collection
===========================

A collection of scripts that make my sysadmin life better:

`properly`
----------

Runs an administrative/maintenance command properly: with backups before and after, logging the action and not leaving a mess behind.

`sudo-git-wrapper`
------------------

Use git as root with your user config.

`metadata-git-wrapper`
----------------------

Simple minimalistic wrapper around git which stores metadata about files: for `/etc` under git (FreeBSD only).

`repo-dirty-checker`
--------------------

Periodically checks whether someone has left a mess behind in `/etc` under git.

`zfs-snapmanage-shell`
----------------------

Limited login shell which allows management of zfs snapshots only. Optionally it can limit operation only to datasets specific to a given jail.
