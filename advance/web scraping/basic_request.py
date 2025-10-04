import requests


# response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(response))
# print(len(response.text))
# print(response.text[:210])
# print(response.status_code)
# print(requests.codes.ok)
# print(response.status_code == requests.codes.ok)



# response = requests.get('https://automatetheboringstuff.com/files/rjt.txt')
# try:
#     response.raise_for_status()
# except Exception as e:
#     print(f'error= {e}')



response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    response.raise_for_status()
except Exception as e:
    print(f'error= {e}')

with open('RomeoAndJuliet.txt', 'wb') as fp:
    for chunks in response.iter_content(100000):
        fp.write(chunks)
