'''
CURRENT TEMPLATE VARIABLES:

    :section:
    :semester:
    :year:
    :location:
    :time:
    :exam1_details:
    :exam2_details:
    :exam3_details:

See course_info.json for formats
'''

import json

course_info = json.load(open('assets/course_info.json', 'r')); del course_info['__formats__']
schedule = open('assets/course_schedule.html', 'r').read()  

readme = open('assets/readme_template.md', 'r').read().replace(':schedule:', schedule)
syllabus = open('assets/syllabus_template.md', 'r').read() 

out_readme = open('README.md', 'w+')
out_syllabus = open('SYLLABUS.md', 'w+')

for key, value in course_info.items():
    readme = readme.replace(':{}:'.format(key), value)
    syllabus = syllabus.replace(':{}:'.format(key), value)

print(readme, file=out_readme, end='')
print(syllabus, file=out_syllabus, end='')