####import requests
#####from requests.auth import HTTPBasicAuth

###r = requests.get('https://api.github.com/events')
####r2 = requests.post('https://httpbin.org/post', data={'key': 'value'})

##payload = {'key1': 'value1', 'key2': 'value2'}
###r = requests.get('https://httpbin.org/get', params=payload)

##print(r.url)
###  можете передать список элементов в качестве значения:
##payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

##r = requests.get('https://httpbin.org/get', params=payload)
###print(r.url)


###r = requests.get('https://api.github.com/events')
###r.encoding = 'utf-8'
###print(r.text)



###basic = HTTPBasicAuth('user', 'pass')
###requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
####requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))



import numpy as np
###a = np.array([1,2,3,4])
##print(a.dtype)

##print(a[2])

###a[1] = '1234'

##print(a)

##print(a.ndim)
##print(a.size)

##np.complex64(10)
##np.complex64(10+0j)
##np.int16(10.5)
##np.int16(10)


##arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
##print(np.sort(arr))

##a = np.array([1, 2, 3, 4])
##b = np.array([5, 6, 7, 8])
##print(np.concatenate((a,b)))

a = np.arange(6)
print(a)
b = a.reshape(3, 2)
print(b)
np.reshape(a, shape=(1, 6), order='C')