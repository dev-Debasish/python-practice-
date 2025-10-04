import pyperclip, sys, webbrowser

def main():
    # step 1: check if the address is provided in the commandline
    if len(sys.argv) > 1:
        # Get the address from the command line argument
        address = ' '.join(sys.argv[1:])
    else:
        # step 2: Otherwise, get the address from the clipboard
        address = pyperclip.paste()
    
    # step 3: create OpenStreetMap URl with the address
    map_url = f'https://www.openstreetmap.org/search?query={address}'
    
    # step 4: Open the web browser to the map
    webbrowser.open(map_url)
    
    
if __name__ == "__main__":
    main()