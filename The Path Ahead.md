If you're reading this, that means you're a computer science major/minor, or you're just interested in computational study areas. I want to do two things. One; provide a transition to your (likely) next pair of classes, CSE232 and CSE260, and two; discuss where you'll be going, and what I recommend you do to prepare for the future.

## CSE232 / What's wrong with Python?

For as amazing of a programming language that Python is, it has problems. All programming languages have their strengths and drawbacks, and Python is no exception. What differentiates Python from the rest?

You might've read online somewhere that Python is "slow" and "high-level". Basically, (and you'll learn a lot more about this in future courses), the further your language strays away from the binary that your computer is actually reading, the more work your computer has to do to translate everything into that binary set of instructions, effectively making the language "slower" to read for the computer.

In CSE232, you'll be working alongside this thing called a *compiler*. It's essentially a small program that takes your C++ code, and translates it straight from C++ to machine code. That machine code gets translated into binary, and then your computer does a thing. Python has to go through a program called an *interpreter*, which then gets put into a *compiler*, which then translates into machine code, and *then* binary. We don't ever see the interpreter because the process is done automatically by your code editor. C++ likes to be a pain, and so you'll have to compile on your own.

The advantage to this, however, is *speed*. This is why you'll pretty commonly see video games developed in C++. C++ is low-level, you're able to do a lot of things with your computer that Python never could. You can manipulate the amount of memory taken up by a variable/class, you can reroute memory allocations, etc.. C++ is also *statically-typed*, meaning that variables must have their types explicitly stated whenever you create one. To declare an `int` in Python, we would say:

```
a = 1
```

While in C++, you unfortunately have to say...

```
int a = 1
```

This is another reason why C++ is so fast. The Python interpreter has to figure out what type you declared, while C++'s compiler knows just from looking at the keyword before your variable. And so hopefully it makes sense as to why video games are developed in C++. Video games need to make hundreds, if not thousands of calculations per second. You might have physics, lighting simulations, player events to keep track of, etc..  

With all of that being said though, Python is becoming increasingly popular among companies for things that don't require that kind of fast arithmetic. Most of the time, you just need to run a simple simulation, store user data, graph something -- whatever company time you lose in execution-time, you make up for in write-time.

Low-level languages like C++ tend to be hard to read and write. The error messages are extremely vague, and the syntax is horribly unforgiving. Most non-video game companies stay away from lower-level languages because there's so much time spent debugging and writing. Unless, of course, they have a particular reason for using a lower-level language. 

We teach you Python first so that it will be easier to make the transition into harder languages like this. You'll find that a majority of the concepts are the same as in Python, while the syntax varies.  

## CSE260 / What are these algorithms really doing?

Next to CSE232, you'll likely be taking CSE260 sometime soon. This class discusses the mathematics behind the code we write. Because, really, every line you write in code is a mathematical expression. It's just that, when you write something like `print("Hello, world!")`, the language has abstracted all of the mathematics so far away from you that, all you must do as the programmer, is type the word "print" with some parentheses at the end.

A hugely important topic you'll also discuss is algorithmic time. Essentially the amount of steps your algorithm takes to get a certain task done. When you go through 232 and 260, you'll come back to these old projects and cringe at your algorithms. Everyone does lol.

## The Path Ahead

It's been a long journey, and I'm sure you're all sick of me by now. But I would assume that since you're interested in computational studies, you might want to know your options. Don't think that you're constrained to only become a software engineer, because that's just one branch out of *hundreds* you could go down. Let's take a brief look at some of the most popular ones at the moment.

### Software Engineering / Web Development

Of course, we still have to talk about software engineering. It's by far the most popular domain within the field, and involves the least amount of math. It's a great domain to be in, because you get to not only design the inner-workings of your software, but you can design *how* you want the user to interact with your program.

Nowadays, the term "software engineering" has become almost synonymous with web development. It's pretty rare to see posting for non-web app jobs, and so I would prioritize learning the "web development essentials" as I call them: JavaScript, HTML and CSS. 

JavaScript is the "language of the browser", and is fairly similar to Python, so it should be easy to pick up. HTML is a markup language that provides structure to your website interface, while CSS builds on top of HTML to make the website look pretty.

These three languages make up what's commonly referred to as the "front end" of software engineering. You'll commonly see Python/Java make up the "back end", languages that can better do computation or data management. 

Desktop applications, (like browsers, creation tools, video games), are usually made in C, C++ or Java. Java is a *very* different programming language from JavaScript, by the way. The two are just named similarly.. for whatever reason.

You will be learning a lot of these languages I'm mentioning at some point during your time at MSU, but it's always good to get a head start.

### Cybersecurity

There are two subdomains within cybersecurity: client-side and server-side. 

If we're discussing client-side security (protecting users on their local machine), the best languages for the job would likely be C and/or C++. Operating systems are built-up from the C language family, and so you'll almost always be using a C language when it comes to protecting the operating system and hardware.

With server-side security, the field branches off again. Cryptography is a field within this side of computing, and is the most popular. Your goal is to make algorithms that hide information on a network, while only letting permitted individuals see that information. This is usually done by creating functions that can be accessed one way, but cannot be accessed any other way. This dives into a lot of neat mathematical concepts, a lot of these algorithms use random number generators, the properties of prime numbers, etc.. You would have to know how networks function on a fundamental level, while also (likely) knowing some of the higher level abstractions, like the web development languages and SQL, a common (and very difficult) database management language.

### Data Science

Ayy this is my study area! Data science tends to involve things like machine learning, data engineering, simulations, modeling, etc.. Lucky for you, Python is the main language in this industry due to the simplicity of its syntax.

`pandas`, `matplotlib`, `numpy` and `scipy` are the main suspects you'll see in the field. We learned a little about `pandas` and `matplotlib`, but there's still much more you can do with them that we didn't cover. If you're big into machine learning like I am, `TensorFlow` and `scikit-learn` are the most popular machine learning libraries. Learning what goes *into* machine learning algorithms is an extremely complex topic, and I would recommend jumping in after you've taken linear algebra and multivariable calculus (calc 3). 

And, in case you didn't know, MSU actually has a data science major! It opened up last year, and I've heard nothing but great things about it so far. Even with there being a data science major, however, there are still many data science related courses within the CSE department, since data science originates from computer science. 

## Classes

Me and my friends commonly joke that "computer science is just a math degree with extra steps". In some respects, this is true. While software engineering, the most popular domain, doesn't really require that much mathematical knowledge, pretty much every other domain does. This is why MSU has you take so many math courses. You might not think that these are useful right now, but you will come to appreciate having them eventually. 

These are just recommendations based on what I've heard/read about each class. You might find some others that better suite your interest/academic plan. Bear in mind that some of these courses only appear in the fall or spring semester.

Mathematics: 
- MTH132 Calculus I
- MTH133 Calculus II 
- MTH234 Multivariable Calculus
- MTH314 Matrix Algebra I 
- STT351 Probability and Statistics for Engineering

Sidenote for Mathematics: *all* of these math courses are helpful if you're interested in Data Science. STT351 is likely very helpful if you're into Cybersecurity. 

Software Engineering Recommendations:
- CSE232 Introduction to Programming II
- CSE335 Object-Oriented Software Design
- CSE415 Parallel Programming
- CSE435 Sofware Engineering
- CSE471 Media Processing & Multimedia Computing
- CSE476 Mobile Application Development
- CSE477 Web Application Architecture & Development
- CSE480 Database Systems
- MI349 Web Design and Development
- MI449 Advanced Web Development and Databases

Sidenote for Software Engineering: MI courses? Huh? Yes, there are web development courses in the Media & Information department. I'm unsure if they're to the same rigor as the CSE web development courses (I'll be finding out this upcoming semester), but the advantage to them is that they only require CSE231 as a prerequisite. MI349 then acts as a prerequisite for MI449.

Cybersecurity Recommendations:
- CSE232 Introduction to Programming II
- CSE320 Computer Organization and Architecture
- CSE325 Computer Systems
- CSE410 Operating Systems
- CSE422 Computer Networks
- CSE425 Introduction to Computer Security
- CSE477 Web Application Architecture & Development
- CSE480 Database Systems

Data Science Recommendations:
- CMSE201 Computational Modeling and Data Analysis I
- CMSE202 Computational Modeling and Data Analysis II
- CMSE404/CSE404 Introduction to Machine Learning
- CMSE411 Computational Medicine
- CSE402 Biometrics and Pattern Recognition
- CSE440 Introduction to Artificial Intelligence
- CSE480 Database Systems
- CSE482 Big Data Analysis

Sidenote for Data Science: CMSE404 and CSE404 are the *same class*. It's interdepartmental, i.e. it goes by alternate names depending on the department you're from. You'll have more data science experience coming from CMSE201/2, but you can just as easily learn the material from those classes on your own time, since you'll know a lot more about programming coming from the CSE department (which is why you're able to take a 400-level CMSE course equivalent). Again, data science and computer science are closely related, so there's a lot of department crossover.

For a majority of the courses I listed, you'll likely be taking them during your junior/senior year. It's implied that you've been through CSE320 (Computer Organization and Architecture) and CSE331 (Algorithms and Data Structures), the two *very* useful prerequisite CSE classes. CSE320 is more useful in Cybersecurity (which is why I listed it there) since Cybersecurity may deal more with operating system-level things.

Beyond the 400-level courses, there are the 800-levels. These are mainly intended for graduate students, but you can take them, too, if you speak with an advisor.
- CSE802 Pattern Recognition & Analysis
- CSE803 Computer Vision
- CSE812 Distributed Systems
- CSE813 Advanced VLSI Design
- CSE820 Advanced Computer Architecture
- CSE822 Parallel Computing
- CSE824 Advanced Computer Networks and Communications
- CSE830 Design and Theory of Algorithms
- CSE835 Algorithmic Graph Theory
- CSE841 Artificial Intelligence
- CSE842 Natural Language Processing
- CSE845 Multi-Disciplinary Research Methods for the Study of Evolution
- CSE847 Machine Learning
- CSE848 Evolutionary Computation
- CSE860 Foundations of Computing
- CSE870 Advanced Software Engineering
- CSE872 Advanced Computer Graphics
- CSE885 Artificial Neural Networks

## Words From Dr. Nahum

One of my favorite professors, Dr. Nahum, stressed to me the importance of keeping up with the industry. You're coming into a market that's changing everyday. Languages are being made, frameworks are being updated, tools are being released. Computer science is probably the most competitive major today. You'll have to work hard, and you'll want to stand out if you're going to get those internships. 

You should *keep learning*. You should keep practicing, and you should always be willing to pick up new frameworks, languages and tools. Make connections, try new things, do side-projects, and always apply for as many internships as possible.

## My Final Farewell

On this repo, there's a book called "Cracking the Coding Interview", which I highly recommend before going into a.. coding.. interview. The title is pretty self-explanatory. At the bottom of the README is a link to apply to become a ULA within the CSE department. I would be more than happy to give any of you guys a referral!

And if you're going to be heading into CSE232 next semester, feel free to contact me for help! I know I'm a 231 TA, but I code in like 5 different languages, so throw me a problem and I can probably get you an algorithm for it lmao.

I believe in all of you. Learning how to program is the biggest hurdle of the major, and after you learn how to program, it's all just stuff you can do *with* programming. The more languages you learn, the better you'll become at programming in every other language you know. Creating an algorithm is the hardest part about programming, but once you nail how to do that, the rest is simple. 

I'm going to miss you guys.

I wish you all the best, remember to never give up.
