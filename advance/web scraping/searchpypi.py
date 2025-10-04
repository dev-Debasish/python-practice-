import sys
import requests
import webbrowser
from bs4 import BeautifulSoup

# Step 1: Get the search term from command-line arguments
print('Searching...')
search_term = ' '.join(sys.argv[1:])

if not search_term:
    print("Please enter a search keyword.")
    sys.exit()

# Step 2: Fetch the search results from PyPI
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(f'https://pypi.org/search/?q={search_term}', headers=headers)
# res = requests.get(f'https://pypi.org/search/?q={search_term}')
res.raise_for_status()

# Step 3: Parse the results using BeautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

# Step 4: Find all result link tags
results = soup.select('a.package-snippet')  # Valid as of mid-2025

if not results:
    print("No results found. Try a different keyword.")
    sys.exit()

# Step 5: Open the top 5 results in browser
num_open = min(5, len(results))
for i in range(num_open):
    url = 'https://pypi.org' + results[i].get('href')
    webbrowser.open(url)

print(f"Opened top {num_open} results for '{search_term}' in your browser.")
