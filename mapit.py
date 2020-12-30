import webbrowser, sys, pyperclip

sys.argv # [ 'mapit.py', '870', 'Valencis', 'St.' ]

# Check if command line arguments were passed
if len(sys.argv) > 1: # if user placed args, they want to open from here
    # [ 'mapit.py', '870', 'Valencis', 'St.' ] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:]) # slices args into single string
else: # else, they want to paste it from their clipboard
    address = pyperclip.paste()

# paste into google maps
# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)