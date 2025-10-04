from bs4 import BeautifulSoup
import os 
import requests
import time

url = 'https://xkcd.com'  # Starting URL
os.makedirs('xkcd', exist_ok= True)
num_downloads = 0
MAX_DOWNLOADS = 5

while not url.endswith('#') and num_downloads < MAX_DOWNLOADS:
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.text, 'html.parser')
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('Could not find comic image.')
    else:
        comic_URL = f'https:{comic_elem[0].get('src')}'
        print(f'Downloading image {comic_URL}...')
        res = requests.get(comic_URL)
        res.raise_for_status()
        
    image_file = open(os.path.join('xkcd', os.path.basename(comic_URL)), 'wb')
    for chunks in res.iter_content(100000):
        image_file.write(chunks)
    image_file.close()
    
    prev_link = soup.select('a[rel= "prev"]')[0]
    url = f'https://xkcd.com{prev_link.get('href')}'
    num_downloads += 1
    time.sleep(1)
    
print('Done.')
    
    
