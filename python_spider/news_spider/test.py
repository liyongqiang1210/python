import schedule
import time
import datetime

def job():
	print(time.asctime(time.localtime(time.time())))

if __name__ == '__main__':
	
	print(datetime.datetime.now().year)
	schedule.every(1).minutes.do(job)

	while True:
		schedule.run_pending()
