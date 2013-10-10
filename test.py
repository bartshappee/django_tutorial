import os
import django

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

print (SITE_ROOT)


DATABASE_NAME = os.path.join(SITE_ROOT, 'db') + '/development.sqllite3'

print(DATABASE_NAME)
