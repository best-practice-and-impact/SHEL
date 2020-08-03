#!/bin/sh
source venv/bin/activate
flask db upgrade
python3 user_setup.py
exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app