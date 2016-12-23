#!/usr/bin/env python3


if __name__ == "__main__":
    from ctl import modules
    import sys

    if len(sys.argv) == 1:
        sys.exit("Usage: ctl.py action module")

    action = sys.argv[1]

    mysql = modules.mysql.MySql()
    print(mysql.get_tasks())
