import json
from math import floor
from datetime import datetime, timedelta

BAR = {
    'width': 14,
    'fill': '⬛',
    'empty': '⬜'
}

def create_bar(p:float) -> str:
    if p < 0:
        return BAR['empty'] * BAR['width']

    fill_width = floor(p * BAR['width'])
    return (fill_width * BAR['fill']) + (BAR['empty'] * (BAR['width'] - fill_width))

def main() -> str:
    course_info = json.load(open('assets/course_info.json', 'r'))

    today = datetime.now()
    # today = datetime(2020, 10, 21)

    first_day = datetime(*course_info['semester_first_day'])
    last_day = datetime(*course_info['semester_last_day'])

    N = last_day - first_day  # number of days in the semester
    n = last_day - today  # current number of days until end of semester

    p = 1 - (n.days / N.days)

    bar_str = create_bar(p)

    if p < 0:
        p = 0

    return '<div align="center"><b>Semester Progress ({:.0%})</b>\n</div><div align="center">{}</div>'.format(p, bar_str)

if __name__ == "__main__":
    main()