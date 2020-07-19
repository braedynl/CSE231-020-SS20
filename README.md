# CSE231 - Introduction to Programming I
This repository is for CSE231 - Introduction to Programming I, Section TBA for Fall 2020 at Michigan State University. It includes all presentations and example code used during my in-class lab. This README file also acts as a hub for everything you'll need in this course. You can use this instead of the main website if you so choose.

Main Course Website: https://web.cse.msu.edu/~cse231/

Logistics:
  - [Coding Standard](CODINGSTANDARD.md)
  - [Contact Information](#contact-information)
  - [Course Schedule](#course-schedule)
  - [Exam Information](SYLLABUS.md#exams)
  - [Help Room Schedule](https://web.cse.msu.edu/~cse231/Online/General/ta.consulting.SS20.html)
  - [Honors](https://web.cse.msu.edu/~cse231/Online/Honors/)
  - [Lab Schedule](https://www.cse.msu.edu/~cse231/Online/General/schedule.labs.SS20.html)
  - [Section Information](#section-information)
  - [Syllabus](SYLLABUS.md)
  - [Textbook](https://www.pearson.com/us/higher-education/product/Punch-Practice-of-Computing-Using-Python-The-3rd-Edition/9780134379760.html)
  - [Traditional Lab Slides](https://web.cse.msu.edu/~cse231/Online/mini-lectures/)

Essential Sites:
  - [D2L](https://d2l.msu.edu/d2l/home)
  - [Mimir](https://class.mimir.io/)
  - [Piazza](https://piazza.com/)
  - [Zoom](https://msu.zoom.us/meeting) (if online)
  - [Discord](https://discord.com/new) (if summer semester)

Help:
  - [Contact Information](#contact-information)
  - [Debugging Guide](https://www.cse.msu.edu/~cse231/Online/debugging.pdf)
  - [Dr. Enbody's Exam-Taking Talk](https://www.youtube.com/watch?v=rLopE19HjTY&feature=youtu.be)
  - [FAQ](https://web.cse.msu.edu/~cse231/Online/General/FAQ.html)
  - [General Tips](#general-tips)
  - [Help Room Schedule](https://web.cse.msu.edu/~cse231/Online/General/ta.consulting.SS20.html)
  - [Past Exams](https://web.cse.msu.edu/~cse231/Online/Exams/)
  - [Piazza](https://piazza.com/)
  - [PythonTutor](http://pythontutor.com/)

Extra:
  - [Past Projects](https://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/)
  - [Performance Statistics](https://msugrades.com/course/CSE/231/RICHARD_J_ENBODY)

## Getting Started

[Download/Install Anaconda (comes packaged with Spyder) and Python 3.7 or higher](https://www.anaconda.com/products/individual). Further instructions are in [Lab 00](Lab%2000). There is also [a video](https://www.youtube.com/watch?v=_CqtctVJZnk&feature=youtu.be) if Lab 00 isn't working out for you.  

You are permitted to install other code editors if you so choose, though bear in mind that the TAs and professors may not be familiar with how some of them work, you'll be on your own if you need help with it. I (Braedyn) almost exclusively work with [Visual Studio Code](https://code.visualstudio.com/), though I am familiar with Spyder.

Other popular code editors:
- [Atom](https://atom.io/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Sublime Text](https://www.sublimetext.com/)
- [Xcode](https://developer.apple.com/xcode/) (MacOS only)

Certain projects pull from 3rd party libraries closer to the end of the semester, (namely `pylab` and `pandas`) -- Anaconda comes packaged with these. If you are using a different code editor, contact me, and I'll show you how to install them manually if you couldn't figure out how to do it by yourself.

The TA lectures and the lecture videos by Dr. Punch are _supplemental_ to the textbook. You can purchase the textbook [here](https://www.pearsonhighered.com/product/Punch-Practice-of-Computing-Using-Python-The-3rd-Edition/9780134379760.html).
- ISBN-13: 9780134379760 (or 9780134380315) 
    - Other ISBN-13 numbers are website-only, or are bundled with extraneous materials.
- Several copies are available in the Course Reserves at the MSU Main Library.
- A draft of chapters 0 and 1 can be found [here](https://www.cse.msu.edu/~cse231/Online/chapter0_and_1.pdf) if you're waiting for shipment. 

All lab and project materials can be found in the "Code" section of this repository. You can find my presentations and example code in path /Lab XX/presentation/, where "XX" is the lab number. You can find Mimir test-case explanations and Spyder keyboard shortcuts in any of the [project folder READMEs](Project%2001/README.md). The assets folder is purely for my own purposes, you can ignore it. 

Read through [the syllabus](SYLLABUS.md) if you haven't already. Your co-pilot on this expedition through CSE231 will be the course schedule, which is down below. I have programs that keep it (and everything else on this repository) up-to-date with the main course website, though my schedule is better because it has links. :grin:

## Course Schedule

Below is the course schedule, your guide to being successful this semester. The assignments listed provide links to the corresponding website they are hosted on. Reading the book chapters and watching the lecture videos can be done at any point during the week, though it's probably a good idea to do it before coming to lab and starting the assignments. You can hover over the assignment's text to see its precise due date (sorry mobile users). It should be assumed that all assignments are due by 11:59 PM EST on their respective days, unless specified otherwise. 

If this section is in-person: labs are *not* homework assignments, they must be done in-class. 

If this section is online: labs may be treated as homework assignments. This rule also applies if there are no in-person meetings due to COVID-19, even if your section would be considered in-person by tradition. 

**Project and lab submissions are on Mimir. The project/lab links provided bring you to the procedure and starter-code. For projects, the introductory videos are included in the subdirectory's README.**

<table>
<thead>
<tr>
<th>Week</th>
<th>Sun</th>
<th>Mon</th>
<th>Tue</th>
<th>Fri</th>
<th>Sat</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">00: 08/30</td>
<td><a title="Sunday, August 30th (8/30/2020)" href="https://www.cse.msu.edu/~cse231/Online/week0.html">Read Ch. 0; Videos: Welcome, Getting Python</a></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"><a title="Friday, September 4th (9/4/2020)" href="Lab%2000">Lab 00</a></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">01: 09/06</td>
<td><a title="Sunday, September 6th (9/6/2020)" href="https://www.cse.msu.edu/~cse231/Online/beginnings.html">Read Ch. 1; Videos: Beginnings</a></td>
<td align="center"></td>
<td align="center"></td>
<td align="center"><a title="Friday, September 11th (9/11/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 01</a>/<a title="Friday, September 11th (9/11/2020)" href="Lab%2001">Lab 01</a></td>
<td align="center"><a title="Saturday, September 12th (9/12/2020)" href="https://class.mimir.io">Exercises: Ch. 01</a></td>
</tr>
<tr>
<td align="center">02: 09/13</td>
<td><a title="Sunday, September 13th (9/13/2020)" href="https://www.cse.msu.edu/~cse231/Online/control.html">Read Ch. 2; Videos: Control</a></td>
<td align="center"><a title="Monday, September 14th (9/14/2020)" href="Project%2001">Project 01</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, September 18th (9/18/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 02</a>/<a title="Friday, September 18th (9/18/2020)" href="Lab%2002">Lab 02</a></td>
<td align="center"><a title="Saturday, September 19th (9/19/2020)" href="https://class.mimir.io">Exercises: Ch. 02</a></td>
</tr>
<tr>
<td align="center">03: 09/20</td>
<td><a title="Sunday, September 20th (9/20/2020)" href="https://www.cse.msu.edu/~cse231/Online/strings.html">Read Ch. 4; Videos: Strings</a></td>
<td align="center"><a title="Monday, September 21st (9/21/2020)" href="Project%2002">Project 02</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, September 25th (9/25/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 03</a>/<a title="Friday, September 25th (9/25/2020)" href="Lab%2003">Lab 03</a></td>
<td align="center"><a title="Saturday, September 26th (9/26/2020)" href="https://class.mimir.io">Exercises: Ch. 04</a></td>
</tr>
<tr>
<td align="center">04: 09/27</td>
<td><a title="Sunday, September 27th (9/27/2020)" href="https://www.cse.msu.edu/~cse231/Online/functions.html">Read Ch. 5; Videos: Functions</a></td>
<td align="center"><a title="Monday, September 28th (9/28/2020)" href="Project%2003">Project 03</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, October 2nd (10/2/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 04</a>/<a title="Friday, October 2nd (10/2/2020)" href="Lab%2004">Lab 04</a></td>
<td align="center"><a title="Saturday, October 3rd (10/3/2020)" href="https://class.mimir.io">Exercises: Ch. 05</a></td>
</tr>
<tr>
<td align="center">05: 10/04</td>
<td><a title="Sunday, October 4th (10/4/2020)" href="https://www.cse.msu.edu/~cse231/Online/files1.html">Read Ch. 6; Videos: Files & Exceptions 1</a></td>
<td align="center"></td>
<td align="center"><div title="Tuesday, October 6th (10/6/2020)">Exam 1</div></td>
<td align="center"><a title="Friday, October 9th (10/9/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 05</a>/<a title="Friday, October 9th (10/9/2020)" href="Lab%2005">Lab 05</a></td>
<td align="center"><a title="Saturday, October 10th (10/10/2020)" href="https://class.mimir.io">Exercises: Ch. 06</a></td>
</tr>
<tr>
<td align="center">06: 10/11</td>
<td><a title="Sunday, October 11th (10/11/2020)" href="https://www.cse.msu.edu/~cse231/Online/lists.html">Read Ch. 7; Videos: Lists & Tuples</a></td>
<td align="center"><a title="Monday, October 12th (10/12/2020)" href="Project%2004">Project 04</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, October 16th (10/16/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 06</a>/<a title="Friday, October 16th (10/16/2020)" href="Lab%2006">Lab 06</a></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">07: 10/18</td>
<td><a title="Sunday, October 18th (10/18/2020)" href="https://www.cse.msu.edu/~cse231/Online/algorithms.html">Read Ch. 3; Algorithms</a></td>
<td align="center"><a title="Monday, October 19th (10/19/2020)" href="Project%2005">Project 05</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, October 23rd (10/23/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 07</a>/<a title="Friday, October 23rd (10/23/2020)" href="Lab%2007">Lab 07</a></td>
<td align="center"><a title="Saturday, October 24th (10/24/2020)" href="https://class.mimir.io">Exercises: Ch. 07</a></td>
</tr>
<tr>
<td align="center">08: 10/25</td>
<td><a title="Sunday, October 25th (10/25/2020)" href="https://www.cse.msu.edu/~cse231/Online/dictionaries.html">Read Ch. 9; Videos: Dictionaries & Sets</a></td>
<td align="center"><a title="Monday, October 26th (10/26/2020)" href="Project%2006">Project 06</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, October 30th (10/30/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 08</a>/<a title="Friday, October 30th (10/30/2020)" href="Lab%2008">Lab 08</a></td>
</tr>
<tr>
<td align="center">09: 11/01</td>
<td><a title="Sunday, November 1st (11/1/2020)" href="https://www.cse.msu.edu/~cse231/Online/functionsII.html">Read Ch. 8; Videos: More Functions</a></td>
<td align="center"><a title="Monday, November 2nd (11/2/2020)" href="Project%2007">Project 07</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, November 6th (11/6/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 09</a>/<a title="Friday, November 6th (11/6/2020)" href="Lab%2009">Lab 09</a></td>
<td align="center"><a title="Saturday, November 7th (11/7/2020)" href="https://class.mimir.io">Exercises: Ch. 08 and 09</a></td>
</tr>
<tr>
<td align="center">10: 11/08</td>
<td><a title="Sunday, November 8th (11/8/2020)" href="https://www.cse.msu.edu/~cse231/Online/program_development.html">Read Ch. 10 Program Development</a></td>
<td align="center"></td>
<td align="center"><div title="Tuesday, November 10th (11/10/2020)">Exam 2</div></td>
<td align="center"><a title="Friday, November 13th (11/13/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 10</a>/<a title="Friday, November 13th (11/13/2020)" href="Lab%2010">Lab 10</a></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">11: 11/15</td>
<td><a title="Sunday, November 15th (11/15/2020)" href="https://www.cse.msu.edu/~cse231/Online/classesI.html">Read Ch. 11; Videos: Classes I</a></td>
<td align="center"><a title="Monday, November 16th (11/16/2020)" href="Project%2008">Project 08</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, November 20th (11/20/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 11</a>/<a title="Friday, November 20th (11/20/2020)" href="Lab%2011">Lab 11</a></td>
<td align="center"><a title="Saturday, November 21st (11/21/2020)" href="https://class.mimir.io">Exercises: Ch. 11</a></td>
</tr>
<tr>
<td align="center">12: 11/22</td>
<td><a title="Sunday, November 22nd (11/22/2020)" href="https://www.cse.msu.edu/~cse231/Online/scope.html">Read Ch. 12; Videos: More on Classes</a></td>
<td align="center"><a title="Monday, November 23rd (11/23/2020)" href="Project%2009">Project 09</a></td>
<td align="center"></td>
<td align="center"><div title="Friday, November 27th (11/27/2020)">Thanksgiving</div></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">13: 11/29</td>
<td><a title="Sunday, November 29th (11/29/2020)" href="https://www.cse.msu.edu/~cse231/Online/classesII.html">Read Section 9.6; Videos: Scope</a></td>
<td align="center"></td>
<td align="center"><a title="Tuesday, December 1st (12/1/2020)" href="Project%2010">Project 10</a></td>
<td align="center"><a title="Friday, December 4th (12/4/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 12</a>/<a title="Friday, December 4th (12/4/2020)" href="Lab%2012">Lab 12</a></td>
<td align="center"><a title="Saturday, December 5th (12/5/2020)" href="https://class.mimir.io">Exercises: Ch. 12</a></td>
</tr>
<tr>
<td align="center">14: 12/06</td>
<td><a title="Sunday, December 6th (12/6/2020)" href="https://www.cse.msu.edu/~cse231/Online/exceptions.html">Read Ch. 14; More Files & Exceptions</a></td>
<td align="center"><a title="Monday, December 7th (12/7/2020)" href="Project%2011">Project 11</a></td>
<td align="center"></td>
<td align="center"><a title="Friday, December 11th (12/11/2020)" href="https://d2l.msu.edu/d2l/loginh/">Pre-Lab 13</a>/<a title="Friday, December 11th (12/11/2020)" href="Lab%2013">Lab 13</a></td>
<td align="center"></td>
</tr>
</tbody>
</table>


The schedule is taken directly from the [course schedule](https://web.cse.msu.edu/~cse231/Online/due_dates.html) on the main website. If there are any descrepancies between the two, [please notify me immediately](#braedyn-lettinga).

Links to Mimir and D2L assignments are not direct because a login is requried.

## Section Information

Leading Professors: Dr. Enbody / Dr. Zaabar

Section Instructor: Braedyn Lettinga

Section: TBA

Location/Time: Online at TBA

## Contact Information

### Dr. Enbody

Email: enbody@cse.msu.edu

Website: https://www.cse.msu.edu/~enbody/

Office: [Engineering Building (EB), Room 3145](https://www.google.com/maps/place/Engineering+Building/@42.7249397,-84.4835239,17z/data=!3m1!4b1!4m5!3m4!1s0x8822c27d94c0dddf:0x5bad697ea8a8837c!8m2!3d42.7249358!4d-84.4813352)

Office Hours: Find an available timeslot on [Dr. Enbody's calendar](https://calendar.google.com/calendar/embed?src=enbody@gmail.com&ctz=America/New_York) and send an email to him requesting for that time.

### Dr. Zaabar

Email: zaabarim@cse.msu.edu

Office: [Engineering Building (EB), Room 3581](https://www.google.com/maps/place/Engineering+Building/@42.7249397,-84.4835239,17z/data=!3m1!4b1!4m5!3m4!1s0x8822c27d94c0dddf:0x5bad697ea8a8837c!8m2!3d42.7249358!4d-84.4813352)

Office Hours: Find an available timeslot on [Dr. Zaabar's calendar](https://calendar.google.com/calendar/embed?src=imenzaabar7%40gmail.com&ctz=America%2FDetroit) and send an email to her requesting for that time.

### Braedyn Lettinga

Email: letting4@msu.edu

Website: https://github.com/braedynl

I sadly don't have an office or office hours since I'm a measly and pitiful ULA. I do, however, meet with students on a regular basis. Send me an email requesting a time and means of communication (in-person, Zoom, Discord, etc.), and I'll get back to you as soon as I can. 

I will occasionally host help rooms of my own when I feel it to be necessary. This is dependent on how well the section is doing as a whole, however. 

Contact **me** with questions regarding most grades. I am the one that grades your labs and projects, not the professors. Chapter exercises and exam grades are based solely on the test cases (exams are conducted through Mimir if course is online), I play no role in grading them. 

If this is a summer semester: I will be sending out an email during the first week in regards to a Discord server for the section. The link to join said server will be in that email, and will not be posted on this page for sake of course privacy. I only host Discord servers for the summer sections, since the summer version of this course is harder. I would prefer student messages through Discord, since writing code in an email is glitchy.

## General Tips

**Start projects early, I cannot stress this enough.**
Sometimes, you might be faced with a problem that you just have no idea how to implement an algorithm for. Simply taking a break and doing something else for a bit can seriously help. This also gives you time to get answers to questions you might have.

**Take it slow.** Rushing through the coding process is bound to cause issues. You should always test as you're writing, as described by the points below. 

**Always, always, always test your code as you're writing it.** Ensure that, every step of the way, you're writing a chunk or line that is doing what you're expecting it to do. Using `print()` or the debugger is good for this. 

**Talk with your friends/acquaintances.** If you can't figure out how to code something, discuss an algorithm or write pseudocode with your buds. Remember that you **cannot**, under any circumstance, share code for the projects. Even _looking_ at another person's implementation of a solution may lead you to do something similar. Simply _talking_ with another student about a project is fine. Everything else in this course is fair game to be collaborated on. Visit the [Office of the University Ombudsperson website about ADR](https://ombud.msu.edu) for more details on plaigarism.

**Take advantage of Piazza and the help room.** These are two amazing resources to use if you're having trouble with your code. You can ask questions anonymously on Piazza and get quick responses from other students and/or instructors.

**Use your IDE's debugger.** The debugger is an incredible tool that executes your code line-by-line. We'll be covering how to use the debugger during lab 2. Feel free to look into it on your own time as well. 

**When in doubt, `print()` it out.** Certainly the most classic of all the options. Print your variables out at certain points in your code to see where things went sour.

**Try [PythonTutor](http://pythontutor.com/)!** PythonTutor visualizes your code, and gives execution control similar to an IDE debugger.
