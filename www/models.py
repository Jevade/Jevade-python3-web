import time,uuid
from orm import BooleanField,StringField,IntegerField,FloatField,TextField,Model

def next_id():
	return '%015d%s00'%(int(time.time()*1000),uuid.uuid4().hex)
class User(Model):
	__table__='users'
	id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	email=StringField(ddl='varchar(50)')
	password=StringField(ddl='varchar(50)')
	admin=BooleanField()
	name=StringField(ddl='varchar(50)')
	image=StringField(ddl='varchar(50)')
	created_at=FloatField(default=time.time)
class Blog(Model):
	__table__='blogs'
	id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	user_id=StringField(ddl='varchar(50)')
	user_name=StringField(ddl='varchar(50)')
	user_image=StringField(ddl='varchar(500)')
	summary=StringField(ddl='varchar(500)')
	name=StringField(ddl='varchar(50)')
	private=BooleanField()
	content=TextField()
	created_at=FloatField(default=time.time)
	clicked=IntegerField(default=0)
	comments=IntegerField(default=0)
class Comment(Model):
	__table__ = 'comments'
	id=StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	blog_id=StringField(ddl='varchar(50)')
	user_id=StringField(ddl='varchar(50)')
	user_name=StringField(ddl='varchar(50)')
	user_image=StringField(ddl='varchar(500)')
	content=TextField()
	created_at=FloatField(default=time.time)
