#!/usr/bin/env python3

import argparse
import cmd


class Shell(cmd.Cmd):
    intro = 'Welcome to interactive ZFS SnapManage shell.\n' \
            'Type help or ? for list commands.\n'
    prompt = '(SnapManage) '

    def do_snapshot(self, arg):
        pass

    def do_rollback(self, arg):
        pass

    def do_list(self, arg):
        pass

    def do_EOF(self, arg):
        print()
        return True

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--dataset',
                    help='Dataset to be operated on', required=True)
parser.add_argument('-c', '--command',
                    help='Command to be executed, starts interactive shell if ommited')

args = parser.parse_args()
dataset = args.dataset

if args.command is not None:
    Shell().onecmd(args.command)
else:
    Shell().cmdloop()
