from projects.models import *

techs = [Technology(name="Django"), Technology(name="HTML")]

for t in techs:
    t.save()