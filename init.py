#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_tutorial.settings")

    from django.core.management import execute_from_command_line

from polls.models import Poll, Choice

os.system("manage.py syncdb")

from django.utils import timezone

if 0 == Poll.objects.all().count():
	p = Poll(question="What's up?", pub_date=timezone.now())
	p.save()

if 0 == Choice.objects.all().count(): 
	p.choice_set.create(choice_text='Not much', votes=0)
	p.choice_set.create(choice_text='The sky', votes=0)
	p.choice_set.create(choice_text='Just hacking again', votes=0)
