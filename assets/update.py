'''
Updates the repository with the CSE231 course website's current schedule
and project files.

Meta details, (e.g. the year, semester, location, etc.), should be updated
manually through course_info.json. 

update_schedule.py
------------------
Creates and/or updates schedule.html and project_dates.json. This script should
always be ran FIRST, as update_project_files and update_meta rely on the two
created files. 

update_project_files.py
-----------------------
Creates and/or updates all project folders with their respective files from the
course website. 

Will only create project folders for project subdomains that exist on the website.

update_meta.py
--------------
Creates and/or updates the main README.md and SYLLABUS.md files from their respective
templates. 

The markdown files use two colons to signify a variable, alike `:var:`. The string
.replace() method is then used to substitute and re-create the files with the proper
information.
'''

import update_meta, update_project_files, update_schedule

print('Creating/Updating schedule.html and project_dates.json...')
update_schedule.main()
print('Done.')

print('Creating/Updating project files...')
update_project_files.main()
print('Done.')

print('Creating/Updating README and SYLLABUS...')
update_meta.main()
print('Done.')