import configs_default


class Dict(dict):
	def __init__(self,names=(),values=(),**kw):
		super(Dict,self).__init__(**kw)
		for k,v in zip(names,values):
			self[k]=v

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r'Dict has no Attribute%s'%key)
	
	def __setattr__(self,key,value):
		self[key]=value


def merge(default,override):
	r={}
	for k,v in default.items():
		if k in override:
			if isinstance(v,dict):
				r[k]=merge(v,override[k])# digui diaoyong
			else:
				r[k]=override[k]
		else:
			r[k]=v
	return r

def toDict(d):
	D=Dict()
	for k,v in d.items():
		D[k]=toDict(v) if isinstance(v,dict) else v
	return D

configs = configs_default.configs
try:
	import configs_override
	configs=merge(configs,configs_override.configs)
except ImportError:
	pass
configs = toDict(configs)
