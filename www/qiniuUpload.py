# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

bucket = 'vake'
#accessKey = vA5IXFjRpguFwQO4_eEiunvONORSek1hN4iN7NZS
#secretKey = qlE6jfP3dmrlOUw-fBYmF0jBceUe-HIfevqqw3Ba
path_to_watch ='/Users/liu/Downloads/image/'


#需要填写你的 Access Key 和 Secret Key
access_key = 'vA5IXFjRpguFwQO4_eEiunvONORSek1hN4iN7NZS'
secret_key = 'qlE6jfP3dmrlOUw-fBYmF0jBceUe-HIfevqqw3Ba'

#构建鉴权对象
q = Auth(access_key, secret_key)
print(q)
#要上传的空间
bucket_name = bucket

#上传到七牛后保存的文件名
key = 'my-python-logo.png';

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
localfile = path_to_watch+'屏幕快照 2017-05-06 21.35.06.PNG'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
