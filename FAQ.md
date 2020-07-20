# FAQ

Frequent student questions that I've been collecting over the years. If the answer to your question ain't in here, I'd be surprised. 

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

**5. Are there any exceptions for close final course grade cut-offs?**

Yes, actually. The professors will look for students who are at the edge of grade boundaries when the semester is over. They are stingier with rounding 4.0s, however. 

**6. Are there any extra credit assignments?**

_Sometimes_. I'm not sure when they happen, or for what reason. To me, it seems like it's just whenever Dr. Enbody feels like throwin one out. All instances where extra credit _has_ been served have been small, so don't get your hopes up.


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


## Miscellaneous/Personal

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

Fun fact: CSE231 used to teach C++

**2. I'm a [major that's not computer science/engineering], will I ever need this?** 

Probably, yeah. Programming is becoming more and more important everyday, to the point where most engineering fields use it to some capacity. The power in programming is its ability to manipulate, and calculate values almost instantaneously in tandem with logic. The phone in your pocket, the stock market, the digital alarm clock on your desk -- all of these wouldn't exist without programming.  

**3. Are we allowed to use a code editor that's not Spyder?**

Yep! Though bear in mind that the TAs and professors may not be familiar with how some of them work, you'll be on your own if you need help with it.

Other popular code editors:
- [Atom](https://atom.io/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Sublime Text](https://www.sublimetext.com/)
- [Visual Studio Code](https://code.visualstudio.com) (Made by Microsoft, what I use)
- [Xcode](https://developer.apple.com/xcode/) (Made by Apple, MacOS only)

Certain projects pull from 3rd party libraries near the end of the semester, (namely `pylab`), Spyder comes packaged with it, which is why we use Spyder in the first place. You'll have to manually install `pylab` if you're on a different code editor, which I can show you how to do if you can't figure it out for yourself.

**4. Why are the online exams proctored? That's so stupid.**

It *is* stupid, isn't it? You can ask the students who took this course in Spring 2020 for that answer.

Spoiler: everyone cheated when we didn't proctor. 

**5. Are there exam statistics anywhere?**

Dr. Enbody will have them in his post-exam email.

**6. Can I forward your emails to my friends in other sections?**

Yes, you may. Though you should warn them that some details I may mention are TA-dependent (e.g. when project/lab grades come back, when D2L gets updated, and anything related to this GitHub repository).

**7. Can my friends in [some other section] use this GitHub repository too?**

Yes, but the course schedule on the main README will only reflect our section's meeting days, they'll have to keep this in mind.

**8. Why do you go through the effort to do all of this?**

Well I didn't really like Dr. Enbody's website when I took the class myself. When I became a TA, making a GitHub page started out as a way to store my mini-lecture presentations, but then it kind of snowballed into a fully-fledged course page as I kept adding more stuff.

In terms of "my thoroughness", (which gets talked about a lot by students who have me), I believe all TAs should be just as thorough. My job, from my perspective, is to make this class a much easier and enjoyable experience for students. I want to ensure that you know where to go, who to contact, and how to get help.

**9. How did you prepare for CSE231 exams?**

I went through the past exams and took them as if they were the real deal -- timer and all. I went back through questions I got wrong with PythonTutor, and asked about ones I didn't understand on Piazza. 

Come exam day, I drank a ludicrous amount of coffee... though I don't recommend doing that. Drink coffee safely, [studies](https://link.springer.com/article/10.1007/s12603-014-0563-8) have shown that caffeine does indeed improve cognitive function. 

**10. How did you do when you took this class?**

I got a 4.0, but I'm not smart by any means -- I just have _a lot_ of practice because I've been programming since I was a kid. If you're having a hard time, please don't compare your situation to people like me, because it's not the same. Programming is an extremely hard skill to master for a majority of people. The biggest thing you can do is practice. 

**11. Did you read the book?**

Nope, not a single word of it. But, again, I've been programming for a long time. Programming languages just kinda come naturally after you learn one (I knew a little Java before CSE231). I just used Piazza or did a quick Google search when I needed help with something.  

**12. Is using w3schools.com and/or programiz.com okay as supplementary material?**

Yep! Just be careful, websites like those may teach certain concepts in a different order, or may show some concepts that we don't teach at all. If you do come across something that we don't teach, it's usually safe to assume that you're not allowed to use it. If you're unsure if a concept may be used in an assignment, feel free to ask on Piazza.

**13. Do you use tabs or spaces?**

Tabs, I'm not tryna demolish my spacebar.

**14. Do you know any other programming languages?**

C, C++, JavaScript, and a minuscule amount of Java. I definitely use Python the most, however (you can tell if you look at my GitHub projects lol).

**15. Does the language you use in the real world matter?**

Kind of, it depends on what you're doing. If you're making a desktop application, or need hyper-fast arithmetic, you'll want C or C++. If you're doing anything web-related, then JavaScript is, and will always be, the industry standard -- you should definitely learn JavaScript at some point if you're a CSE major, you're going to need it. Python/Java can be used for everything else, though Java is mostly being phased out in favor of Python. 

If you're interested in data science, machine learning, ethical hacking, web-scraping, or academic research, Python is your go-to (not a complete list). 

**16. What is your ethnic background?**

I'm half white, half Korean. 

**17. Where are you from?**

Grand Rapids, Michigan. 

**18. Do you have social media?**

Hardly. I have a Twitter and a Snapchat, but I'm rarely ever on my phone in the first place. Talk with me if you want to add me. 

**19. What code editor do you use?**

[Visual Studio Code](https://code.visualstudio.com).

**20. How do you type so fast?**

Too much time spent writing essays in an IB high school. 

**21. Where can I apply to become a ULA for a CSE course?**

[Here](https://www.cse.msu.edu/Resources/EmploymentStudents.php). I had to finish CSE232 before Dr. Enbody would hire me for CSE231, I'm unsure if that rule still applies. 

**22. Do you need a 4.0 to become a ULA for this class?**

Maybe? I actually have no idea, that'd be a good question for Dr. Enbody. If I had to guess, I'd say 3.5-4.0. Maybe 3.0 if you answer questions on Piazza frequently. You should still answer questions on Piazza even if you're in good standing grade-wise, it'll show that you're eager to help others. 

**23. Do you need to be a CSE major to become a ULA for this class?**

No, but Dr. Enbody probably wants you to be comfortable with programming in general. 

**24. How much do you get paid?**

$11/hour, though MSU had to reduce everyone's wage a little because of COVID-19 -- I'm not sure by how much for me, personally. I didn't take this job for the money. 

**25. Can you give me a referral?**

If I think you got what it takes, then maybe. Contact me about it. 
