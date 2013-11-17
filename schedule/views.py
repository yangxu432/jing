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
    code = 'schedule.swagCode (Check Swagbucks Code)'
    def do(self):
        from schedule.swagCode import openPage
        from schedule.models import swagCode
        from django.conf import settings
        from django.core.mail import send_mail
        result = openPage()
        import datetime
        now = datetime.datetime.now()
        active = {}
        expired = {}
        
        for key, value in result.iteritems() :

            if value["expires"] > now:
                active.update({key:{'Code': value['code'],
                    'Worth': value['worth'], 
                    'Expires':str(value['expires'])}})
            else:
                expired.update({key:{'Code': value['code'],
                    'Worth': value['worth'], 
                    'Expires':str(value['expires'])}})

        for key, value in expired.iteritems() :
            try:
                change = swagCode.objects.get(code=value['code'],
                    worth = value['worth'],
                    expires = value['expires'])
                change.isActive = False
                change.save()
            except:
                pass

        for key, value in active.iteritems() :
            try:
                swagCode.object.get(code=value['code'],
                    worth = value['worth'],
                    expires = value['expires'])
                #data in the database
            except:
                from django.contrib.auth.models import User
                #send to all user
                allUser = User.objects.all()
                emailList = []
                for i in allUser:
                    emailList.append(i.email)



                swagCode(code=value['code'],
                    worth=value['worth'],
                    expires=value['expires'],
                    isActive=value['isActive']).save()
                #send user email new code is here
                self.code = "'schedule.swagCode ("+value['code']+")"
                send_mail(value['code']+" "+value['worth'], 'Have Fun!', settings.EMAIL_HOST_USER,
                    emailList, fail_silently=False)

        '''
        swagCode.objects.latest("id")

        for key, value in result.iteritems() :
            swagCode(code=value['code'],
                worth=value['worth'],
                expires=value['expires'],
                isActive=value['isActive']).save()
            #print value
        '''

        


