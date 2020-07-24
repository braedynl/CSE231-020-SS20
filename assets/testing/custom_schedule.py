import json
from datetime import datetime, timedelta
from urllib.error import HTTPError
from urllib.request import urlopen, urlretrieve

from bs4 import BeautifulSoup

'''
calendar = {
    week_n : {
        "day" : {
            "date" : str,
            "attributes" : list,
            "html" : str
        },
        ...
    },
    ...
}
'''

COURSE_INFO = json.load(open('assets/course_info.json', 'r'))

DAY_DELTAS = {'Sun': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6}

START = [2020, 8, 30]
END = [2020, 12, 19]

def create_calendar(start:list, end:list) -> dict:
    start_date = datetime(*start)
    end_date = datetime(*end)

    calendar = {}

    week_n = 0
    dt = 0

    while (start_date + timedelta(dt)) < end_date:
        calendar[week_n] = {}
        for day in DAY_DELTAS.keys():
            datet = start_date + timedelta(dt)

            calendar[week_n][day] = {
                'date': get_pretty_date(datet), 
                'attributes': [datet.year, datet.month, datet.day],
                'html': '',
                }

            dt += 1
        week_n += 1
    
    return calendar


def get_td_deltas(soup:BeautifulSoup) -> dict:
    td_deltas = {}
    for i, th in enumerate(soup.find('thead').find_all('th')):
        if i == 0:
            td_deltas[i] = None 
        else:
            td_deltas[i] = DAY_DELTAS[th.text]
    
    return td_deltas


def get_ordinal_suffix(num:int) -> str:
    return {1: "st", 2: "nd", 3: "rd"}.get(num % 10 * (num % 100 not in [11, 12, 13]), "th")


def get_pretty_date(datet:'datetime') -> str:
    date_str_exp = datet.strftime('%A, %B %d')
    date_str_num = datet.strftime('(%m/%d/%Y)') 

    ordinal_suffix = get_ordinal_suffix(int(date_str_exp[-2:]))

    full_date = (date_str_exp + ordinal_suffix + ' ' + date_str_num).replace('(0', '(').replace('/0', '/').replace(' 0', ' ')

    return full_date


def fill_calendar(calendar:dict, prelab_day:str, lab_day:str):

    soup = BeautifulSoup(urlopen(COURSE_INFO['schedule_url']), features='html.parser')

    td_deltas = get_td_deltas(soup)

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
            pretty_date = get_pretty_date(shifted_date)   # prettier date format for hovertext

            if 'read' in td.lower():
                calendar[week_n][day]['html'] = '<a title="On: {}" href="{}">{}</a>'.format(pretty_date, COURSE_INFO['week_urls'][str(week_n)], td)
            elif 'exercise' in td.lower():
                calendar[week_n][day]['html'] = '<a title="Due: {}" href="https://class.mimir.io">{}</a>'.format(pretty_date, td)
            elif 'exam' in td.lower():
                calendar[week_n][day]['html'] = '<a title="On: {}" href="#exam-information">{}</a>'.format(pretty_date, td)
            elif 'proj' in td.lower():
                proj_n = int(td[-2:])
                calendar[week_n][day]['html'] = '<a title="Due: {}" href="Project%20{n:02d}">Project {n:02d}</a>'.format(pretty_date, n=proj_n)
            elif 'lab' in td.lower():
                has_lab = True
                lab_n = int(td[td.find(' '):])
                if lab_n == 0:
                    calendar[week_n][day]['html'] = '<a title="Due: {}" href="Lab%2000">Lab 00</a>'.format(pretty_date)
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

    return calendar


def create_html_calendar(calendar:dict) -> None:

    fp_out = open('assets/testing/schedule_test.html', 'w+')

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
    print('\t<tr>', file=fp_out)
    for head in headers:
        print('\t\t<th align="center">{}</th>'.format(head), file=fp_out)
    print('\t</tr>', file=fp_out)
    print('</thead>', file=fp_out)

    print('<tbody>', file=fp_out)
    for week_n, week_dict in calendar.items():
        print('\t<tr>', file=fp_out)
        print('\t\t<td align="center">{:02d}: {:02d}/{:02d}</td>'.format(
            week_n, 
            week_dict['Sun']['attributes'][1],
            week_dict['Sun']['attributes'][2]
            ),
            file=fp_out
        )
        for day, day_dict in week_dict.items():
            if day in headers:
                if 'read' in day_dict['html'].lower():
                    print('\t\t<td>{}</td>'.format(day_dict['html']), file=fp_out)
                else:
                    print('\t\t<td align="center">{}</td>'.format(day_dict['html']), file=fp_out)
        print('\t</tr>', file=fp_out)
    print('</tbody>', file=fp_out)

    print('</table>', file=fp_out)

    fp_out.close()


calendar = create_calendar(START, END)
filled_calendar = fill_calendar(calendar, prelab_day='Thu', lab_day='Fri')

create_html_calendar(filled_calendar)