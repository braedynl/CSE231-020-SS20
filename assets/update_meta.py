import json
import update_progressbar

def main():
    course_info = json.load(open('assets/course_info.json', 'r'))  # must be local
    schedule = open('assets/schedule.html', 'r').read()  # must be local
    progressbar = update_progressbar.main()

    readme = open('assets/templates/readme_temp.md', 'r', encoding='utf-8').read().replace(':schedule:', schedule).replace(':progressbar:', progressbar)
    syllabus = open('assets/templates/syllabus_temp.md', 'r').read() 

    for key, value in course_info.items():
        try:
            readme = readme.replace(':{}:'.format(key), value)
            syllabus = syllabus.replace(':{}:'.format(key), value)
        except:
            continue

    print(readme, file=open('README.md', 'w+'), end='')
    print(syllabus, file=open('SYLLABUS.md', 'w+'), end='')

if __name__ == "__main__":
    main()