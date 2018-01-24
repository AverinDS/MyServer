"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys, site
from django.core.wsgi import get_wsgi_application
sys.path.append("/home/dmitry/MyServer/")

site.addsitedir('/home/dmitry/MyServer/.virtenv/VE/lib/python3.5/site-packages')

#sys.path.append("/home/dmitry/MyServer/server")
#sys.path.append('/home/dmitry/MyServer/.virtenv/VE/')

os.environ["DJANGO_SETTINGS_MODULE"] = "server.settings"


activate_env=os.path.expanduser("/home/dmitry/MyServer/.virtenv/VE/bin/activate_this.py")
exec(open(activate_env).read(), dict(__file__=activate_env))

application = get_wsgi_application()
