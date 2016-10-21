#!/usr/bin/env bash

# Run Django on Gunicorn
PIDFILE="/tmp/gunicorn-$(date +%s).pid"
gunicorn \
    --pid $PIDFILE \
    --daemon \
    --bind 0.0.0.0:8000 \
    --worker-class gevent \
    --workers 3 \
    --pythonpath hot_code_reload \
    --settings hot_code_reload.settings \
    hot_code_reload.wsgi:application
sleep 3
if [ -f $PIDFILE ]; then
    echo "...Gunicorn boot successful"
    exit 0
else
    echo "...Gunicorn boot failed"
    exit 1
fi