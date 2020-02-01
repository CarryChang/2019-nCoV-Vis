export PATH=$PATH:/usr/local/bin
cd  /home/carry/Outbreak_BD/Outbreak_BD_server/midend_code/process
/home/carry/p36venv/bin/python  precess_train.py > log/train_log_$(date +\%Y-\%m-\%d).log 2>&1
find /home/carry/Outbreak_BD/Outbreak_BD_server/midend_code/process/log  -mtime +5 -name "*.log"  -exec rm -rf {} \;