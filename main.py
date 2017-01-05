#!/usr/bin/env python3

import sys

from ctl import settings, lib


if __name__ == "__main__":
    argv = list(sys.argv)
    argc = len(argv)
    if argc < 5:
        sys.exit("Usage: (source) ctl.sh action(s) module(s)")

    try:
        dry_run = True if argv[-1] == "dry_run" else False
        is_sourced = True if argv[-2] == "true" else False
        argv = argv[1:-2]
        # make them 'globally' accessible
        settings._is_sourced = is_sourced
        settings._dry_run = dry_run

        action_args, module_args = lib.parse_args(argv)
    except ValueError as e:
        sys.exit(str(e))

    for action in action_args:
        for module in module_args:
            module.do(action)
