# ltp_test_td
TD事物


# 数据库迁移
    python manage.py collectstatic
    python manage.py makemigrations
    python manage.py migrate

# 服务启动
    python3 manage.py runserver 0.0.0.0:8000  

# gunicorn部署
    pgrep -f "gunicorn"
    pkill -f "gunicorn"
    gunicorn QualityCenter.wsgi:application -c gunicorn.conf.py 
    nohup celery -A QualityCenter worker -l info > /dev/null 2>&1 & 
    nohup celery -A QualityCenter beat -l info > /dev/null 2>&1 & 

