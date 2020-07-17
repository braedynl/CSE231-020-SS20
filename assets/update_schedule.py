import json
from datetime import datetime, timedelta
from urllib.request import urlopen
from bs4 import BeautifulSoup

COURSE_INFO = json.load(open('assets/course_info.json', 'r'))
TIME_DELTAS = {'Sun': 0, 'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6}

def get_table_deltas(soup:BeautifulSoup) -> dict:
    # since I'm not sure what days of the week Enbody is going to include, a lookup
    # table is created in get_table_deltas(). 
    # the day positions in the table's header row is used to circumvent this issue,
    # but is obviously reliant on Enbody keeping the first column as the week numbers
    # and using shorthand week-day notation (e.g. "Mon", "Tue", etc.)

    td_deltas = {}  # FORMAT: td_iteration : time_delta

    for i, th in enumerate(soup.find('thead').find_all('th')):
        if i == 0:
            td_deltas[i] = None  # 0th td is the week number/date
        else:
            td_deltas[i] = TIME_DELTAS[th.text]
    
    return td_deltas

def main():
    soup = BeautifulSoup(urlopen(COURSE_INFO['schedule_url']), features='html.parser')
    td_deltas = get_table_deltas(soup)
    out_html = open('assets/schedule.html', 'w+')
    project_dates = {}  # used for update_project_files

    print('<table>', file=out_html)
    print(soup.find('thead'), file=out_html)
    print('<tbody>', file=out_html)

    tr_list = soup.find('tbody').find_all('tr')
    for i, tr in enumerate(tr_list):

        if i == len(tr_list)-1:  # Stops before last row, something is wrong with the way Enbody made it 🙃
            break                # TODO: Needs better solution

        print('<tr>', file=out_html)
        for i, td in enumerate(tr.find_all('td')):

            print('<td align="center">', end='', file=out_html)
            td_text = td.text.strip()

            # first column will always be the week# and starting date (summer semester too)
            if i == 0:
                colon_i = td_text.find(':')
                week_num = int(td_text[:colon_i])
                date = td_text[colon_i + 2:]

                slash_i = date.find('/')
                month = int(date[:slash_i])
                day = int(date[slash_i + 1:])

                print('{:02d}: {:02d}/{:02d}</td>'.format(week_num, month, day), file=out_html)

                # creates a datetime instance to calculate exact dates for the week's assignments,
                # Sunday is treated as "day 0"
                datet = datetime(int(COURSE_INFO['year']), month, day)
        
            else:
                title = (datet + timedelta(td_deltas[i])).strftime('%A, %B %d (%m/%d/%y)')

                if i == 1:
                    # this assumes Enbody will always put the readings/lecture videos on Sunday, which
                    # coouulldd be problematic. would likely be an easy fix if this needs changing
                    print('<a title="{}" href="{}">{}</a></td>'.format(title, COURSE_INFO['week_urls'][str(week_num)], td_text), file=out_html)
                else:
                    if td_text == '':
                        print('</td>', file=out_html)

                    # for some reason, Enbody names labs as "Lab XX", but names projects as "projXX" 🙃
                    # these conditions are to standardize it as "Lab XX" and "Project XX",
                    # also attaches more stuff to the HTML td tags, like hover text and hrefs

                    elif 'lab' in td_text.lower():
                        lab_num = int(td_text[td_text.find(' '):])
                        print('<a title="{}" href="Lab%20{n:02d}">Lab {n:02d}</a></td>'.format(title, n=lab_num), file=out_html)

                    elif 'proj' in td_text.lower():
                        proj_num = int(td_text[-2:])
                        project_dates['Project {:02d}'.format(proj_num)] = title
                        print('<a title="{}" href="Project%20{n:02d}">Project {n:02d}</a></td>'.format(title, n=proj_num), file=out_html)

                    elif 'exercise' in td_text.lower():
                        print('<a title="{}" href="https://class.mimir.io">{}</a></td>'.format(title, td_text), file=out_html)
                    
                    else:
                        print('<div title="{}">{}</div></td>'.format(title, td_text.title()), file=out_html)

        print('</tr>', file=out_html)
    print('</tbody>', file=out_html)
    print('</table>', file=out_html)

    json.dump(project_dates, open('assets/project_dates.json', 'w+'), indent=4)

    out_html.close()

if __name__ == "__main__":
    main()
