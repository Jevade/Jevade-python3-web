#!/usr/bin/env python3
#-*-coding:utf8 -*-

import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from models import User,Blog,Comment

from datetime import datetime
from aiohttp import web
import orm
from coroweb import get
from jinja2 import Environment,FileSystemLoader
import orm
from coroweb import add_static,add_routes
from handlers import cookie2user,COOKIE_NAME

def init_jinja2(app,  **kw):
	logging.info('init_jinjia2......%s'%kw)
	options=dict(
		autoescape = kw.get('autoescape',True),
			#dict.get(key,default)
			#key -- 这是要搜索在字典中的键。
			#default -- 这是要返回键不存在的的情况下默认值。
		block_start_string=kw.get('block_start_string','{%'),
		block_end_string=kw.get('block_end_string','%}'),
		variable_start_string=kw.get('variable_start_string','{{'),
		variable_end_string=kw.get('variable_end_string','}}'),
		auto_reload=kw.get('auto_reload',True)
		)
	path=kw.get('path',None)
	if path is None:
		path=os.path.join (os.path.dirname(os.path.abspath(__file__)),'templates')#获取—file的绝对路径
		#再获得上层文件夹，再同templates链接，，，获得本文件夹下templates文件夹的路径
	logging.info('templates path:%s'%path)
	env=Environment(loader=FileSystemLoader(path),**options)#初始化环境的参数
	filters=kw.get('filters',None)
	if filters is not None:
		for name ,f in filters.items():
			env.filters[name] = f
	app['__templating__'] = env#将env作为

async def logger_factory(app,handler):
	async def logger(request):
		logging.info('Request %s:%s'%(request.method,request.path))
		return (await handler(request))
	return logger

async def auth_factory(app,handler):
	async def auth(request):
		logging.info('checked user:%s %s'%(request.method,request.path))
		request.__user__=None
		cookie_str=request.cookies.get(COOKIE_NAME)
		print(cookie_str)
		if cookie_str:
			user=await cookie2user(cookie_str)
			if user:
				request.__user__=user

		if request.path.startswith('/manage/') and (request.__user__ is None):
			return web.HTTPFound('/signin')
		return (await handler(request))
	return auth

#@asyncio.coroutine
async def data_factory(app,handler):
	#@asyncio.coroutine
	async def parse_data(request):
		if request.method=='POST':
			if request.content_type.startswith('application/json'):
				request.__data__=await request.json()
				logging.info('request json:%s'%str(request.__data__))
			elif request.content_type.startswith('application/x-www-from-urlencoded'):
				request.__data__=await request.post()
				logging.info('request json:%s'%str(request.__data__))
			return (await handler(request))
		return parse_data


#@asyncio.coroutine
async def response_factory(app,handler):
	#@asyncio.coroutine
	async def response(request):
		logging.info('Response handler...')		
		r=await handler(request)
		
		if isinstance(r,web.StreamResponse):
			return r 
		if isinstance(r,bytes):
			resp=web.Response(body=r)
			resp.content_type='application/octet-stream'
			return resp
		if isinstance(r,str):
			if r.startswith('redirect:'):
				return web.HTTPFound(r[9:])
			resp=web.Response(body=r.encode('utf8'))
			resp.content_type='text/html;charset=utf8'
			return resp		
		if isinstance(r,dict):
			template=r.get('__template__')
			if template is None:

				resp=web.Response(body=json.dumps(r,ensure_ascii=False,default=lambda x:x.__dict__).encode('utf-8'))
				resp.content_type='application/json;charset=utf8'
				return resp 
			else:
				r['__user__']=request.__user__
				resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
				#dicts=app['__templating__'].get_template(template).render(**r)
				#resp=web.Response(body=dicts.encode('utf8'))
				
				resp.content_type='text/html;charset=utf8'
				return resp	
		if isinstance(r,int) and r>=100 and r<600:
			web.Response(r)
		if isinstance(r,tuple) and len(r)==2:
			t,m=r
			if isinstance(t,int) and t>=100 and t<600:
				return web.Response(t,str(m))
		resp = web.Response(body=str(r).encode('utf8'))
		resp.content_type='text/html;charset=utf8'
		return resp
	
	return response
		

def datetime_filter(t):
	delta=int(time.time()-t)
	if delta<60:
		return u'1分钟前'
	if delta<3600:
		return u'%s分钟前'%(delta//60)
	if delta<3600*24:
		return u'%s小时前'%(delta//3600)
	if delta<3600*24*7:
		return u'%s天前'%(delta//86400)
	dt=datetime.fromtimestamp(t)
	return u'%s年%s月%s日'%(dt.year,dt.month, dt.day)

#@asyncio.coroutine
async def init(loop):
	await orm.create_pool(loop=loop,host='192.168.42.1',port=3306,user='root',password='123456',db='awesome')
	app=web.Application(loop=loop,middlewares=[logger_factory,response_factory,auth_factory])
	init_jinja2(app,filters=dict(datetime=datetime_filter))
	add_routes(app,'handlers')
	add_static(app)
	port=9001
	srv=await loop.create_server(app.make_handler(),'',port)
	logging.info('server started at http://127.0.0.1:%s'%port)
	return srv



loop=asyncio.get_event_loop ()
loop.run_until_complete(init(loop))
loop.run_forever()
if __name__ == '__main__':
	print(123)
