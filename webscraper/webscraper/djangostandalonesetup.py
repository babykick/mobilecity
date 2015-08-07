import os, sys
import django
# Setup environ
p =  os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, os.pardir)
print p
sys.path.append(p)
os.environ['DJANGO_SETTINGS_MODULE'] = 'lordrecommender.settings'
django.setup()