import asyncio,os,inspect,logging,functools
from urllib import parse

from aiohttp import web

from apis import APIError

def get(path):
	def decorator(f):
		@functools.wraps(f)
		def wrapper(*args,**kw):
			return f(*args,**kw)
		wrapper.__method__='GET'
		wrapper.__route__=path
		return wrapper
	return decorator

def post(path):
	'''
	Define decorate@post('/path')
	'''
	def decorator(f):
		@functools.wraps(f)
		def wrapper(*args,**kw):
			return f(*args,**kw)
		wrapper.__method__='POST'
		wrapper.__route__=path
		return wrapper
	return decorator

def get_required_kw_args(fn):
	args=[]
	params=inspect.signature(fn).parameters
	for name,param in params.items():
		if param.kind==inspect.Parameter.KEYWORD_ONLY and param.default==inspect.Parameter.empty:
			args.append(name)
	return tuple(args)

def get_named_kw_args(fn):
	args=[]

	params=inspect.signature(fn).parameters
	print('?????????????',fn,params)
	for name,param in params.items():
		if param.kind==inspect.Parameter.KEYWORD_ONLY :
			args.append(name)
	return tuple(args)
def has_named_kw_args(fn):
	params=inspect.signature(fn).parameters
	for name,param in params.items():
		if param.kind==inspect.Parameter.KEYWORD_ONLY :
			return True
	return False

def has_var_kw_arg(fn):
	params=inspect.signature(fn).parameters
	for name,param in params.items():
		if param.kind==inspect.Parameter.VAR_KEYWORD :
			return True
	return False	

def has_request_arg(fn):
	sig=inspect.signature(fn)
	params=sig.parameters
	found=False
	for name,param in params.items():
		if name=='request':
			found=True
			continue
		if found and (param.kind!=inspect.Parameter.VAR_KEYWORD and param.kind!=inspect.Parameter.KEYWORD_ONLY and param.kind!=inspect.Parameter.VAR_POSITIONAL):
			raise ValueError('request param must be the last named param in function:%s%s'%(fn.__name__,str(sig)))
	return found

class RequestHandler(object):
	def __init__(self,app,fn):
		self.__app=app
		self.__func=fn
		self._has_request_arg=has_request_arg(fn)
		self._has_var_kw_arg=has_var_kw_arg(fn)
		self._has_named_kw_args=has_named_kw_args(fn)
		self._get_named_kw_args=get_named_kw_args(fn)
		self._get_required_kw_args=get_required_kw_args(fn)
		
	
	@asyncio.coroutine
	def __call__(self,request):
		print(request)

		print('coroweb:requestd',self._get_named_kw_args)
		kw=None
		if self._has_var_kw_arg or self._has_named_kw_args or self._get_required_kw_args:
			if request.method=='POST':
				if not request.content_type:
					return web.HTTPBadRequest('Missing Content-Type')
				ct=request.content_type.lower()
				if ct.startswith('application/json'):
					params=yield from request.json()
					if not isinstance(params,dict):
						return web.HTTPBadRequest('json object must be object')
					kw=params

				elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
					params=yield from request.post()
					kw=dict(**params)
				else:
					return web.HTTPBadRequest('unsupported Content-Type:%s'%request.content_type)
			if request.method=='GET':
				qs=request.query_string
				if qs:
					kw=dict()
					for k,v in parse.parse_qs(qs,True).items():#parse a string to argument
						kw[k]=v[0]
		if kw is None:
			kw=dict(**request.match_info)
		else:

			if not self._has_request_arg and self._has_named_kw_args:
				copy=dict()
				for name in self._get_named_kw_args:
					if name in kw:
						copy[name]=kw[name]
				kw=copy
			for k,v in request.match_info.items():
				if k in kw:
					logging.warning('duplicate arg name in named arg and kw args:%s'%k)
				kw[k]=v
		if self._has_request_arg:
			kw['request']=request
		if self._has_request_arg:
			for name in self._get_required_kw_args:
				if not name in kw:
					return web.HTTPBadRequest('Missing argument:%s'%name)
		
		logging.info('called with args:%s'%str(kw))
		try:
			r=yield from self.__func(**kw)
			return r
		except APIError as e:
			return dict(error=e.error,data=e.data,message=e.message)
def add_static(app):
	path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'static')
	app.router.add_static('/static',path)
	logging.info('add static %s=>%s'%('/static',path))



def add_route(app,fn):
	method=getattr(fn,'__method__',None)
	path=getattr(fn,'__route__',None)
	if path is None or method is None:
		raise ValueError('@get or @post not defined in %s'%str(fn))
	if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
		fn=asyncio.coroutine(fn)
	logging.info('add route %s%s=>%s(%s)'%(method,path,fn.__name__,','.join(inspect.signature(fn).parameters.keys())))
	app.router.add_route(method,path,RequestHandler(app,fn))

def add_routes(app,module_name):
	
	n=module_name.rfind('.')
	if n==(-1):
		mod=__import__(module_name,globals(),locals())
	else:
		name=module_name[n+1:]
		mod=getattr(__import__(module_name[:n],globals(),locals(),[name]),name)
	for attr in dir(mod):
		if attr.startswith('_'):
			continue
		fn=getattr(mod,attr)
		if callable(fn):
			method=getattr(fn,'__method__',None)
			path=getattr(fn,'__route__',None)
			if method and path:
				try:
					add_route(app,fn)					
				except Exception as e:
					print(app,fn)
					
