#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jevade'

'url handlers'

from models import User,Comment,Blog,next_id

from coroweb import get,post

import re,json,logging,hashlib,base64,asyncio,time
import markdown2

from aiohttp import web
from apis import Page,APIValueError,APIResourceNotFoundError,APIPermissionError,APIError
from config import configs

COOKIE_NAME='awesession'
_COOKIE_KEY = configs.session.secret

def check_admin(request):
	if request.__user__ is None:
		#%or not request.__user__.admin:
		raise APIPermissionError()

def check_root(request,UBC):
	if isinstance(UBC,Blog):
		if request.__user__ is None or not (UBC.user_id==request.__user__['id'] or request.__user__.admin):
			return False
	if isinstance(UBC,Comment):
		if request.__user__ is None or not (UBC.user_id==request.__user__['id'] or request.__user__.admin):
			return False
	if isinstance(UBC,User):
		if request.__user__ is None or not (UBC.id==request.__user__['id'] or request.__user__.admin):
			return False
	return True

def get_page_index(page_str):
	p=1
	try:
		p=int(page_str)
	except ValueError as e:
		pass
	if p<1:
		p=1
	return p

def user2cookie(user,max_age):
	expires=str(int(time.time()+max_age))
	s='%s-%s-%s_%s'%(user.id,user.password,expires,_COOKIE_KEY)
	l=[user.id,expires,hashlib.sha1(s.encode('utf-8')).hexdigest()]
	return '-'.join(l)

def text2html(text):
	lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
	return ''.join(lines)


async def cookie2user(cookie_str):
	if not cookie_str:
		return None
	try:
		L=cookie_str.split('-')
		if len(L)!=3:
			return None
		uid,expires,sha1=L
		if int(expires)<time.time():
			return None
		user=await User.find(uid)
		if user is None:
			return None
		s='%s-%s-%s_%s'%(user.id,user.password,expires,_COOKIE_KEY)
		sha2=hashlib.sha1()
		sha2.update(s.encode('utf8'))
		if sha1!=sha2.hexdigest():
			logging.info('invalid sha1')
			return None
		user.password='*******'
		return user
	except Exception as e:
		logging.exception(e)
		return None

def sortedDictValues3(adict):
	keys = adict.keys()
	keys.sort()
	return map(adict.get, keys)
@get('/')
async def index(*,page='1'):

	page_index=get_page_index(page)
	num=await Blog.findNumber('count(id)')
	p=Page(num,page_index)
	if num==0:
		blogs=[]
	else:
		blogs = await Blog.findAll(orderby='created_at desc',limit=(p.offset,p.limit))
		#blogs=[blog for b in blogs if not b.private]
	if 0:
		blogs=sorted(blogs, key=lambda blog:blog['created_at'],reverse=True) 
	else:
		blogs=sorted(blogs, key=lambda blog:blog['clicked'],reverse=True) 
	return{
		'__template__':'blogs.html',
		'blogs':blogs,
		'page':page
	}


@get('/blog/{id}')
async def get_blog(id):
	blog=await Blog.find(id)
	blog.clicked=blog.clicked+1	
	await blog.update()
	comments=await Comment.findAll('blog_id=?',[id],orderby='created_at desc')
	for c in comments:
		if c:
			c.html_content=text2html(c.content)
	if blog:
		blog.html_content=markdown2.markdown(blog.content)
	return{
		'__template__':'blog.html',
		'blog':blog,
		'comments':comments
	}



@get('/register')
def rigister():
	return{
		'__template__':'register.html'
	}

@get('/signin')
def signin():
	return{
		'__template__':'signin.html'
	}

@post('/api/authenticate')
async def authenticate(*,email,password):	
	if not email:
		raise APIValueError('email','invalid email')
	if not password:
		raise APIValueError('password','invalide password')
	users =await User.findAll('email=?',[email])
	if len(users)==0:
		raise APIValueError('email','not exist email')
	user=users[0]

	#CryptoJS.SHA1(email + ':' + this.password).toString()
	#sha1.update() 向其中加字符串
	#sha1.hexdigest() 转换为sha1值
	sha1=hashlib.sha1()
	sha1.update(user.email.encode('utf8'))
	sha1.update(b':')
	sha1.update(user.password.encode('utf8'))
	if sha1.hexdigest()!=password and user.password!=password:
		raise APIValueError('password','invalid password')
	r=web.Response()
	r.set_cookie(COOKIE_NAME,user2cookie(user,86400),max_age=86400,httponly=True)
	user.password='******'
	r.content_type='application/json'
	r.body=json.dumps(user,ensure_ascii=False).encode('utf8')
	return r

@get('/signout')
def signout(request):
	referer=request.headers.get('Referer')
	r=web.HTTPFound(referer or '/')
	r.set_cookie(COOKIE_NAME,'-deleted-',max_age=0,httponly=True)
	logging.info('user signed out.')
	return r

@post('/upload')
def upload_file():
    if request.method == 'POST':
        f = request.files['files[]']
        filename = f.filename
        minetype = f.content_type
        f.save('static/' + filename)
    return json.dumps({"files": [{"name": filename, "minetype": minetype}]})

@get('/upload')
def upload_file():
    if request.method == 'POST':
        f = request.files['files[]']
        filename = f.filename
        minetype = f.content_type
        f.save('static/' + filename)
    return json.dumps({"files": [{"name": filename, "minetype": minetype}]})

@get('/manage/')
def manage():
	return 'redirect:/manage/comments'

@get('/manage/comments')
def manage_comments(*,page='1'):
	return {
		'__template__':'manage_comments.html',
		'page_index':get_page_index(page),
	}

@get('/manage/blogs')
def manage_blogs(*,page='1'):
	return {
	'__template__':'manage_blogs.html',
	'page_index':get_page_index(page),
	}

@get('/blogs/create')
def create_blog():
	return {
		'__template__':'blog_edit.html',
		'id':'',
		'action':'/api/blogs'
	}

@get('/user/blogs/edit')
def edit_blog(*,id):
	return{
		'__template__':'blog_edit.html',
		'id':id,
		'action':'/api/blogs/%s'%id
	}

@get('/manage/users')
def manage_user(*,page='1'):
	return{
		'__template__':'manage_users.html',
		'page_index':get_page_index(page)
	}

@get('/api/comments')
async def api_comments(*,page='1'):
	page_index = get_page_index(page)
	num=await Comment.findNumber('count(id)')
	p=Page(num,page_index)
	if num==0:
		return dict(page=p,comments=())
	else:
		comments=await Comment.findAll(orderby='created_at asc',limit=(p.offset,p.limit))
		return dict(page=p,comments=comments)


@post('/api/blogs/{id}/comments')
async def api_create_comment(id,request,*,content):
	check_admin(request)

	user=request.__user__
	if not user:
		raise APIPermissionError('please sign in')
	
	if not content or not content.strip():
		raise APIValueError('content','content cannot be empty ')
	blog=await Blog.find(id)
	if not blog:
		raise APIResourceNotFoundError('Blog not found')
	
	comments=Comment(blog_id=blog.id,user_id=user.id,user_name=user.name,user_image=user.image,content=content.strip(),created_at=time.time())
	await comments.save()
	return comments


@post('/api/comments/{id}/delete')
async def api_delete_comment(id,request):
	check_admin(request)
	c=await Comment.find(id)
	if not c:
		raise APIResourceNotFoundError('Comment')
	if not check_root(request,c):
		raise APIPermissionError('forbidden')
	await c.remove()
	return dict(id=id)

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

@get('/api/users')
async def api_get_users(*,page='1'):
	page_index=get_page_index(page)
	num= await User.findNumber('count(id)')
	p=Page(num,page_index)
	if num==0:
		return dict(page=p,users=())
	users=await User.findAll(orderby='created_at desc',limit=(p.offset,p.limit))
	for u in users:
		u.password='*******'
	return dict(page=p,users=users)


@post('/api/users')
async def api_register_user(*,email,name,password,image):
	if not name or not name.strip():
		raise APIValueError('name')
	if not email or not _RE_EMAIL.match(email):
		raise APIValueError('email')
	if not password or not _RE_SHA1.match(password):
		raise APIValueError('password')
	users=await User.findAll('email=?',[email])
	if len(users)>0:
		raise APIError('register:failed','email','email is already used')
	uid=next_id()
	user=User(id=uid,name=name.strip(),admin=False,email=email,password=password.encode('utf8'),image=image)
	await user.save()
	r=web.Response()
	r.set_cookie(COOKIE_NAME,user2cookie(user,86400),max_age=86400,httponly=True)
	user.password='******'
	r.content_type='application/json'
	r.body=json.dumps(user,ensure_ascii=False).encode('utf8')
	return r

@get('/api/blogs')
async def api_blogs(*,page='1'):
	page_index=get_page_index(page)
	num= await Blog.findNumber('count(id)')
	p=Page(num,page_index)
	if num==0:
		return dict(page=p,blogs=())
	blogs=await Blog.findAll(orderby='created_at desc',limit=(p.offset,p.limit))	
	return dict(page=p,blogs=blogs)



@get('/api/blogs/{id}')
async def api_get_blog(*,id):
	blog=await Blog.find(id)
	return blog

@post('/api/blogs')
async def api_create_blog(request,*,name,summary,content,private=1):
	check_admin(request)
	if not name or not name.strip():
		raise APIValueError('name','name can not be empty')
	if not summary or not summary.strip():
		#raise APIValueError('summary','summary can not be empty')
		sunmmary=None
	if not content or not content.strip():
		raise APIValueError('content','content cannot be empty ')
	user=await User.findAll('email=?',[request.__user__.email])	
	blog=Blog(user_id=request.__user__.id,user_name=request.__user__.name,private=private,user_image=request.__user__.image,name=name.strip(),summary=summary.strip(),content=content.strip())
	await blog.save()
	return blog

def sortBlog(blogs):
	if 0:
		blogs=sorted(blogs, key=lambda blog:blog['created_at'],reverse=True) 
	else:
		blogs=sorted(blogs, key=lambda blog:blog['clicked'],reverse=True) 
	return blogs

@get('/user/{id}')
async def user_id(id):
	
	user=await User.find(id)
	blogs=await Blog.findAll('user_id=?',[id],orderby='created_at desc')
	if 0:
		blogs=sorted(blogs, key=lambda blog:blog['created_at'],reverse=True) 
	else:
		blogs=sorted(blogs, key=lambda blog:blog['clicked'],reverse=True) 
	return{
		'__template__':'profile.html',
		'user':user,
		'blogs':blogs
	}


@post('/api/blogs/{id}')
async def api_update_blog(request,*args,**kw):

	id=kw['id']
	name=kw['name']
	summary=kw['summary']
	content=kw['content']
	private=kw['private']

	blog=await Blog.find(id)

	if not check_root(request,blog):
		#request.__user__['admin']):
		raise APIPermissionError('not admin,forbidden to this ')

	if not name or not name.strip():
		raise APIValueError('name','name can not be empty')
	if not summary or not summary.strip():
		raise APIValueError('summary','summary can not be empty')
	if not content or not content.strip():
		raise APIValueError('content','content cannot be empty ')
	blog.name=name.strip()
	blog.summary=summary.strip()
	blog.content=content.strip()
	blog.private=private
	await blog.update()
	return blog

@post('/api/blogs/{id}/delete')
async def api_delete_blog(request,*,id):
	check_admin(request)
	blog=await Blog.find(id)
	if not check_root(request,blog):
		raise APIPermissionError('permission','没有权限删除')
	await blog.remove()
	return dict(id=id)



@post('/api/user/{id}/delete')
async def api_delete_user(request,*,id):
	user=await User.find(id)
	if user.admin:
		raise APIPermissionError('permission','无法删除管理员')
	check_admin(request)
	blogs=await Blog.findAll('user_id=?',[id],orderby='created_at desc')
	if blogs:
		for blog in blogs:
			if not check_root(request,blog):
				raise APIPermissionError('permission','没有权限删除')
			await blog.remove()

	comments=await Comment.findAll('user_id=?',[id],orderby='created_at desc')
	if comments:
		for comment in comments:
			if not check_root(request,comment):
				raise APIPermissionError('permission','没有权限删除')
			await comment.remove()
	
	
	if not check_root(request,user):
		raise APIPermissionError('permission','没有权限删除')
	await user.remove()


	return dict(id=id)
