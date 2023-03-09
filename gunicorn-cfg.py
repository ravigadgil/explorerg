wsgi_app = "LearningPortal.wsgi:application"
bind = '0.0.0.0:8000'
workers = 1
accesslog = '-'
reload = True
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
