'''
Well you're a curious one, aren't you?

This is the code I use to keep the repository up-to-date with
the main course website. There's a lot of file work and library
tools, so much of this probably won't make sense until you're 
done with the course.

Also, as a forewarning, this code was bodged together in a few
afternoons. I'm the only one that uses it, so I just keep it
unkempt. Even I don't understand some of the things I wrote
here, looking back at this months later.

Have fun! :)

GitHub: https://github.com/braedynl/CSE231-GITHUB
Author: Braedyn Lettinga
Dependencies: BeautifulSoup, matplotlib, seaborn, numpy, pandas, xlrd
'''

import json
import os
import re
import zipfile
from datetime import datetime, timedelta
from math import floor
from typing import Union
from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve

import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib.dates import DateFormatter, drange
from pytz import timezone

import seaborn; seaborn.set()

HEADING_ORDER = {'Week': 0, 'Sun': 1, 'Mon': 2, 'Tue': 3, 'Wed': 4, 'Thu': 5, 'Fri': 6, 'Sat': 7}
DAY_DELTAS = {'Sun': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6}
PLOT_COUNTIES = ['Wayne', 'Kent', 'Washtenaw', 'Ingham', 'Macomb']

class CSE231GitHub(object):

    def __init__(self):
        self.course_info = json.load(open('assets/course_info.json', 'r'))
        self.lab_info_temp = open('assets/templates/lab_info_temp.md', 'r').read()
        self.project_info_temp = open('assets/templates/project_info_temp.md', 'r').read()
        self.readme_temp = open('assets/templates/readme_temp.md', 'r').read()
        self.syllabus_temp = open('assets/templates/syllabus_temp.md', 'r').read()
        self.progressbar = {'width': 14, 'fill': '⬛', 'empty': '⬜'}

        self.update_schedules(self.course_info['prelab_day'], self.course_info['lab_day'])

    def update_all(self, package:bool=True) -> None:
        self.update_project_files(package)
        self.update_lab_files(package)
        self.update_readme()
        self.update_syllabus()

    def update_syllabus(self) -> None:
        syllabus_text = self.__course_info_replace(self.syllabus_temp)
        syllabus = open('SYLLABUS.md', 'w+')
        print(syllabus_text, file=syllabus)
        syllabus.close()
    
    def update_readme(self) -> None:
        # self.__update_plot()

        schedule_html = open('assets/schedule.html', 'r').read()

        tz = timezone('US/Eastern')
        today = datetime.now(tz=tz)
        refresh = today.strftime('%m/%d/%Y %I:%M %p EST')
        semester_start = datetime(*self.course_info['semester_start'], tzinfo=tz)
        semester_end = datetime(*self.course_info['semester_end'], tzinfo=tz)

        N = semester_end - semester_start  # number of days in the semester
        n = semester_end - today     # number of days from now until the end of the semester

        p = 1 - (n.days / N.days)  # percentage of completion
        if p < 0: 
            p = 0
        elif p > 1:
            p = 1

        bar_str = self.__create_bar_str(p)

        bar_html = '<div align="center"><b>Semester Progress ({:.0%})</b></div>\n<div align="center">{}</div>'.format(p, bar_str)

        soup = BeautifulSoup(urlopen('https://www.michigan.gov/Coronavirus'), features='html.parser')

        stat_container = soup.find('section', attrs={'class':'stat-container'}).find_all('p')
        as_of = soup.find('p', text=re.compile(r'\d+/\d+/\d+')).text

        covid_data = '- **Total Confirmed Cases:** {}\n'.format(stat_container[1].text.replace('*', ''))
        covid_data += '- **Total COVID-19 Deaths:** {}\n'.format(stat_container[3].text.replace('*', ''))
        covid_data += '- **New Confirmed Cases:** {}\n'.format(stat_container[5].text.replace('*', ''))
        covid_data += '- **New COVID-19 Deaths:** {}\n\n'.format(stat_container[7].text.replace('*', ''))
        covid_data += 'As of: {}'.format(as_of)
    
        readme_text = self.__course_info_replace(
            self.readme_temp.replace(':schedule:', schedule_html).replace(':progressbar:', bar_html)\
                            .replace(':refresh:', refresh).replace(':covid_data:', covid_data)
            )

        readme = open('README.md', 'w+', encoding='utf8')
        print(readme_text, file=readme)
        readme.close()

    def update_lab_files(self, package:bool=True) -> None:
        lab_dates = json.load(open('assets/lab_dates.json', 'r'))

        for folder_name in os.listdir():
            if 'lab' in folder_name.lower() and '.' not in folder_name:
                n = int(folder_name[-2:])

                if n == 0:  # lab 0 is updated manually by me
                    continue
                
                os.chdir(folder_name)

                online_date = lab_dates['lab{:02d}'.format(n)][0]
                lab_date = lab_dates['lab{:02d}'.format(n)][1]

                readme_text = self.lab_info_temp.replace(':n:', str(n)).replace(':n02d:', '{:02d}'.format(n)) \
                                                .replace(':help_room_url:', self.course_info['help_room_url']) \
                                                .replace(':online_date:', online_date).replace(':lab_date:', lab_date)

                readme = open('README.md', 'w+')
                print(readme_text, file=readme)
                readme.close()

                os.chdir('..')

        if package:
            self.package('lab')
        
    def update_project_files(self, package:bool=True) -> None:
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
                
                if 'youtube' in href or 'mediaspace' in href:
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

            readme_text = self.project_info_temp.replace(':video:', video).replace(':n:', str(n)) \
                                                .replace(':n02d:', '{:02d}'.format(n)).replace(':due:', project_dates[name_short]) \
                                                .replace(':help_room_url:', self.course_info['help_room_url'])
            
            readme = open('README.md', 'w+')
            print(readme_text, file=readme)
            readme.close()

            video = ''

            os.chdir('..')

        if package:
            self.package('proj')

    def update_schedules(self, prelab_day:str=None, lab_day:str=None) -> None:
        soup = BeautifulSoup(urlopen(self.course_info['schedule_url']), features='html.parser')
        td_deltas = self.__get_td_deltas(soup.find('thead').find_all('th'))
        calendar = self.__create_calendar()

        project_dates = {}
        lab_dates = {}  # lab_dates = { 'labXX': [online_date, lab_date], ... }

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
                pretty_date = self.__get_pretty_date(shifted_date)   # prettier date format for hovertext

                if 'read' in td.lower():
                    calendar[week_n][day]['html'] = '<a title="On: {}" href="{}">{}</a>'.format(pretty_date, self.course_info['week_urls'][str(week_n)], td)
                elif 'exercise' in td.lower():
                    calendar[week_n][day]['html'] = '<a title="Due: {} @ 11:59 PM EST" href="https://class.mimir.io">{}</a>'.format(pretty_date, td)
                elif 'exam' in td.lower():
                    calendar[week_n][day]['html'] = '<a title="On: {}" href="#exam-information">{}</a>'.format(pretty_date, td)
                elif 'proj' in td.lower():
                    proj_n = int(td[-2:])
                    project_dates['proj{:02d}'.format(proj_n)] = pretty_date
                    calendar[week_n][day]['html'] = '<a title="Due: {} @ 11:59 PM EST" href="Project%20{n:02d}">Project {n:02d}</a>'.format(pretty_date, n=proj_n)
                elif 'lab' in td.lower():
                    has_lab = True
                    lab_n = int(td[td.find(' '):])
                    lab_dates['lab{:02d}'.format(lab_n)] = [pretty_date, None] 

                    if lab_n == 0:
                        calendar[week_n][day]['html'] = '<a title="Due: {} @ 11:59 PM EST" href="Lab%2000">Lab 00</a>'.format(pretty_date)
                        lab_dates['lab00'][1] = calendar[week_n][day]['date']

                    if lab_day is None and prelab_day is None:  # if both are None, use date given on website
                        lab_day = prelab_day = day 
                    elif lab_day is None and prelab_day is not None:  # if lab is None and pre-lab has an override, labs use date on website
                        lab_day = day 
                    elif lab_day is not None and prelab_day is None:  # if lab has override and pre-lab doesn't, pre-labs are put on the same day as labs
                        prelab_day = lab_day

                else:  # edge-case for random stuff Enbody sometimes puts on there
                    calendar[week_n][day]['html'] = '<div title="On: {}">{}</div>'.format(pretty_date, td.title())

            if lab_n == 0 or has_lab == False:  # skips pre-lab/lab insertion if lab 0 or if week has no lab
                continue

            lab_html = '<a title="Due: {}" href="Lab%20{n:02d}">Lab {n:02d}</a>'.format(calendar[week_n][lab_day]['date'], n=lab_n)
            prelab_html = '<a title="Due: {} @ 11:59 PM EST" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab {n:02d}</a>'.format(calendar[week_n][prelab_day]['date'], n=lab_n)

            lab_dates['lab{:02d}'.format(lab_n)][1] = calendar[week_n][lab_day]['date']
            
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

        lab_dates_fp = open('assets/lab_dates.json', 'w+')
        json.dump(lab_dates, lab_dates_fp, indent=4)
        lab_dates_fp.close()
        
        self.__process_html_calendar(calendar)

    def package(self, folder_type:Union['proj', 'lab']) -> None:
        if folder_type not in ['proj', 'lab']:
            raise ValueError('folder_type argument not "proj" or "lab"')

        for folder_name in os.listdir():
            if folder_type in folder_name.lower() and '.' not in folder_name:

                zip_file = zipfile.ZipFile('assets/packages/{}{}_content.zip'.format(folder_type, folder_name[-2:]), 'w')

                paths = self.__walk_tree(folder_name)  # inefficient, but eh -- it works

                for path in paths:
                    save_path = path.replace('{}/'.format(folder_name), '')
                    zip_file.write(path, save_path, compress_type=zipfile.ZIP_DEFLATED)
                
                zip_file.close()

    def __walk_tree(self, path:str) -> list:
        file_paths = []
        for root, _, files in os.walk(path):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        return file_paths

    def __course_info_replace(self, text:str) -> str:
        for key, value in self.course_info.items():
            try: 
                text = text.replace(':{}:'.format(key), value)
            except: 
                continue
        return text

    def __create_bar_str(self, p:float) -> str:
        fill_w = floor(p * self.progressbar['width'])
        empty_w = self.progressbar['width'] - fill_w
        return (fill_w * self.progressbar['fill']) + (empty_w * self.progressbar['empty'])

    def __update_plot(self) -> None:
        soup = BeautifulSoup(urlopen('https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'), features='html.parser')

        filename = 'assets/covid_data.xlsx'

        link = 'https://www.michigan.gov'
        for a_tag in soup.find_all('a'):
            href = a_tag.get('href')
            if 'Cases_and_Deaths_by_County_and_by_Date' in href:
                link += href
                break

        urlretrieve(link, filename=filename)

        df = pd.read_excel(filename, sheet_name='Data', dtype=str)
        df = df[df['CASE_STATUS'] == 'Confirmed']
        df = df[df['COUNTY'].isin(PLOT_COUNTIES)]

        _, ax = plt.subplots()

        for county in PLOT_COUNTIES:
            county_data = df[df['COUNTY'] == county].dropna()

            d1 = datetime.strptime(county_data.head(1)['Date'].values[0][:10], '%Y-%m-%d')
            d2 = datetime.strptime(county_data.tail(1)['Date'].values[0][:10], '%Y-%m-%d')
            delta = timedelta(1)

            dates = drange(d1, d2 + delta, delta)
            cases = county_data['Cases'].to_numpy(dtype=int)

            ax.plot_date(dates, cases, '-', label=county, alpha=0.9)

        ax.axvline(x=d2, ymin=0, ymax=0.6, alpha=0.7, color='k', linestyle='--')
        ax.text(x=d2 - timedelta(2), y=ax.get_ylim()[1] / 2, s=d2.strftime('%m/%d/%y'), ha='right')

        ax.xaxis.set_major_formatter(DateFormatter('%m/%d/%y'))
        ax.tick_params(axis='x', top=False, reset=True)
        ax.set_title('New Confirmed Cases of COVID-19 in Michigan by County')
        ax.set_xlabel('Date')
        ax.set_ylabel('New Confirmed Cases')
        ax.legend(loc=2)

        plt.tight_layout()
        plt.xticks(rotation=15)
        # plt.show()
        plt.savefig('assets/images/covid_data.png')

    def __process_html_calendar(self, calendar:dict) -> None:
        fp_out = open('assets/schedule.html', 'w+')

        # finds all day columns that are required to be present (don't ever write code like this lmao)
        headers = sorted(
            {'Week', } | {day for week_dict in calendar.values() for day, day_dict in week_dict.items() if day_dict['html'] != ''},
            key=lambda head: HEADING_ORDER[head]
            )

        print('<div align="center">\n<table>\n<thead>\n<tr>', file=fp_out)
        for head in headers:
            print('<th align="center">{}</th>'.format(head), file=fp_out)
        print('</tr>\n</thead>\n<tbody>', file=fp_out)
        for week_n, week_dict in calendar.items():
            print('<tr>\n<td align="center">{:02d}: {:02d}/{:02d}</td>'.format(
                week_n, 
                week_dict['Sun']['attributes'][1],  # month
                week_dict['Sun']['attributes'][2]   # day
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
        print('</tbody>\n</table>\n</div>', file=fp_out)

        fp_out.close()

    def __get_td_deltas(self, th_list:list) -> dict:
        td_deltas = {}
        for i, th in enumerate(th_list):
            if i == 0: 
                td_deltas[i] = None 
            else: 
                td_deltas[i] = DAY_DELTAS[th.text]

        return td_deltas
    
    def __create_calendar(self) -> dict:
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
                    'date': self.__get_pretty_date(datet), 
                    'attributes': [datet.year, datet.month, datet.day],
                    'html': '',
                    }
                dt += 1
            week_n += 1
        
        return calendar

    def __get_pretty_date(self, datet:datetime) -> str:
        date_str_exp = datet.strftime('%A, %B %d')
        date_str_num = datet.strftime('(%m/%d/%Y)') 

        ordinal_suffix = self.__get_ordinal_suffix(int(date_str_exp[-2:]))

        # All the .replace() methods are to get rid of leading 0s
        full_date = (date_str_exp + ordinal_suffix + ' ' + date_str_num).replace('(0', '(').replace('/0', '/').replace(' 0', ' ')

        return full_date

    def __get_ordinal_suffix(self, num:int) -> str:
        return {1: "st", 2: "nd", 3: "rd"}.get(num % 10 * (num % 100 not in [11, 12, 13]), "th")


if __name__ == "__main__":
    github = CSE231GitHub()

    # github.package('lab')
    # github.update_readme()
    # github.update_project_files(True)
    # github.update_all(True)
