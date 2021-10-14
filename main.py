import httpx

r = httpx.get('https://www.example.org/', params={'key1': 'value1'})
r.status_code
r.headers['content-type']

r.url
print(r.url)

r = httpx.post('https://httpbin.org/post', data={'key': 'value'})
r = httpx.put('https://httpbin.org/put', data={'key': 'value'})
r = httpx.delete('https://httpbin.org/delete')
r = httpx.head('https://httpbin.org/get')
r = httpx.options('https://httpbin.org/get')

r = httpx.get('https://api.github.com/events').json()

print(r)