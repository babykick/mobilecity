# Requirement && Infrastructure 
 
### Web framework
Django 1.8
geodjango

with:
django-bootstrap3
djangorestframework
djangorestframework-oauth
pip install django-social-auth
pip install djangorestframework-gis
pip install django-rest-swagger
pip install django-redis
pip install shell_plus
pip uninstall south # not use south in django 1.8, keep it may throws error in django-celery
pip install django-celery
pip install django-braces

### Database:
Postgresql 9.3 or 9.4 with postgis

### NoSQL:
couchdb
pip install couchdbkit

### Cache, Queue & push notification
redis
celery-with-redis
gearman
pyapns

### Backend
Nginx 
gunicorn

### Web Front
Bootstrap


# Web scraper
scrapy 1.0
scrapy-redis
scrapy-djangoitem
pip install service_identity

# 分词, NLP
jieba
nltk