import json
from math import floor
from datetime import datetime, timedelta

BAR = {
    'width': 20,
    'fill': '⬛',
    'empty': '⬜'
}

def create_bar(p:float) -> str:
    if p < 0:
        return (BAR['empty'] * BAR['width']) + ' 0%'

    fill_width = floor(p * BAR['width'])
    return (fill_width * BAR['fill']) + (BAR['empty'] * (BAR['width'] - fill_width)) + ' {:.0%}'.format(p)

def main() -> str:
    course_info = json.load(open('assets/course_info.json', 'r'))

    # today = datetime.now()
    today = datetime(2020, 10, 22)

    first_day = datetime(*course_info['semester_first_day'])
    last_day = datetime(*course_info['semester_last_day'])

    N = last_day - first_day  # number of days in the semester
    n = last_day - today  # current number of days until end of semester

    p = 1 - (n.days / N.days)

    bar_str = create_bar(p)

    return '<div align="center">{}</div>'.format(bar_str)

if __name__ == "__main__":
    main()