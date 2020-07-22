import json
import os
from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

def main():

    due_dates = json.load(open('assets/project_dates.json'))  # must be local
    url = 'https://www.cse.msu.edu/~cse231/Online/Projects/Project{:02d}/'

    for n in range(1, 13):  # project numbers
        try:
            soup = BeautifulSoup(urlopen(url.format(n)).read(), features='html.parser')
        except HTTPError:
            break  # breaks if page doesn't exist yet

        sub_dir = 'Project {:02d}/'.format(n)
        if not os.path.exists(sub_dir):
            os.mkdir(sub_dir)
        os.chdir(sub_dir)

        files = []  # list of all file names found in the table (type:str, extensions included)

        for link in soup.find_all('a'):
            href = link.get('href')
            file_url = url.format(n) + href

            if not any(href.endswith(ex) for ex in ['.py', '.txt', '.csv', '.pdf']):
                if 'youtube' in href:
                    video_link = href
                continue
            
            # the following conditions are to ensure standardization of the project file names
            # (sometimes Enbody names them differently)
            elif 'proj' in href.lower() and href.endswith('.py'):
                save_as = 'proj{:02d}.py'.format(n)
            elif 'proj' in href.lower() and href.endswith('.pdf'):
                save_as = 'proj{:02d}.pdf'.format(n)
            else:
                save_as = href
            
            files.append(save_as)
            
            urlretrieve(file_url, save_as)
        
        if 'proj{:02d}.py'.format(n) not in files:  # creates an empty project file if none is present in the subdirectory
            open('proj{:02d}.py'.format(n), 'w+').close()

        readme_temp = open('../assets/templates/project_info_temp.md', 'r').read()
        readme_temp = readme_temp.replace(':video_link:', video_link).replace(':n:', str(n)).replace(':due:', due_dates['Project {:02d}'.format(n)])

        print(readme_temp, file=open('README.md', 'w+'), end='')

        os.chdir('..')

if __name__ == "__main__":
    main()
