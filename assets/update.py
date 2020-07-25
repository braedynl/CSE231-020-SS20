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


DAY_DELTAS = {'Sun': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6}

class CSE231GitHub(object):

    def __init__(self):
        self.course_info = json.load(open('assets/course_info.json', 'r'))

        self.lab_info_temp = open('assets/templates/lab_info_temp.md', 'r').read()
        self.project_info_temp = open('assets/templates/project_info_temp.md', 'r').read()
        self.readme_temp = open('assets/templates/readme_temp.md', 'r').read()
        self.syllabus_temp = open('assets/templates/syllabus_temp.md', 'r').read()

        self.progressbar = {'width': 14, 'fill': '⬛', 'empty': '⬜'}

        self.update_schedules(
            prelab_day=self.course_info['prelab_day'],
            lab_day=self.course_info['lab_day']
            )

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

        semester_start = datetime(*self.course_info['semester_start'])
        semester_end = datetime(*self.course_info['semester_end'])

        N = semester_end - semester_start  # number of days in the semester
        n = semester_end - today     # number of days from now until the end of the semester

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

    def update_schedules(self, prelab_day:str=None, lab_day:str=None) -> None:
        '''
        Creates and/or modifies schedule.html and project_dates.json, two files
        that are used by the other method functions. This method is always ran
        at instantiation. 

        Parameters
        ----------
            prelab_day : A custom pre-lab day, title-case abbreviated format.
            lab_day : A custom lab day, title-case abbreviated format. 
        
        Notes
        -----
        If prelab_day is None, pre-labs will be assigned on the day of the lab.
        If lab_day is None, labs will be assigned to the day followed by the
        due dates page of the website. 

        This function shifts the pre-labs/labs on a week-by-week basis. So if
        Lab 01 is due on week 1, and lab_day="Thu", Lab 01 will be shifted to be
        due on Thursday of week 1. 
        '''

        print('Updating "schedule.html" and "project_dates.json"...')

        soup = BeautifulSoup(urlopen(self.course_info['schedule_url']), features='html.parser')
        td_deltas = self._get_td_deltas(soup.find('thead').find_all('th'))
        calendar = self._create_calendar()

        project_dates = {}

        for week_n, tr in enumerate(soup.find('tbody').find_all('tr')):

            initial_date = datetime(*calendar[week_n]['Sun']['attributes'])
            has_lab = False  # flag to determine if the week has a lab or not

            for i, td in enumerate(tr.find_all('td')):

                if i not in td_deltas:  # handles last row (has one extra column for some reason)
                    break 
                if i == 0:  # 0th column is always the week number
                    continue

                td = td.text.strip()

                if td == '':  # if calendar cell has no assignment/text
                    continue
                
                # calculates the date adjusted by the amount of days from the initial_date (Sunday of each week)
                shifted_date = initial_date + timedelta(td_deltas[i])
                day = shifted_date.strftime('%a')  # Union['Sun', 'Mon', 'Tue', ...]
                pretty_date = self._get_pretty_date(shifted_date)   # prettier date format for hovertext

                if 'read' in td.lower():
                    calendar[week_n][day]['html'] = '<a title="On: {}" href="{}">{}</a>'.format(pretty_date, self.course_info['week_urls'][str(week_n)], td)
                elif 'exercise' in td.lower():
                    calendar[week_n][day]['html'] = '<a title="Due: {}" href="https://class.mimir.io">{}</a>'.format(pretty_date, td)
                elif 'exam' in td.lower():
                    calendar[week_n][day]['html'] = '<a title="On: {}" href="#exam-information">{}</a>'.format(pretty_date, td)
                elif 'proj' in td.lower():
                    proj_n = int(td[-2:])
                    calendar[week_n][day]['html'] = '<a title="Due: {}" href="Project%20{n:02d}">Project {n:02d}</a>'.format(pretty_date, n=proj_n)
                    project_dates['proj{:02d}'.format(proj_n)] = pretty_date
                
                elif 'lab' in td.lower():
                    has_lab = True
                    lab_n = int(td[td.find(' '):])

                    if lab_n == 0:
                        calendar[week_n][day]['html'] = '<a title="Due: {}" href="Lab%2000">Lab 00</a>'.format(pretty_date)

                    if lab_day is None and prelab_day is None:
                        lab_day = prelab_day = day 
                    elif lab_day is None and prelab_day is not None:
                        lab_day = day 
                    elif lab_day is not None and prelab_day is None:
                        prelab_day = lab_day

                else:
                    calendar[week_n][day]['html'] = '<div title="On: {}">{}</div>'.format(pretty_date, td.title())


            if lab_n == 0 or has_lab == False:  # skips pre-lab/lab insertion if lab 0 or if week has no lab
                continue

            lab_html = '<a title="Due: {}" href="Lab%20{n:02d}">Lab {n:02d}</a>'.format(calendar[week_n][lab_day]['date'], n=lab_n)
            prelab_html = '<a title="Due: {}" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab {n:02d}</a>'.format(calendar[week_n][prelab_day]['date'], n=lab_n)
            
            if calendar[week_n][lab_day]['html'] != '':
                calendar[week_n][lab_day]['html'] = lab_html + ' / ' + calendar[week_n][lab_day]['html']
            else:
                calendar[week_n][lab_day]['html'] = lab_html
            
            if calendar[week_n][prelab_day]['html'] != '':
                calendar[week_n][prelab_day]['html'] = prelab_html + ' / ' + calendar[week_n][prelab_day]['html']
            else:
                calendar[week_n][prelab_day]['html'] = prelab_html
            
            has_lab = False

        project_dates_fp = open('assets/project_dates.json', 'w+')
        json.dump(project_dates, project_dates_fp, indent=4)
        project_dates_fp.close()

        self._process_html_calendar(calendar)

        print("Done.\n")

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

    def _process_html_calendar(self, calendar:dict) -> None:
        '''
        Parses the calendar dictionary into an HTML file used
        by master README.md. 

        Parameters
        ----------
            calendar : The calendar dictionary.
        '''

        fp_out = open('assets/schedule.html', 'w+')

        headers = {'Week', }
        for week_dict in calendar.values():
            for day, day_dict in week_dict.items():
                if day_dict['html'] != '':
                    headers.add(day)
        
        headers = sorted(
                headers, 
                key=lambda head: {'Week': 0, 'Sun': 1, 'Mon': 2, 'Tue': 3, 'Wed': 4, 'Thu': 5, 'Fri': 6, 'Sat': 7}[head]
                )

        print('<table>', file=fp_out)

        print('<thead>', file=fp_out)
        print('<tr>', file=fp_out)
        for head in headers:
            print('<th align="center">{}</th>'.format(head), file=fp_out)
        print('</tr>', file=fp_out)
        print('</thead>', file=fp_out)

        print('<tbody>', file=fp_out)
        for week_n, week_dict in calendar.items():
            print('<tr>', file=fp_out)
            print('<td align="center">{:02d}: {:02d}/{:02d}</td>'.format(
                week_n, 
                week_dict['Sun']['attributes'][1],
                week_dict['Sun']['attributes'][2]
                ),
                file=fp_out
            )
            for day, day_dict in week_dict.items():
                if day in headers:
                    if 'read' in day_dict['html'].lower():
                        print('<td>{}</td>'.format(day_dict['html']), file=fp_out)
                    else:
                        print('<td align="center">{}</td>'.format(day_dict['html']), file=fp_out)
            print('</tr>', file=fp_out)
        print('</tbody>', file=fp_out)

        print('</table>', file=fp_out)

        fp_out.close()

    def _get_td_deltas(self, th_list:list) -> dict:
        '''
        Creates a mapping of HTML td tag iterations to timedeltas
        of the included days of the week.

        Parameters
        ----------
            th_list : List of table header tags. 
        
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

        td_deltas = {}

        for i, th in enumerate(th_list):
            if i == 0:
                td_deltas[i] = None 
            else:
                td_deltas[i] = DAY_DELTAS[th.text]
        
        return td_deltas
    
    def _create_calendar(self) -> dict:
        '''
        Creates a "skeleton calendar" with dates and empty
        HTML attributes. The structure is as follows:

        calendar = {
            0 : {
                "Mon" : {
                    "date" : str,
                    "attributes" : list,  # [year (int), month (int), day (int)]
                    "html" : str
                },
                ...
            },
            ...
        } 
        '''

        start_date = datetime(*self.course_info['schedule_start'])
        end_date = datetime(*self.course_info['schedule_end'])

        calendar = {}

        week_n = 0
        dt = 0

        while (start_date + timedelta(dt)) < end_date:
            calendar[week_n] = {}
            for day in DAY_DELTAS.keys():
                datet = start_date + timedelta(dt)

                calendar[week_n][day] = {
                    'date': self._get_pretty_date(datet), 
                    'attributes': [datet.year, datet.month, datet.day],
                    'html': '',
                    }

                dt += 1
            week_n += 1
        
        return calendar

    def _get_pretty_date(self, datet:datetime) -> str:
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

        full_date = (date_str_exp + ordinal_suffix + ' ' + date_str_num).replace('(0', '(').replace('/0', '/').replace(' 0', ' ')  # replaces padding zeroes

        return full_date

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
