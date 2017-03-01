from smartHouse.models import *
for i in range(12):
    q=room(state=False,name=str('room'+str(i)))
    q.save()