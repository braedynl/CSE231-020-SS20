# FAQ

Frequent student questions that I've been collecting over the years. If the answer to your question ain't in here, I'd be surprised. 

Jump to section:
1. [Where can I find...](#where-can-i-find)
2. [Grades](#grades)
3. [Meta](#meta)
4. [CSE Computing System](#cse-computing-system)
5. [Spyder](#spyder)
6. [Programming](#programming)
7. [Academic Dishonesty Reports](#academic-dishonesty-reports)
8. [Miscellaneous/Personal](#miscellaneouspersonal)

## Where can I find...

**1. pre-lab XX?**

Go to the CSE231 [D2L](https://d2l.msu.edu/d2l/loginh/) site, and look through the Content page (could also be on the right sidebar of the home page). 

**2. lab XX's files?**

Go to the code for this repository (the [home folder](https://github.com/braedynl/CSE231-GITHUB)), you should see a sub-folder named "Lab XX".

**3. lab XX's submission page?**

Go to our [Mimir](https://class.mimir.io/) site, and look through the Active Coursework. 

**4. project XX's files?**

Go to the code for this repository (the [home folder](https://github.com/braedynl/CSE231-GITHUB)), you should see a sub-folder named "Project XX". 

**5. project XX's submission page?**

Go to our [Mimir](https://class.mimir.io/) site, and look through the Active Coursework. 

**6. chapter exercise XX?**

Go to our [Mimir](https://class.mimir.io/) site, and look through the Active Coursework. 

**7. the coding standard?**

[Here](https://github.com/braedynl/CSE231-GITHUB/blob/master/CODING_STANDARD.md), in the home folder of the repository. 

**8. the syllabus?**

[Here](https://github.com/braedynl/CSE231-GITHUB/blob/master/SYLLABUS.md), in the home folder of the repository.

**9. the course schedule?**

[Here](https://github.com/braedynl/CSE231-GITHUB#course-schedule), in the second section of the home folder's README file. 

**10. our section information?**

[Here](https://github.com/braedynl/CSE231-GITHUB#section-information), in the third section of the home folder's README file. 

**11. contact information?**

[Here](https://github.com/braedynl/CSE231-GITHUB#contact-information), in the fourth section of the home folder's README file. 

**12. exam information?**

[Here](https://github.com/braedynl/CSE231-GITHUB#exam-information), in the fifth section of the home folder's README file. 

**13. the help room schedule?**

[Here](https://github.com/braedynl/CSE231-GITHUB/blob/master/README.md), at the beginning of the home folder's README file, under the "Logistics" and "Help" link categories.  

**14. the past exams?**

[Here](https://github.com/braedynl/CSE231-GITHUB/blob/master/README.md), at the beginning of the home folder's README file, under the "Help" link category. 

**15. your lab slides?**

I categorize them by lab number, so it'll be in the corresponding lab folder's path, i.e. /Lab XX/presentation/

**16. our Microsoft Teams session information? (only applies to no in-person meeting arrangements)**

It will be in an email sent out to the section. The session details will not be posted here since this is a public page. 

**17. our Discord server information? (only applies to summer semesters)**

It will be in an email sent out to the section. The server details will not be posted here since this is a public page. 


## Grades

**1. Who do I contact about extensions?**

For exams: Dr. Enbody (enbody@cse.msu.edu) or Dr. Zaabar (zaabarim@cse.msu.edu)

For everything else: me (letting4@msu.edu)

**2. Who do I contact about a grading dispute?**

For exams: Dr. Enbody (enbody@cse.msu.edu) or Dr. Zaabar (zaabarim@cse.msu.edu)

For everything else: me (letting4@msu.edu)

**3. When do our exam grades come back?**

If you took the exam on Mimir: _usually_ the day after all students have taken it (i.e. after makeups have finished, in most cases).

If you took the multiple choice paper exam: _usually_ up to a week after all students have taken it (i.e. after makeups have finished, in most cases).

**4. When do lab/project grades come back?**

_Usually_ the day after everyone in the section has finished, including anyone who had an extension.

**5. How do I view your project feedback?**

Go to your project submission, there should be a blue "View Feedback" button at the top-right of the page.

**6. Is there any leniency for close final grade boundaries?**

Yes, actually. The professors will look for students who are at the edge of grade boundaries when the semester is over. The lower the boundary, the more lenient they'll be about rounding you up (so being rounded to a 2.0 is likelier than being rounded to a 4.0, for example). 

**7. Are there any extra credit assignments?**

Sometimes. I'm not sure when they happen, or for what reason. To me, it seems like it's just whenever Dr. Enbody feels like throwin one out. All instances where extra credit _has_ been served have been small, so don't get your hopes up.


## Meta

**1. Mimir is asking for a course code, what is ours?**

There is no course code. Access Mimir from the link provided on our [D2L page](https://d2l.msu.edu/d2l/loginh/) and it should get everything sorted for you.

**2. I missed [an assignment], what should I do?**

If you missed it due to illness or a personal emergency, please contact me (letting4@msu.edu). 

**3. I missed an exam, what should I do?**

Please contact Dr. Enbody (enbody@cse.msu.edu) and/or Dr. Zaabar (zaabarim@cse.msu.edu).

**4. I need extra help.**

All of the TAs staff help room at certain points during the week, I highly recommend attending (applies to Fall/Spring only). 

Piazza is the fastest way to get answers, and offers anonymity if that's something you'd prefer. 

You may also contact me (letting4@msu.edu), or whoever your favorite TA is for more personal help. 

Some students want a tutor. The department does not have the resources to screen and train tutors, though some students have had luck finding one online through Facebook, Reddit, and universitytutor.com. Please be cautious with meeting people you find online — only meet in public areas. Always ensure you're actually learning the content, and not just having the tutor do all of the work for you. 

**5. Why does this class teach Python and not [some other programming language]?**

Python is probably the simplest programming language to understand for newcomers, while also being extremely useful and popular to use in real-world applications. Python syntax tends to use natural language expressions rather than complicated strings of characters, which helps a lot with mental links to programming concepts. 

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

Admittedly an extreme example, but yeah, Python tends to be easier to write in general. Some students may find the indentation of Python annoying, but they get used to it.

Fun fact: CSE231 used to teach C++!

**6. Are we allowed to use a code editor that's not Spyder?**

Yep! Though bear in mind that the TAs and professors may not be familiar with how some of them work, you'll be on your own if you need help with it.

Other popular code editors:
- [Atom](https://atom.io/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Sublime Text](https://www.sublimetext.com/)
- [Visual Studio Code](https://code.visualstudio.com) (Made by Microsoft, what I use)
- [Xcode](https://developer.apple.com/xcode/) (Made by Apple, MacOS only)

Certain projects pull from 3rd party libraries near the end of the semester, (namely `pylab`), Spyder comes packaged with it, which is why we use Spyder in the first place. You'll have to manually install `pylab` if you're on a different code editor, which I can show you how to do if you can't figure it out for yourself.

**7. What do I do if I have a chromebook?**

You'll have to install the DECS RDP client on your chromebook and use Anaconda/Spyder remotely on the DECS servers. Instructions can be found [here](https://www.egr.msu.edu/decs/help-support/how-to/connect-decs-remote-desktop-services-rds-servers). 

If you are experiencing issues installing the DECS Remote Client, take your chromebook to [DECS Support](https://www.egr.msu.edu/decs/help-support). 

Once installed, login to EGR RDP using your EGR credentials, and you should be free to use Anaconda/Spyder.

One student found [this article](https://chromebook.home.blog/2019/01/20/installing-anaconda-on-a-chromebook-no-dev-beta-or-crouton-needed/) that may be another viable option.

I unfortunately don't know much about ChromeOS, so if you're encountering trouble, I'd post a question to Piazza. There's bound to be at least one student or TA who's familiar with the operating system.

**8. Is using w3schools.com and/or programiz.com okay as supplementary material?**

Yes. Just be careful, websites like those may teach certain concepts in a different order, or may show some concepts that we don't teach at all. If you do come across something that we don't teach, it's usually safe to assume that you're not allowed to use it. If you're unsure if a concept may be used in an assignment, feel free to ask on Piazza.

**9. Why are the online exams proctored? That's so stupid.**

It *is* stupid, isn't it? You can ask the students who took this course in Spring 2020 for that answer.

Spoiler: everyone cheated when we didn't proctor. 

**10. Are there exam statistics?**

Dr. Enbody will have them in his post-exam email.

**11. Do the TAs make exam questions?**

No, they're all made by the professors. We review their questions/answers on occasion (mainly checking if there are any mistakes).

**12. Do the TAs make the projects?**

Very, very rarely. There'll be one or two (at most) made by a TA, the rest are made by Dr. Enbody or Dr. Zaabar. 

**13. Do the TAs make the labs?**

No, they were all made by the professors.

**14. There's something on the repository that I think should be added/moved/removed. Can you do anything about it?**

Yes! I'd be happy to, as long as it's within the realm of possibility and I think it'd be a good change. Please email me (letting4@msu.edu) about it.


## CSE Computing System

**1. Where can I find more information about the CSE computing system?**

The [Facilities](http://www.cse.msu.edu/Resources/Facilities/) page usually has the answers you're looking for. 

**2. How do I log into the CSE computing system for the first time?**

See the [First Login](http://www.cse.msu.edu/Resources/Facilities/Account/FirstLogin.php) page. 

**3. How do I change/reset my CSE password?**

See the [Account Information](http://www.cse.msu.edu/Resources/Facilities/Account/) page.

**4. Can I recover a deleted file in my CSE account?**

See the [User File Backups](http://www.cse.msu.edu/Resources/Facilities/Policies/Backups.php) page.

**5. How do I access my CSE account remotely?**

See the [Remote Access](https://www.cse.msu.edu/Resources/Facilities/Services/SSH.php) page (this is fairly advanced stuff, feel free to ask us about this).

**6. Why can't I use Samba off campus?**

Many Internet Service Providers disallow Samba connections (SMB network protocols). Might be worth looking into alternatives. 


## Spyder

**1. My shell and variable explorer disappeared. How do I get them back?**

There is a tab at the top called "View". In View, there's a subcategory called "Panes". You can re-enable the shell and variable explorer here, among other windows.

Alternatively, you can go to the "Tools" tab, and hit "Reset Spyder to Factory Defaults". 

**2. Running my program with the debugger executes the program normally.**

You probably didn't set a breakpoint. 

**3. Spyder isn't working.**

Most problems with Spyder can be solved with a [reinstallation](https://docs.anaconda.com/anaconda/install/uninstall/). Ensure that your problem is with *Spyder itself* and not your program's execution (did you call your `main()` function? Did you call your other functions?). 

**4. Reinstalling Spyder didn't work.**

Contact me about it (letting4@msu.edu).

**5. Spyder is saying that the `pylab` module could not be found.**

Try updating your Spyder installation (open Anaconda Navigator, click the gear icon at the top-right, and select "Update Application"). 

If the option is greyed-out and/or updating did not fix the issue, contact me (letting4@msu.edu).


## Programming

**1. How do you print an empty line?**

You can use `print()` with no arguments.

Example:
```python
print("Line 1")
print()
print("Line 2")
```
Out:
```
Line 1

Line 2
```

**2. Can you have multiple print statements display on the same line in console?**

Yes. The `print()` function has a parameter called `end`, which specifies a `str` to concatenate to the back of the line that's being printed. It has a default value of `'\n'`, the newline character, which is why print statements on subsequent lines in your code display text on subsequent lines in the console. 

Default behavior:
```python
print("Line 1")
print("Line 2")
```
Out:
```
Line 1
Line 2
```

Changing `end`:
```python
print("Line 1", end='')  # set to empty string
print("Line 2")
```
Out:
```
Line 1Line2
```

**3. What's the best way to reverse a string/list?**

Negative step indices.

Example:
```python
my_str = 'hello'
my_list = [1, 2, 3]

print(my_str[::-1])
print(my_list[::-1])
```
Out:
```
olleh
[3, 2, 1]
```

**4. What are the immutable and mutable types?**

Immutable: `int`, `str`, `float`, `bool`, `tuple`

Mutable: `list`, `set`, `dict`

**5. What's the difference between immutable and mutable types?**

Immutable types _pass by copy_, while mutable types _pass by reference_.

Consider the following example. Recall that strings are immutable, and lists are mutable. 
```python
def my_function(obj):
    return obj

my_str = 'hello'
my_list = [1, 2, 3]

# we're going to pass my_str and my_list to a function that simply returns its one parameter
new_str = my_function(my_str)
new_list = my_function(my_list)

# All seems well at first.
print("Before changes")
print("---")
print("my_str   = {}".format(my_str))
print("new_str  = {}".format(new_str))
print("my_list  = {}".format(my_list))
print("new_list = {}".format(new_list))

# now let's perform their corresponding appendation methods
new_str = new_str + ' world!'
new_list.append(4)

# notice what changed?
print("\nAfter changes")
print("---")
print("my_str   = {}".format(my_str))
print("new_str  = {}".format(new_str))
print("my_list  = {}".format(my_list))
print("new_list = {}".format(new_list))
```
Out:
```
Before changes
---
my_str   = hello
new_str  = hello
my_list  = [1, 2, 3]
new_list = [1, 2, 3]

After changes
---
my_str   = hello
new_str  = hello world!
my_list  = [1, 2, 3, 4]
new_list = [1, 2, 3, 4]
```

So what happened here? `my_str` was left _unchanged_, while `new_str` was _changed_. `my_list` was _changed_, but `new_list` was also _changed_.

When `my_str` gets passed to `my_function()`, a _copy_ of `my_str`'s value gets passed to the `obj` parameter. We're taking that copy, and storing it in a new variable called `new_str` — and because it's a copy, changes made to `new_str` **_will not affect_** `my_str`. 

When `my_list` gets passed to `my_function()`, a _reference_ of `my_list` gets passed to the `obj` parameter. We're taking that reference, and storing it in a new variable called `new_list` — and because it's a reference, changes made to `new_list` **_will affect_** `my_list`. 

Note that this difference is also why many `list` method functions _don't_ require a variable reassignment. These are referred to as **in-place** method functions — only mutable types will have them for this reason. There are some operations between mutable and immutable types that may _seem_ identical at first, but have one or two key differences. For example:

```python
my_str = 'hello'
my_list = [1, 2, 3]

print(my_str[0])   # perfectly okay!
print(my_list[0])  # perfectly okay!

my_str[0] = 'y'  # RAISES ERROR, ALL HELL BREAKS LOOSE
my_list[0] = 3   # perfectly okay!
```

**6. Is there a way to quickly unpack multiple list/tuple values?**

Yep! This was a relatively recent Python addition, actually.

```python
def example(a, b, c, d, e, f):
    print(a, b, c, d, e, f, sep='')

my_list = [1, 2, 3, 4, 5, 6]

# you use the asterisk symbol before the variable, it 
# will unpack each value in order (so for this example,
# it would be unpacked as a=1, b=2, c=3, etc.)
example(*my_list)

print("{}{}{}{}{}{}".format(*my_list))  # also convenient for filling up format-strings
```

**7. How do you sort a dictionary by key?**

```python
from operator import itemgetter

my_dict = {'c': 3, 'a': 1, 'd': 4, 'b': 2}

sorted_dict = dict(sorted(my_dict.items(), key=itemgetter(0)))

print(sorted_dict)
```
Out:
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

**8. How do you sort a dictionary by value?**

```python
from operator import itemgetter

my_dict = {'c': 3, 'a': 1, 'd': 4, 'b': 2}

sorted_dict = dict(sorted(my_dict.items(), key=itemgetter(1)))

print(sorted_dict)
```
Out:
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

**9. How do you reverse the sorting order of `.sort()` or `sorted()`?**

You can supply `True` to the `reverse` parameter. 

```python
my_list = [1, 2, 3, 4]

my_list.sort(reverse=True)

print(my_list)
```
Out:
```
[4, 3, 2, 1]
```

**10. What is the difference between `.sort()` and `sorted()`?**

`.sort()` is an in-place `list` method function. 

`sorted()` is a generic function that returns a sorted `list` copy of the given iterable.

**11. Is there a way to assign multiple variables to the same value in one line?**

Yes, but I don't recommend doing this. It's much better to put assignments on subsequent lines for readability. 

```python
a, b, c = 0, 0, 0

a = b = c = 0

a = 0; b = 0; c = 0
```

**12. Can you iterate through multiple collections at once?**

Yes, you can with the `zip()` function. 

```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [3.14, 2.718, 9.8]

for aval, bval, cval in zip(a, b, c):
    print(aval, bval, cval)
```
Out:
```
1 a 3.14
2 b 2.718
3 c 9.8
```

**13. What is `self`?**

`self`, in technical terms, is a _reference_ to the class instantiation. User-defined classes are, by default, _mutable_ types — and so the class needs a way to refer back to what it contains. 

```python
# let's say we have a simple Vector class
class Vector(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def mag(self):
        return (x**2 + y**2)**(1/2)

    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)

# on instantiation, think of the parameter mapping as:
# Vector(self=Vector, x=1, y=2)
v = Vector(1, 2)

# for methods, think of self as being called by the instance being acted on:  
# mag(self=v)
m = v.mag()
```

I know how different it is from what we've become accustomed to, so this is a way of _thinking_ about the mapping of parameters when dealing with a class. It might not necessarily be what's happening behind the scenes.


## Academic Dishonesty Reports

**1. Do you know who has received an academic dishonesty report?**

No, unless the student tells me (you don't have to by any means). Academic dishonesty reports are kept private between the professors and the student in question, unless the TA was involved to some capacity.

I have caught plagiarizing students myself, however. I browse through at least one hundred projects every week (all of the section's + students on Piazza), I will occasionally spot similar solutions. 

**2. Have you had students in your section recieve academic dishonesty reports?**

Oh yes, many. It saddens me when it happens — it feels like a failure on my part, which is why I stress doing your own work so much. I tend to have students that are very open with me, and so I'm aware of almost everyone in my past sections who has received one. I wish I could've stopped them, but it's always too late 🤷

**3. What should I do if I receive an academic dishonesty report?**

You can either take the punishment or appeal. Convictions are usually made with strong evidence, however. I frankly don't know much about the ADR process, so I would visit the Office of the University Ombudsperson [website](https://ombud.msu.edu). 


## Miscellaneous/Personal

**1. I'm a [major that's not computer science/engineering], will I ever need this?** 

Probably, yeah. Programming is becoming more and more important everyday, to the point where most engineering fields use it to some capacity. Most engineering majors at MSU have to take a MatLab or R course at some point. After going through this class, they should be easy.

**2. Can I forward your emails to my friend in [some other section]?**

Yes, you may. Though you should warn them that some details I may mention are TA-dependent (e.g. when project/lab grades come back, when D2L gets updated, and anything related to this GitHub repository).

**3. Can my friends in [some other section] use this GitHub repository too?**

Yes, but the course schedule on the home README will only reflect our section's meeting days, they'll have to keep this in mind.

**4. How does this repository automatically stay up-to-date with the course website?**

There are Python modules that allow you to [web scrape](https://en.m.wikipedia.org/wiki/Web_scraping), (collect data from websites). The code that keeps this page up-to-date does a few things: it updates the course schedule, syllabus, home README, and all lab/project files. The update script can be found in /assets/update.py.

The syllabus and home README have templates that you can find in /assets/templates/. There are "variables" encoded into the documents (words surrounded by colons like :this:) that my program simply finds and replaces with the proper information (like year, semester, location, etc.). Lab and project folders have their own README files, these are also updated via templates in a similar fashion.

The course schedule on the home README literally has its HTML code (the code that displays the schedule) ripped straight from Dr. Enbody's website (the Due Dates page, specifically). My code disassembles the HTML and re-constructs it with links, standardized formatting, and hover text. It's like a program that writes a program in a way.

For project files, I noticed that Dr. Enbody would keep the URL of the project domains consistent, (like it would always be /projects/Project01/, /projects/Project02/, etc.), I used this to my advantage. A template URL with a missing project number is kept as a constant within the program, where a for-loop then iterates through numbers to fill the gap. The program then web-scrapes all the links from the page, and downloads each file if the domain exists. If the domain doesn't exist yet, no folder on the GitHub page is created. 

**5. How does the progress bar work?**

The number of days in the semester is calculated from dates that I feed it, we'll call this `N`. The program also extracts the date that it's currently running at, we'll call this little `n`. The percentage of completion can then be calculated as `1 - (n / N)`, we'll call this `p`.

There are three attributes to the progress bar: a width (14, at the time of writing. Was chosen so that it will display properly on most devices), a fill character (⬛, the black square emoji), and an empty character (⬜, the white square emoji). 

The number of fill characters we need will be `p` (the percentage of completion) multiplied by the width, [floored](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) — i.e. the number that is `p` percent of the width. We floor this value because the number of fill characters can't be a decimal number, and we don't round because a value like 0.95 could be interpreted as 100%, which could be misleading. 

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

**6. What are those small messages that appear next to file names?**

[Commit messages](https://en.wikipedia.org/wiki/Commit_(version_control)). Whenever I make changes to the repository, one of the common version control practices is to describe what you, as the committer, changed. I keep them extremely brief since I'm the only one working on the repository. You can ignore them, they're more for my sake. 

**7. What is the ".md" file extension that you use?**

[Markdown](https://en.wikipedia.org/wiki/Markdown). They're kinda like text files, but will convert all text into HTML script internally. I use them because they're easy to write, and allow for extensive formatting. 

**8. What is the ".json" file extension that you use?**

[JavaScript Object Notation](https://en.wikipedia.org/wiki/JSON). They're text files that store JavaScript object data, but most programming languages (like Python) have libraries that can read them. I use them because they're easy to read/write.

**9. How did you prepare for CSE231 exams?**

I went through the past exams and took them as if they were the real deal — timer and all. I went back through questions I got wrong with PythonTutor, and asked about ones I didn't understand on Piazza. 

Come exam day, I drank a ludicrous amount of coffee... though I don't recommend doing that. Drink coffee safely, [studies](https://link.springer.com/article/10.1007/s12603-014-0563-8) have shown that caffeine does indeed improve cognitive function. 

**10. Do you know any other programming languages?**

C, C++, and JavaScript. I use Python the most, however.

**11. Does the programming language you use in the real-world matter?**

Yes, but not in the way you might expect. The language you should use is dependent on what you're doing. Some languages will be better at one thing, and some languages will be better at another thing.

For example, if you're making a desktop application, or need hyper-fast arithmetic, you'll want C or C++. If you're doing anything web-related, then you'll definitely be working with JavaScript (or TypeScript as of late). Python or Java can be used for *pretty much* everything else, though Java is mostly being phased out in favor of Python. 

If you're interested in data science, machine learning, cybersecurity, or research, Python is a great option. 

**12. What code editor do you use?**

[Visual Studio Code](https://code.visualstudio.com). My installation may look slightly different because I have custom theme. I use "One Dark Pro", which you can find in the extensions marketplace.

**13. How do you type so fast?**

Too much time spent writing essays in an IB high school. 

**14. Where can I apply to become a ULA for this course?**

[Here](https://www.cse.msu.edu/Resources/EmploymentStudents.php). I had to finish CSE232 before Dr. Enbody would hire me for CSE231, I'm unsure if that rule still applies. I'm sure other professors have restrictions like that, if you're looking to become a ULA for another course.

**15. Do you need a 4.0 to become a ULA for this class?**

Maybe? I actually have no idea, that'd be a good question for Dr. Enbody. If I had to guess, I'd say 3.5-4.0. Maybe 3.0 if you answer questions on Piazza frequently. You should still answer questions on Piazza even if you're in good standing grade-wise, it'll show that you're eager to help others. 

**16. Do you need to be a CSE major to become a ULA for this class?**

No, but Dr. Enbody probably wants you to be comfortable with programming in general. 

**17. How much do you get paid?**

$11/hour, though MSU had to reduce everyone's wage a little because of COVID-19.

**18. Can you give me a referral?**

If I don't know you that well, then my answer is _probably_ no. If I think your performance in the course is noteworthy, and you have some experience to back it up, then get in touch — you might change my mind. 

I know that sounds pretentious of me, but the last thing I'd want to do is give a professor someone that just has no idea what they're doing.
