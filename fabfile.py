import os,re
from datetime import datetime
from fabric.api import *
env.user = 'root'
# sudo用户为root:
env.sudo_user = 'root'
# 服务器地址，可以有多个，依次部署:
env.hosts = ['120.24.190.4']
env.password='rootftp'

# 服务器MySQL用户名和口令:
db_user = 'root'
db_password = '123456'

_TAR_FILE = 'dist-awesome.tar.gz'

_REMOTE_TMP_TAR='/tmp/%s'%_TAR_FILE	
_REMOTE_BASE_DIR='/srv/awesome'


def build():
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py','*.sql']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.join(os.path.abspath('.'), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))


def deploy():
	newdir='www-%s'%datetime.now().strftime('%y-%m-%d_%H.%M.%S')
	try:
		run('rm -f%s'%_REMOTE_TMP_TAR)
	except Exception as e:
		print(e)
	finally:
		put('dist/%s'%_TAR_FILE,_REMOTE_TMP_TAR)
		with cd(_REMOTE_BASE_DIR):
			sudo('mkdir %s'%newdir)
		with cd('%s/%s'%(_REMOTE_BASE_DIR,newdir)):
			sudo('tar -xzvf %s'%_REMOTE_TMP_TAR)
		with cd(_REMOTE_BASE_DIR):
			sudo('rm -f www')
			sudo('ln -s %s www'%newdir)
			sudo('chown www-data:www-data www')
			sudo('chown -R www-data:www-data %s'%newdir)
		with settings(warn_only=True):
			sudo('source /usr/bin/env27/bin/activate')

			sudo('supervisorctl stop awesome')
			sudo('supervisorctl start awesome')
			sudo('deactivate')
			sudo('/etc/init.d/nginx reload')
			find='lsof -i tcp | grep LISTEN'
def runblog():
	sudo('python3 /srv/awesome/www/app.py')
	sudo('sudo service nginx restart ')

