from django_cron import CronJobBase, Schedule
import time
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    RUN_AT_TIMES =['01:52','01:53','01:54']
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins = 1)
    code = 'schedule.check'

    def do(self):
            with open("test.txt","a") as myfile:
                myfile.write("appended text")

class checkSwagbucksCode(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'schedule.Check Swagbucks Code'
    def do(self):
        pass

