#!/usr/bin/env bash

# determine whether i am being called like `source ctl.sh ...` or not
if [ "$0" == "$BASH_SOURCE" ]; then
    is_sourced=false
else
    is_sourced=true
fi

# $@ == given arguments
python3 ./main.py "$@" "$is_sourced" dry_run
eval "`python3 ./main.py $@ $is_sourced real_run`"
