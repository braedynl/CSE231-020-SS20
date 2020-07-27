# FAQ

Frequent student questions that I've been collecting over the years. If the answer to your question ain't in here, I'd be surprised. 

## Where can I find...

**1. ...pre-lab XX?**

Go to the CSE231 [D2L](https://d2l.msu.edu/d2l/loginh/) site, and look through the Content page (could also be on the right sidebar of the home page). 

**2. ...lab XX's files?**

Go to the code for this repository (the [home folder](https://github.com/braedynl/CSE231-GITHUB)), you should see a sub-folder named "Lab XX".

**3. ...lab XX's submission page?**

Go to our [Mimir](https://class.mimir.io/) site, and look through the Active Coursework. 

**4. ...project XX's files?**

Go to the code for this repository (the [home folder](https://github.com/braedynl/CSE231-GITHUB)), you should see a sub-folder named "Project XX". 

**5. ...project XX's submission page?**

Go to our [Mimir](https://class.mimir.io/) site, and look through the Active Coursework. 

**6. ...chapter exercise XX?**

Go to our [Mimir](https://class.mimir.io/) site, and look through the Active Coursework. 

**7. ...the coding standard?**

[Here](https://github.com/braedynl/CSE231-GITHUB/blob/master/CODING_STANDARD.md), in the home folder of the repository. 

**8. ...the syllabus?**

[Here](https://github.com/braedynl/CSE231-GITHUB/blob/master/SYLLABUS.md), in the home folder of the repository.

**9. ...the course schedule?**

[Here](https://github.com/braedynl/CSE231-GITHUB#course-schedule), in the second section of the home folder's README file. 

**10. ...the help room schedule?**

[Here](https://github.com/braedynl/CSE231-GITHUB/blob/master/README.md), at the beginning of the home folder's README file, under the "Logistics" and "Help" link categories.  

**11. ...our section information?**

[Here](https://github.com/braedynl/CSE231-GITHUB#section-information), in the third section of the home folder's README file. 

**12. ...contact information?**

[Here](https://github.com/braedynl/CSE231-GITHUB#contact-information), in the fourth section of the home folder's README file. 

**13. ...exam information?**

[Here](https://github.com/braedynl/CSE231-GITHUB#exam-information), in the fifth section of the home folder's README file. 

**14. ...the past exams?**

[Here](https://web.cse.msu.edu/~cse231/Online/Exams/), at the beginning of the home folder's README file, under the "Help" link category. 

**15. ...your lab slides?**

I categorize them by lab number, so it'll be in the corresponding lab folder's path, i.e. /Lab XX/presentation/

**16. ...our Zoom session information? (only applies to no in-person meeting arrangements)**

It will be in an email sent out to the section. The session details will not be posted here since this is a public page. 

**17. ...our Discord server information? (only applies to summer semesters)**

It will be in an email sent out to the section. The server details will not be posted here since this is a public page. 

## Assignment/Exam Grades

**1. Who do I contact about extensions?**

For exams: Dr. Enbody (enbody@cse.msu.edu) or Dr. Zaabar (zaabarim@cse.msu.edu)

For everything else: me (letting4@msu.edu)

**2. When do our exam grades come back?**

If you took the exam on Mimir: _usually_ the day after all students have taken it (i.e. after makeups have finished, in most cases).

If you took the multiple choice paper exam: _usually_ up to a week after all students have taken it (i.e. after makeups have finished, in most cases).

**3. When do lab/project grades come back?**

_Usually_ the day after everyone in the section has finished, including anyone who had an extension.

**4. How do I view your project feedback?**

Go to your project submission, there should be a blue "View Feedback" button at the top-right of the page.

**5. Is there any leniency for close final grade boundaries?**

Yes, actually. The professors will look for students who are at the edge of grade boundaries when the semester is over. The lower the boundary, the more lenient they'll be about rounding you up (so being rounded to a 2.0 is likelier than being rounded to a 4.0, for example). 

**6. Are there any extra credit assignments?**

Sometimes. I'm not sure when they happen, or for what reason. To me, it seems like it's just whenever Dr. Enbody feels like throwin one out. All instances where extra credit _has_ been served have been small, so don't get your hopes up.


## Academic Dishonesty Reports

**1. Do you know who has received an academic dishonesty report?**

No, unless the student tells me (you don't have to by any means). Academic dishonesty reports are kept private between the professors and the student in question, unless the TA was involved to some capacity.

I have caught plagiarizing students myself, however. I browse through at least one hundred projects every week (all of the section's + students on Piazza), I will occasionally spot similar solutions. 

**2. Have you had students in your section recieve academic dishonesty reports?**

Oh yes, many. It saddens me when it happens -- it feels like a failure on my part, which is why I stress doing your own work so much. I tend to have students that are very open with me, and so I'm aware of almost everyone in my past sections who has received one. I wish I could've stopped them. 

**3. What should I do if I receive an academic dishonesty report?**

You can either take the punishment or appeal. Convictions are usually made with strong evidence, however. I frankly don't know much about the ADR process, so I would visit the Office of the University Ombudsperson [website](https://ombud.msu.edu). 

**4. If you guys are constantly checking for similarities between hundreds of project files, isn't there bound to be at least two students who have similar code that have never spoken to each other?**

It can, and has happened -- so yes, but it is exceedingly rare. Less-experienced programmers are actually _less likely_ to have similar code to other people because their solutions tend to involve odd uses of the language, or strange work-arounds to problems, for which there could be millions of methodologies. 

Experienced programmers are _more likely_ to have similar code to other people because they know the most efficient way of tackling a problem, which tends to be a very limited amount of methodologies. 

It is easy for us to tell when a student plagiarizes in this course, since less-experienced programmers usually can't think of other/equivalent ways of programming an algorithm after seeing an already-implemented solution. The trouble really begins in later CSE courses, since students, by then, will know how to code equivalent expressions/algorithms from looking at their friend's solution.

## Meta

**1. Why does this class teach Python and not [some other programming language]?**

Python is probably the simplest programming language to understand for newcomers, while also being extremely useful and industry standard for many companies -- including companies that aren't like Google, Microsoft, Apple, etc.. Python syntax tends to use natural language expressions rather than complicated strings of rarely-used characters, which helps a lot with mental links to programming concepts. 

Just to show you how simple Python is, here's how you test if an `int` with value `5` is contained within an array, for which we then print our results to the console:
```python
array = [1, 2, 3, 4, 5]

print(5 in array) 
```

... and here's how you do the same thing in C++:
```c++
#include <iostream>
#include <vector>
#include <algorithm>

vector<int> array = {1, 2, 3, 4, 5};

if (std::find(array.begin(), array.end(), 5) != array.end()) {
  std::cout << "true" << std::endl;
} else {
  std::cout << "false" << std::endl;
}
```

Admittedly a somewhat extreme example, but I think you get the point. Python tends to be easier to write in general. Some students may find the indentation of Python annoying, but they get used to it. 

Fun fact: CSE231 used to teach C++!

**2. Are we allowed to use a code editor that's not Spyder?**

Yep! Though bear in mind that the TAs and professors may not be familiar with how some of them work, you'll be on your own if you need help with it.

Other popular code editors:
- [Atom](https://atom.io/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Sublime Text](https://www.sublimetext.com/)
- [Visual Studio Code](https://code.visualstudio.com) (Made by Microsoft, what I use)
- [Xcode](https://developer.apple.com/xcode/) (Made by Apple, MacOS only)

Certain projects pull from 3rd party libraries near the end of the semester, (namely `pylab`), Spyder comes packaged with it, which is why we use Spyder in the first place. You'll have to manually install `pylab` if you're on a different code editor, which I can show you how to do if you can't figure it out for yourself.

**3. Is using w3schools.com and/or programiz.com okay as supplementary material?**

Yee. Just be careful, websites like those may teach certain concepts in a different order, or may show some concepts that we don't teach at all. If you do come across something that we don't teach, it's usually safe to assume that you're not allowed to use it. If you're unsure if a concept may be used in an assignment, feel free to ask on Piazza.

**4. Why are the online exams proctored? That's so stupid.**

It *is* stupid, isn't it? You can ask the students who took this course in Spring 2020 for that answer.

Spoiler: everyone cheated when we didn't proctor. 

**5. Are there exam statistics?**

Dr. Enbody will have them in his post-exam email.

**6. Do the TAs make exam questions?**

No, they're all made by the professors. We review their questions/answers on occasion (mainly checking if there are any mistakes).

**7. Do the TAs make the projects?**

Very, very rarely. There'll be one or two (at most) made by a TA, the rest are made by Dr. Enbody or Dr. Zaabar. 

**8. Do the TAs make the labs?**

No, they were all made by the professors.

**9. There's something on the repository that I think should be added/moved. Can you do anything about it?**

Yes! I'd be happy to, as long as it's within the realm of possibility and I think it'd be a good change. Please email me (letting4@msu.edu), or, if you're feeling spicy, you can make a GitHub account and submit a problem to the "Issues" page. 

## Miscellaneous/Personal

**1. I'm a [major that's not computer science/engineering], will I ever need this?** 

Probably, yeah. Programming is becoming more and more important everyday, to the point where most engineering fields use it to some capacity. The power in programming is its ability to manipulate, and calculate values almost instantaneously in tandem with logic. The phone in your pocket, the stock market, the digital alarm clock on your desk -- all of these wouldn't exist without programming.

**2. Can I forward your emails to my friends in other sections?**

Yes, you may. Though you should warn them that some details I may mention are TA-dependent (e.g. when project/lab grades come back, when D2L gets updated, and anything related to this GitHub repository).

**3. Can my friends in [some other section] use this GitHub repository too?**

Yes, but the course schedule on the home README will only reflect our section's meeting days, they'll have to keep this in mind.

**4. What does your course schedule look like?**

| Time (EST)        | Sun   | Mon    | Tue    | Wed    | Thu    | Fri   | Sat   |
| :---:             | :---: | :---:  | :---:  | :---:  | :---:  | :---: | :---: |
| 10:20 AM-11:40 PM |       |        | CSE331 |        | CSE331 |       |       |
| 12:40 PM-02:00 PM |       | MTH314 | CSE320 | MTH314 | CSE320 |       |       |
| 05:20 PM-06:10 PM |       | STT351 |        | STT351 | STT351 |       |       |

Unlisted: MI349, MI491

How I got such an amazing schedule is beyond me lmao. 

**5. Why do you go through the effort to do all of this?**

Well, I didn't really like Dr. Enbody's website when I took the class myself ("be the change you want to see in the world", right?). When I became a TA, making a GitHub page started out as a way to store my mini-lecture presentations, but then it kind of snowballed into a full-fledged course page as I kept adding more stuff.

In terms of "my thoroughness", (which I know gets talked about by students who have me), I believe all TAs should be just as thorough. My job, (at least in my view), is to make this class a much easier and enjoyable experience for students. I want to ensure that you know where to go, who to contact, and how to get the help you need.

That being said, you shouldn't shame the other TAs. Most of them are senior CSE majors in 400-level classes, they probably don't have that much time on their hands. Why do _I_ have so much time on _my_ hands? Uhh.. well.. I don't really do much other than school work, I tend to get stuff done quickly. 

**6. Are there things, besides assignment answers, that you're not allowed to share with us?**

Yes, but _most_ things that I forbid myself from saying/doing with students is per my own decision. I won't talk to a student about politics, for example, since such a topic could foster contention between me and a student. 

I do, however, likely share a lot more than most TAs. I think being transparent is a good thing, but if a student ever asks about something that has the potential to harm their learning or the learning of others, I'll probably say that I cannot give an answer. 

**7. How does this repository automatically stay up-to-date with the course website?**

There are Python modules that allow you to [web scrape](https://en.m.wikipedia.org/wiki/Web_scraping), (collect data from websites). The code that keeps this page up-to-date does a few things: it updates the course schedule, syllabus, home README, and all lab/project files. The update script can be found in /assets/update.py.

The syllabus and home README have templates that you can find in /assets/templates/. There are "variables" encoded into the documents (words surrounded by colons like :this:) that my program simply finds and replaces with the proper information (like year, semester, location, etc.). Lab and project folders have their own README files, these are also updated via templates in a similar fashion.

The course schedule on the home README literally has its HTML code (the code that displays the schedule) ripped straight from Dr. Enbody's website (the Due Dates page, specifically). My code disassembles the HTML and re-constructs it with links, standardized formatting, and hover text. So, yes, it's a program that writes a program in a way.

For project files, I noticed that Dr. Enbody would keep the URL of the project domains consistent, (like it would always be /projects/Project01/, /projects/Project02/, etc.), I used this to my advantage. A template URL with a missing project number is kept as a constant within the program, where a for-loop then iterates through numbers to fill the gap. The program then web-scrapes all the links from the page, and downloads each file if the domain exists. If the domain doesn't exist yet, no folder on the GitHub page is created. 

**8. How does the progress bar work?**

The number of days in the semester is calculated from dates that I feed it, we'll call this `N`. The program also extracts the date that it's currently running at, we'll call this little `n`. The percentage of completion can then be calculated as `1 - (n / N)`, we'll call this `p`.

There are three attributes to the progress bar: a width (14, at the time of writing. Was chosen so that it will display properly on most devices), a fill character (⬛, the black square emoji), and an empty character (⬜, the white square emoji). 

The number of fill characters we need will be `p` (the percentage of completion) multiplied by the width, [floored](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) -- i.e. the number that is `p` percent of the width. We floor this value because the number of fill characters can't be a decimal number, and we don't round because a value like 0.95 could be interpreted as 100%, which could be misleading. 

We store this number of fill characters, and subtract the total width from it to find the number of empty characters we need to complete the bar. We finally concatenate the two chunks of fill and empty character strings together. 

Below is a psuedocode algorithm:

```python
bar = {
  'width' : 14,
  'fill' : '⬛',  # yes, you can store emojis in strings lmao
  'empty': '⬜'
}

today = ...  # using a date-fetching library
semester_end = ...
semester_start = ...

N = semester_end - semester_start  # number of days in the semester
n = semester_end - today           # number of days until the end of the semester

p = 1 - (n / N)  # find the percentage of completion

fill_num = floor(p * bar['width'])  # number of fill characters we need (decimal, so we floor)

empty_num = bar['width'] - fill_num  # number of empty characters we need to complete the rest of the bar

bar_str = (fill_num * bar['fill']) + (empty_num * bar['empty'])  # combine
```

**9. What are those small messages that appear next to file names?**

[Commit messages](https://en.wikipedia.org/wiki/Commit_(version_control)). Whenever I make changes to the repository, one of the common version control practices is to describe what you, as the committer, changed. I keep them extremely brief since I'm the only one working on the repository. You can ignore them, they're more for my sake. 

**10. What is the ".md" file extension that you use?**

[Markdown](https://en.wikipedia.org/wiki/Markdown). They're kinda like .txt files, but will convert all text into HTML script internally. I use them because they're easy to write, and allow for extensive formatting. 

**11. What is the ".json" file extension that you use?**

[JavaScript Object Notation](https://en.wikipedia.org/wiki/JSON). They're text files that store JavaScript object data, but most programming language (like Python) have libraries that read them. I use it a lot because it's extremely quick and readable.

**12. How did you prepare for CSE231 exams?**

I went through the past exams and took them as if they were the real deal -- timer and all. I went back through questions I got wrong with PythonTutor, and asked about ones I didn't understand on Piazza. 

Come exam day, I drank a ludicrous amount of coffee... though I don't recommend doing that. Drink coffee safely, [studies](https://link.springer.com/article/10.1007/s12603-014-0563-8) have shown that caffeine does indeed improve cognitive function. 

**13. How did you do when you took this class?**

I got a 4.0, but I'm not smart by any means -- I just have _a lot_ of practice because I've been programming since I was a kid. If you're having a hard time, please don't compare your situation to people like me, because it's not the same. Programming is an extremely hard skill to master for a majority of people. The biggest thing you can do is practice. 

**14. Do you use tabs or spaces?**

Tabs, I'm not tryna demolish my spacebar.

**15. Do you know any other programming languages?**

C, C++, JavaScript, and a minuscule amount of Java. I definitely use Python the most, however (you can tell if you look at my GitHub projects lol).

**16. Does the language you use in the real world matter?**

Kind of, it depends on what you're doing. If you're making a desktop application, or need hyper-fast arithmetic, you'll want C or C++. If you're doing anything web-related, then JavaScript is, and will always be, the industry standard -- you should definitely learn JavaScript at some point if you're a CSE major, you're going to need it. Python/Java can be used for everything else, though Java is mostly being phased out in favor of Python. 

If you're interested in data science, machine learning, ethical hacking, web-scraping, or academic research, Python is your go-to (not a complete list). 

**17. What is your ethnic background?**

I'm half white, half Korean. 

**18. Do you have social media?**

Hardly. I have a Twitter and a Snapchat, but I'm rarely ever on my phone in the first place. Talk with me if you want to add me. 

**19. What code editor do you use?**

[Visual Studio Code](https://code.visualstudio.com).

**20. How do you type so fast?**

Too much time spent writing essays in an IB high school. 

**21. Where can I apply to become a ULA for a CSE course?**

[Here](https://www.cse.msu.edu/Resources/EmploymentStudents.php). I had to finish CSE232 before Dr. Enbody would hire me for CSE231, I'm unsure if that rule still applies. I'm sure other professors have restrictions like that.

**22. Do you need a 4.0 to become a ULA for this class?**

Maybe? I actually have no idea, that'd be a good question for Dr. Enbody. If I had to guess, I'd say 3.5-4.0. Maybe 3.0 if you answer questions on Piazza frequently. You should still answer questions on Piazza even if you're in good standing grade-wise, it'll show that you're eager to help others. 

**23. Do you need to be a CSE major to become a ULA for this class?**

No, but Dr. Enbody probably wants you to be comfortable with programming in general. 

**24. How much do you get paid?**

$11/hour, though MSU had to reduce everyone's wage a little because of COVID-19.

**25. Can you give me a referral?**

If I think you got what it takes, then maybe. Talk to me about it. 
