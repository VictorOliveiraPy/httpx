import httpx

with httpx.Client() as client:
    resp = client.get('https://example.com')

with httpx.Client() as client:
    headers = {'X-Custom': 'value'}
    resp = client.get('https://example.com', headers=headers)

    resp.request.headers['X-CUSTOM']

    print(resp)
