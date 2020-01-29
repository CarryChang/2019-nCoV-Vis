export PATH=$PATH:/usr/local/bin
#!/bin/bash
cd /home/carry/Outbreak_BD/Outbreak_BD_server/frontend_code
kill `cat log/gunicorn.pid`
# ps -ef|grep "gunicorn" |grep -v grep|cut -c 9-15|xargs kill -9
rm -rf log/*
source /home/carry/p36venv/bin/activate
#pstree -ap|grep gunicorn
gunicorn  -c gun.py front_server:app
deactivate