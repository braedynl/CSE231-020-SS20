import os
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
from bs4 import BeautifulSoup

extensions = ['.py', '.txt', '.csv', '.pdf']
url = 'https://www.cse.msu.edu/~cse231/Online/Projects/Project{:02d}/'

for n in range(1, 13):
    print("Gathering project {:02d} files...\n".format(n))
    try:
        soup = BeautifulSoup(urlopen(url.format(n)).read(), features='html.parser')
    except HTTPError:
        print("Project {:02d} subdomain not found. Halting execution...".format(n))
        break

    sub_dir = 'Project {:02d}/'.format(n)
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
    os.chdir(sub_dir)

    files = []

    for link in soup.find_all('a'):
        href = link.get('href')
        file_url = url.format(n) + href

        if not any(href.endswith(ex) for ex in extensions):
            if 'youtube' in href:
                print("YouTube link encountered: {}\n".format(file_url))
                yt_link = href
            else:
                print("Unrecognized file extension/href encountered: {}\n".format(file_url))
            continue

        elif 'proj' in href.lower() and href.endswith('.py'):
            save_as = 'proj{:02d}.py'.format(n)
        elif 'proj' in href.lower() and href.endswith('.pdf'):
            save_as = 'proj{:02d}.pdf'.format(n)
        else:
            save_as = href
        
        files.append(save_as)
        
        print("Downloading file from: {} ...".format(file_url))
        urlretrieve(file_url, save_as)
        print("Done.\n")

    if 'proj{:02d}.py'.format(n) not in files:
        print("Project {:02d} file not found. Creating an empty one...".format(n))
        open('proj{:02d}.py'.format(n), 'w+').close()
        print("Done.\n")
    
    os.chdir('..')