import httpx

#
# url = 'https://httpbin.org/headers'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = httpx.get(url, headers=headers)
#
# print(r)
#
# # Envio de dados codificados de formulário
#
# data = {'key1': 'value1', 'key2': 'value2'}
# r = httpx.post("https://httpbin.org/post", data=data)
# print(r.text)
#
# # Envio de uploads de arquivos multipartes
#
# #files = {'upload-file': open('report.xls', 'rb')}
# r = httpx.post("https://httpbin.org/post")
# print(r.text)
#
# # Se você precisar incluir campos de dados que não sejam de arquivo no formulário multipartes, use o data=...parâmetro:
# data = {'message': 'Hello, world!'}
# files = {'file': open('report.xls', 'rb')}
# r = httpx.post("https://httpbin.org/post", data=data, files=files)
# #print(r.text)

# Envio de dados codificados em JSON

data = {'integer': 123, 'boolean': True, 'list': ['a', 'b', 'c']}
r = httpx.post("https://httpbin.org/post", json=data)
r.headers.get('content-type')
#
r.raise_for_status()
print(r)

# Respostas de streaming
# conteúdo binário da resposta ...
with httpx.stream("GET", "https://www.example.com") as r:
    for data in r.iter_bytes():
        print(data)

# Ou o texto da resposta ...

with httpx.stream("GET", "https://www.example.com") as r:
    for text in r.iter_text():
        print(text)

# Ou transmita o texto, linha por linha ...

with httpx.stream("GET", "https://www.example.com") as r:
    for line in r.iter_lines():
        # print(line)
        pass

with httpx.stream("GET", "https://www.example.com") as r:
    for chunk in r.iter_raw():
        print(chunk)

# COOKIES

r = httpx.get('https://httpbin.org/cookies/set?chocolate=chip')
r.cookies['chocolate']

print(r.cookies['chocolate'])