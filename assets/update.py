'''
Well you're a curious one, aren't you?

This is the code I use to keep the repository up-to-date with
the main course website. There's a lot of file work and library
tools, so much of this won't make sense until you're done with 
the course. Even then, a lot of this code deals with HTML, so
you might have to do a quick web development course before
reading through this. 

It might be interesting to see how much you understand as the 
semester goes on, though. Everything here is documented for my 
sake, but you may come to understand my lingo as you get better 
at programming.

                        ｔｈｏｎｋ
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣶⣶⣤⣤⣤⣀⡀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⡿⠟⠛⠋⠉⠉⠉⠉⠉⠉⠙⠛⠻⢿⣶⣤⡀
        ⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⣄
        ⠀⠀⠀⠀⣠⣾⠋⣩⣶⡿⠿⠿⢿⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣷⣄
        ⠀⠀⠀⣴⡟⠁⠀⠋⠁⠀⠀⠀⢀⠀⠉⠀⠀⠀⠀⠀⠀⣤⣴⣶⡶⠶⠶⠶⠤⠀⠈⢻⣦
        ⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⢀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⢻⣧
        ⠀⢰⡿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⢿⡆
        ⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿
        ⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄
        ⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃
        ⠀⣿⣷⠀⠀⠀⣠⣄⡀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿
        ⠀⠸⣿⣇⠀⢸⠁⠈⢳⠀⠀⠀⠘⠛⠛⠛⠛⠛⠻⠿⠶⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠇
        ⠀⠀⢻⣿⣦⣾⠇⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟
        ⠀⠀⠀⠻⣿⡿⠀⠀⠘⢿⣶⣤⡤⠤⠤⠄⠒⠒⠈⠉⠉⣩⡄⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟
        ⠀⠀⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣾⠿⠋⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋
        ⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣧⠀⠀⠀⣀⣠⣤⣶⠿⠛⠁
        ⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⢀⣀⣰⣿⠻⠿⠿⠛⠛⠛⠉⠁
        ⠀⠀⠀⠀⠀⠀⠙⠻⠶⠶⠾⠿⠿⠟⠛⠁

GitHub: https://github.com/braedynl/CSE231-GITHUB
Author: Braedyn Lettinga
Dependencies: BeautifulSoup
'''

import json
import os
import zipfile
from datetime import datetime, timedelta
from math import floor
from typing import Union
from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve

from bs4 import BeautifulSoup


class CSE231GitHub(object):
    '''
    CSE231GitHub
    ============
    Locally updates the CSE231-GITHUB repository with the latest data from the
    main course website. 

    Public Methods
    --------------
    update_all()
        Updates all files and folders accounted for by the class. Equivalent to
        running all method functions at once. 
    
    update_syllabus()
        Updates /master/SYLLABUS.md from its template and course_info.json.
    
    update_readme()
        Updates /master/README.md from its template and course_info.json.
    
    update_lab_files()
        Updates all /Lab XX/README.md files from its template. 
    
    update_project_files()
        Updates all /Project XX/ files from the main course website, and the
        README.md files from its template. 
    
    update_schedule()
        Creates and/or modifies schedule.html and project_dates.json, two files
        that are used by the other method functions. This method is always ran
        at instantiation. 
    
    package()
        Copies all lab or project files to a corresponding *.zip file in
        /assets/packages/.

    Private Methods
    ---------------
    _walk_tree()
        Collects all possible paths within a subdirectory.

    _course_info_replace()
        Iterates through self.course_info to replace all markdown
        variables. 

    _create_bar_str()
        Creates progress bar string. 

    _get_td_deltas()
        Creates a mapping of HTML td tag iterations to timedeltas
        of the included days of the week.

    _expand_date()
        Expands out a datetime instance as a string in the form:
            "Weekday, Month Day[Ordinal Suffix] (m/d/y)"

    _get_ordinal_suffix()
        Calculates the ordinal suffix for a given number.

    Notes
    -----
    The option to disable automatic packaging is present to reduce commit
    deltas and runtime if necessary. Re-packaging project/lab folders may
    lead Git to think that the *.zip files changed even if they didn't. 

    All templates can be found in /assets/templates/. Markdown "variables"
    are signified by two colons like :this:. 
    '''

    def __init__(self):
        self.course_info = json.load(open('assets/course_info.json', 'r'))

        self.lab_info_temp = open('assets/templates/lab_info_temp.md', 'r').read()
        self.project_info_temp = open('assets/templates/project_info_temp.md', 'r').read()
        self.readme_temp = open('assets/templates/readme_temp.md', 'r').read()
        self.syllabus_temp = open('assets/templates/syllabus_temp.md', 'r').read()

        self.progressbar = {'width': 14, 'fill': '⬛', 'empty': '⬜'}

        self.update_schedule()

    def update_all(self, package:bool=True) -> None:
        '''
        Updates all files and folders accounted for by the class. Equivalent to
        running all method functions at once. 

        Parameters
        ----------
            package : Option to enable/disable automatic packaging. 
        '''

        print('Updating repository, this may take a few seconds...')
        print('---------------------------------------------------\n')

        self.update_project_files(package)
        self.update_lab_files(package)
        self.update_readme()
        self.update_syllabus()

        print('---------------------------------------------------')
        print('Repository updated.\n')

    def update_syllabus(self) -> None:
        '''
        Updates /master/SYLLABUS.md from its template and course_info.json.
        '''

        print('Updating master "SYLLABUS.md"...')

        syllabus_text = self._course_info_replace(self.syllabus_temp)

        syllabus = open('SYLLABUS.md', 'w+')
        print(syllabus_text, file=syllabus)
        syllabus.close()

        print('Done.\n')
    
    def update_readme(self) -> None:
        '''
        Updates /master/README.md from its template and course_info.json.
        '''

        print('Updating master "README.md"...')

        schedule_html = open('assets/schedule.html', 'r').read()

        today = datetime.now()

        sem_fday = datetime(*self.course_info['semester_first_day'])
        sem_lday = datetime(*self.course_info['semester_last_day'])

        N = sem_lday - sem_fday  # number of days in the semester
        n = sem_lday - today     # number of days from now until the end of the semester

        p = 1 - (n.days / N.days)  # percentage of completion

        bar_str = self._create_bar_str(p)

        if p < 0:  # makes all negative percents 0 (since I'm writing/testing this script before the semester has begun)
            p = 0 
        
        bar_html = '<div align="center"><b>Semester Progress ({:.0%})</b></div>\n<div align="center">{}</div>'.format(p, bar_str)
    
        readme_text = self._course_info_replace(self.readme_temp.replace(':schedule:', schedule_html).replace(':progressbar:', bar_html))

        readme = open('README.md', 'w+')
        print(readme_text, file=readme)
        readme.close()

        print('Done.\n')

    def update_lab_files(self, package:bool=True) -> None:
        '''
        Updates all /Lab XX/README.md files from its template.

        Parameters
        ----------
            package : Option to enable/disable automatic packaging.
        '''

        print('Updating lab files...')

        for folder_name in os.listdir():
            if 'lab' in folder_name.lower() and '.' not in folder_name:
                n = int(folder_name[-2:])

                if n == 0:  # lab 00 is updated manually by me
                    continue
                
                os.chdir(folder_name)

                readme_text = self.lab_info_temp.replace(':n:', str(n)).replace(':n02d:', '{:02d}'.format(n)).replace(':help_room_url:', self.course_info['help_room_url'])

                readme = open('README.md', 'w+')
                print(readme_text, file=readme)
                readme.close()

                os.chdir('..')
        
        if package:
            self.package('lab')
        else:
            print('Done.\n')
        
    def update_project_files(self, package:bool=True) -> None:
        '''
        Updates all /Project XX/ files from the main course website, and the
        README.md files from its template. 

        Parameters
        ----------
            package : Option to enable/disable automatic packaging.
        '''

        print('Updating project files...')

        project_dates = json.load(open('assets/project_dates.json', 'r'))
        url = 'https://www.cse.msu.edu/~cse231/Online/Projects/Project{:02d}/'

        for n in range(1, 13):  # project numbers (up to 12 to force HTTPError)
            complete_url = url.format(n)

            name_expanded = 'Project {:02d}'.format(n)
            name_short = 'proj{:02d}'.format(n)

            try:
                soup = BeautifulSoup(urlopen(complete_url), features='html.parser')
            except HTTPError:
                break
            
            subdir = '{}/'.format(name_expanded)
            if not os.path.exists(subdir):
                os.mkdir(subdir)
            os.chdir(subdir)

            file_names = []

            for link in soup.find_all('a'):
                href = link.get('href')
                
                if 'youtube' in href:
                    video = href
                    continue

                file_url = complete_url + href 
            
                if 'proj' in href.lower() and href.endswith('.py'):  # standardizes project file and PDF names 
                    save_as = name_short + '.py'
                elif 'proj' in href.lower() and href.endswith('.pdf'):
                    save_as = name_short + '.pdf'
                else:
                    save_as = href

                file_names.append(save_as)

                urlretrieve(file_url, save_as)

            if name_short + '.py' not in file_names:  # creates project file if none exists
                open(name_short + '.py', 'w+').close()
                file_names.append(name_short + '.py')

            readme_text = self.project_info_temp.replace(':video:', video).replace(':n:', str(n)).replace(':n02d:', '{:02d}'.format(n)).replace(':due:', project_dates[name_short]).replace(':help_room_url:', self.course_info['help_room_url'])
            
            readme = open('README.md', 'w+')
            print(readme_text, file=readme)
            readme.close()

            os.chdir('..')
        
        if package:
            self.package('proj')
        else:
            print('Done.\n')

    def update_schedule(self) -> None:
        '''
        Creates and/or modifies schedule.html and project_dates.json, two files
        that are used by the other method functions. This method is always ran
        at instantiation. 

        "Ew Braedyn what the hell is this? Why are you not using CSS!?"

        At the time of writing, you cannot run CSS scripts in GitHub repos.
        If I were able to run CSS on here, most of this function would be
        unnecessary. Thus, we have Python-generated HTML 🤷🏼‍♀️

        Was pretty fun to make ngl.
        '''

        print('Updating "schedule.html" and "project_dates.json"')
        print('These files must be updated before any method functions can run, please wait...')

        soup = BeautifulSoup(urlopen(self.course_info['schedule_url']), features='html.parser')

        td_deltas = self._get_td_deltas(soup)

        schedule_fp = open('assets/schedule.html', 'w+')
        project_dates_fp = open('assets/project_dates.json', 'w+')

        project_dates = {}

        print('<table>', file=schedule_fp)
        print(soup.find('thead'), file=schedule_fp)
        print('<tbody>', file=schedule_fp)

        for tr in soup.find('tbody').find_all('tr'):

            print('<tr>', file=schedule_fp)

            for i, td in enumerate(tr.find_all('td')):

                if i not in td_deltas:  # handles the last row (has one more column for some reason)
                    break

                td = td.text.strip()

                if i == 0:  # first column is the week number and initial date
                    colon_index = td.find(':')
                    week = int(td[:colon_index])
                    date = td[colon_index + 2:]

                    slash_index = date.find('/')
                    month = int(date[:slash_index])
                    day = int(date[slash_index + 1:])

                    print('<td align="center">{:02d}: {:02d}/{:02d}</td>'.format(week, month, day), file=schedule_fp)

                    init_datet = datetime(int(self.course_info['year']), month, day)
                
                else:
                    full_date = self._expand_date(init_datet + timedelta(td_deltas[i]))
                    
                    if td == '':
                        print('<td align="center"></td>', file=schedule_fp)
                    elif 'read' in td.lower():
                        print('<td><a title="On: {}" href="{}">{}</a></td>'.format(full_date, self.course_info['week_urls'][str(week)], td), file=schedule_fp)
                    elif 'exercise' in td.lower():
                        print('<td align="center"><a title="Due: {}" href="https://class.mimir.io">{}</a></td>'.format(full_date, td), file=schedule_fp)
                    elif 'exam' in td.lower():
                        print('<td align="center"><a title="On: {}" href="#exam-information">{}</a></td>'.format(full_date, td), file=schedule_fp)

                    elif 'lab' in td.lower():
                        lab_n = int(td[td.find(' '):])
                        if lab_n == 0:  # accounts for lab 00 not having a pre-lab
                            print('<td align="center"><a title="Due: {}" href="Lab%20{n:02d}">Lab {n:02d}</a></td>'.format(full_date, n=lab_n), file=schedule_fp)
                        else:
                            print('<td align="center"><a title="Due: {full_date}" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab</a> / <a title="Due: {full_date}" href="Lab%20{n:02d}">Lab {n:02d}</a></td>'.format(full_date=full_date, n=lab_n), file=schedule_fp)

                    elif 'proj' in td.lower():
                        proj_n = int(td[-2:])
                        project_dates['proj{:02d}'.format(proj_n)] = full_date
                        print('<td align="center"><a title="Due: {}" href="Project%20{n:02d}">Project {n:02d}</a></td>'.format(full_date, n=proj_n), file=schedule_fp)

                    else:
                        print('<td align="center"><div title="On: {}">{}</div></td>'.format(full_date, td.title()), file=schedule_fp)

            print('</tr>', file=schedule_fp)
        print('</tbody>', file=schedule_fp)
        print('</table>', file=schedule_fp)

        json.dump(project_dates, project_dates_fp, indent=4)

        schedule_fp.close()
        project_dates_fp.close()

        print('Done. Method functions are now accessible.\n')

    def package(self, folder_type:Union['proj', 'lab']) -> None:
        '''
        Copies all lab or project files to a corresponding *.zip file in
        /assets/packages/. 

        Parameters
        ----------
            folder_type : Option to package project or lab folders.
        '''

        if folder_type not in ['proj', 'lab']:
            raise ValueError('folder_type argument not "proj" or "lab"')

        print('Packaging all {} folders...'.format(folder_type))

        for folder_name in os.listdir():
            if folder_type in folder_name.lower() and '.' not in folder_name:

                zip_file = zipfile.ZipFile('assets/packages/{}{}_content.zip'.format(folder_type, folder_name[-2:]), 'w')

                paths = self._walk_tree(folder_name)  # inefficient, but eh -- it works and makes sense

                for path in paths:
                    save_path = path.replace('{}/'.format(folder_name), '')
                    zip_file.write(path, save_path, compress_type=zipfile.ZIP_DEFLATED)
                
                zip_file.close()

        print('Done.\n')

    def _walk_tree(self, path:str) -> list:
        '''
        Collects all possible paths within a subdirectory.

        Parameters
        ----------
            path : Subdirectory path. 
        
        Returns
        -------
            list : A list of strings of all possible paths.
        '''

        file_paths = []
        for root, _, files in os.walk(path):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    def _course_info_replace(self, text:str) -> str:
        '''
        Iterates through self.course_info to replace all markdown
        variables. 

        Parameters
        ----------
            text : Markdown file's text. 
        
        Returns
        -------
            str : The markdown file's text with proper substitutions. 
        '''

        for key, value in self.course_info.items():
            try:
                text = text.replace(':{}:'.format(key), value)
            except:
                continue
        return text

    def _create_bar_str(self, p:float) -> str:
        '''
        Creates progress bar string. 

        Parameters
        ----------
            p : Bar fill percent. 
        
        Returns
        -------
            str : The corresponding progress bar to `p`. 
        '''

        if p < 0:
            return self.progressbar['empty'] * self.progressbar['width']
        
        fill_w = floor(p * self.progressbar['width'])
        return (fill_w * self.progressbar['fill']) + (self.progressbar['empty'] * (self.progressbar['width'] - fill_w))

    def _get_td_deltas(self, soup:BeautifulSoup) -> dict:
        '''
        Creates a mapping of HTML td tag iterations to timedeltas
        of the included days of the week.

        Parameters
        ----------
            soup : BeautifulSoup instance with URL opened.
        
        Returns
        -------
            dict : Mapping of td tags to timedeltas. 
        
        Notes
        -----
        This function works under two, possibly hazy, assumptions:
        1: Enbody will always use shorthand day expressions (e.g. "Sun", "Mon", etc.)
        2: Enbody will always keep the first column as the week number and date

        If he suddenly changes his formatting, it's possible that all of this will
        fall apart. 

        Return structure:
        {td_iteration: timedelta, ...}

        Key 0 will always have None as its value (since the first column is the
        week number and date).
        '''

        week_deltas = {'Sun': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6}

        td_deltas = {}

        for i, th in enumerate(soup.find('thead').find_all('th')):
            if i == 0:
                td_deltas[i] = None 
            else:
                td_deltas[i] = week_deltas[th.text]
        
        return td_deltas

    def _expand_date(self, datet:'datetime') -> str:
        '''
        Expands out a datetime instance as a string in the form:
            "Weekday, Month Day[Ordinal Suffix] (m/d/y)"

        Parameters
        ----------
            datet : A datetime instance.

        Returns
        -------
            str : Expanded datetime string. 
        '''

        date_str_exp = datet.strftime('%A, %B %d')
        date_str_num = datet.strftime('(%m/%d/%Y)') 

        ordinal_suffix = self._get_ordinal_suffix(int(date_str_exp[-2:]))

        full_date = date_str_exp + ordinal_suffix + ' ' + date_str_num

        return full_date.replace('(0', '(').replace('/0', '/').replace(' 0', ' ')  # replaces padding zeroes


    def _get_ordinal_suffix(self, num:int) -> str:
        '''
        Calculates the ordinal suffix for a given number. 

        Parameters
        ----------
            num : Number for suffix determination. 
        
        Returns
        -------
            str : Corresponding ordinal suffix. 
        '''

        return {1: "st", 2: "nd", 3: "rd"}.get(num % 10 * (num % 100 not in [11, 12, 13]), "th")


if __name__ == "__main__":
    github = CSE231GitHub()

    github.update_all(False)
