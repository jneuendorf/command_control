#!/usr/bin/env bash

# determine whether i am being called like `source ctl.sh ...` or not
if [ "$0" == "$BASH_SOURCE" ]; then
    is_sourced=false
    command_control_dir=`dirname $0`
else
    is_sourced=true
    command_control_dir=`dirname $BASH_SOURCE`
fi

# $@ == given arguments
python3 $command_control_dir/main.py "$@" "$is_sourced" dry_run
# TODO: have another "type or running"
#       -> script for eval only gets the last cd command (without running stuff)
eval "`python3 $command_control_dir/main.py $@ $is_sourced real_run`"
