import os, sys
import django
# Setup environ
sys.path.append('F:\\programing\\python\\app\\webprojects\\django\\mobilecity')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lordrecommender.settings'
django.setup()