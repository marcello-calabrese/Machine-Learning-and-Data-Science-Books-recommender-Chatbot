
from zipfile import ZipFile



# Extract all the contents of zip file in current directory

def extract_all(zip_file):
    with ZipFile(zip_file, 'r') as zip:
        zip.printdir()
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')
        
# Execute the script

extract_all('archive.zip')

