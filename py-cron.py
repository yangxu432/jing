import time
from datetime import date, timedelta
from subprocess import call
DAYS_TO_RUN = 30
RUN_EVERY_MINS = 60

start = date.today()
end = start + timedelta(DAYS_TO_RUN)

while start != end:
    
    
    call(["python","./Web/manage.py","runcrons"])
    time.sleep(RUN_EVERY_MINS*60)
    start = date.today()


