
import os
import sys
import django.core.handlers.wsgi

activate_this = '/home/dell/Web/ENV/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

project_home = u'/home/dell/Web/jing'
if project_home not in sys.path:
    sys.path.append(project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Web.settings'

application = django.core.handlers.wsgi.WSGIHandler()    
    
