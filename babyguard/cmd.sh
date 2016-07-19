#!/bin/bash

#nohup python manage.py runserver 0.0.0.0:10001 &
#python manage.py runserver 0.0.0.0:10001
#gunicorn -w4 -b0.0.0.0:10001 aircheck.wsgi:application
#!/bin/bash
ps aux | grep manage.py |grep 10001| grep -v grep |awk '{print $2}' | xargs -i kill -9 {}

if [ "$1" = '1' ]; then
nohup python manage.py runserver 0.0.0.0:10001 > /dev/null 2>&1 &
fi
if [ "$1" = '' ]; then
python manage.py runserver 0.0.0.0:10001
fi
if [ "$1" = '0' ]; then
python manage.py runserver 0.0.0.0:10001
fi

