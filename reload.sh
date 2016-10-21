#!/usr/bin/env bash

# Hot reload code on Gunicorn
pidfile=$(ls /tmp/gunicorn*.pid | sort -n -t - -k 2 | tail -n 1)
kill -HUP $(cat $pidfile)
