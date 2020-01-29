cd /home/carry/Outbreak_BD/spider
/home/carry/p36venv/bin/python data_spider.py > /home/carry/Outbreak_BD/spider/log/spider_log_$(date +\%Y-\%m-\%d).log 2>&1
find /home/carry/Outbreak_BD/log  -mtime +5 -name "*.log"  -exec rm -rf {} \;
