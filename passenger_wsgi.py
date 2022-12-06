import os
import sys
from personal.wsgi import application
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal.settings')
