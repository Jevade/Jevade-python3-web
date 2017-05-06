import time,uuid
from orm import BooleanField,StringField,IntegerField,FloatField,TextField,Model

def next_id():
	return '%015d%s00'%(int(time.time()*1000),uuid.uuid4().hex)
class User(Model):
	__table__='users'
	id=IntegerField(primary_key=True)
	name=StringField()
print(next_id())