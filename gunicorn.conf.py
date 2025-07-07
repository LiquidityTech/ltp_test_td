# -*- coding:utf-8 _*-
import os
import multiprocessing

bind = '0.0.0.0:8000'
pidfile = '/tmp/gunicorn.pid'
backlog = 2048

workers = multiprocessing.cpu_count() + 1
worker_class = 'gthread'

threads = int(480 / workers)
timeout = 60
graceful_timeout = 60

reload = True
daemon = True

accesslog = '/data/ltp_test_td/logs/gunicorn.log'
access_log_format = '%(h)s %(l)s %({REMOTE_USER}i)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = '/data/ltp_test_td/logs/gunicorn_error.log'
loglevel = 'info'

os.environ.setdefault('WERKZEUG_RUN_MAIN', 'true')


