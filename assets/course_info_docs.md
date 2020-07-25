# course_info.json

Use `"TBA"` to represent an unknown `str` value in all cases.

`"section"` - Section number. 
- Type: `int`
- Recognized: *
- Dependents: `update_readme()`

`"semester"` - Semester season.
- Type: `str`
- Recognized: `"Fall"`, `"Spring"`, `"Summer"`
- Dependents: `update_readme()`, `update_syllabus()`

`"year"` - Semester year.
- Type: `int`
- Recognized: *
- Dependents: `update_readme()`, `update_syllabus()`

`"section_details"` - Location, days, and time. 
- Type: `str`
- Recognized: `"Online - [Weekday] at [HH]:[MM] [AM, PM] EST"`, `"Engineering Building Rm. 3320 - [Weekday] at [HH]:[MM] [AM, PM] EST"`, `"Wilson Hall Rm. C004 - [Weekday] at [HH]:[MM] [AM, PM] EST"`
- Dependents: `update_readme()`

`"exam1_details"`, `"exam2_details"`, `"exam3_details"` - Exam locations, dates and times. 
- Type: `str`
- Recognized: `"Online - [Weekday], [Month] [d][Ordinal Suffix] ([m]/[d]/[y]) at [HH]:[MM] [AM, PM] EST"`, `"[Building] Rm. [Number] - [Weekday], [Month] [d][Ordinal Suffix] ([m]/[d]/[y]) at [HH]:[MM] [AM, PM] EST"`
- Dependents: `update_readme()`, `update_syllabus()`

`"schedule_url"` - URL of the main course website's Due Dates page. 
- Type: `str`
- Recognized: *
- Dependents: `update_schedules()`

`"help_room_url"` - URL of the help room schedule.
- Type: `str`
- Recognized: *
- Dependents: `update_readme()`, `update_lab_files()`, `update_project_files()`

`"labs_url"` - URL of the lab schedule.
- Type: `str`
- Recognized: *
- Dependents: `update_readme()`

`"week_urls"` - Mapping of week numbers to URLs. 
- Type: `Dict[str] = str`
- Recognized: *
- Dependents: `update_schedules()`

`"semester_start"` - Starting date of the semester in order: year, month, day. 
- Type: `List[int, int, int]`
- Recognized: *
- Dependents: `update_schedules()`

`"semester_end"` - Ending date of the semester in order: year, month, day. 
- Type: `List[int, int, int]`
- Recognized: *
- Dependents: `update_schedules()`

`"schedule_start"` - The earliest Sunday's date on the main course website's Due Dates page. In order: year, month, day. 
- Type: `List[int, int, int]`
- Recognized: *
- Dependents: `update_schedules()`

`"schedule_end"` - The latest Saturday's date on the main course website's Due Dates page. In order: year, month, day. 
- Type: `List[int, int, int]`
- Recognized: *
- Dependents: `update_schedules()`

`"lab_day"` - Day of weekly labs. Use `null` to indicate no change in lab days from the Due Dates page. 
- Type: `str`
- Recognized: `"Mon"`, `"Tue"`, `"Wed"`, `"Thu"`, `"Fri"`, `"Sat"`, `null`
- Dependents: `update_schedules()`

`"prelab_day"` - Day of weekly pre-labs. Use `null` to set pre-labs on the same day as labs. 
- Type: `str`
- Recognized: `"Mon"`, `"Tue"`, `"Wed"`, `"Thu"`, `"Fri"`, `"Sat"`, `null`
- Dependents: `update_schedules()` 