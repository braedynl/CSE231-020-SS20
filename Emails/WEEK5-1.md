Subject: CSE231 Sec 020 - Lab05 Stuff & SIGPIPE Errors (Week of 2/2/2020)

Sent: Sat 2/8/2020 6:19PM

________________________________________

Howdy ya'll,

Sorry my email is a bit later than usual.

[Lab05 stuff can be found here](https://github.com/braedynl/CSE231-020-SS20/tree/master/Lab%2005).  The 'b' version of the file is only slightly different from the 'a' version, so I didn't write a documented version. If anyone wants one, however, tell me and I can make one for you. The only difference in the 'b' version is that all of the display strings get written into an output text file using the `file` parameter of print(). The reason I expressed a lot of disgust towards this lab is because it's extremely tedious to do what Enbody wanted without some sort of data structure. Next week we'll be talking about lists, an extremely essential and useful data structure that would make this code 10 lines or less. 

Mimir Exercises Ch.6 is due tonight (2/8/2020 11:59PM), and Project 04 is due Monday (2/10/2020 11:59PM). 

One of you talked to me in-class about a SIGPIPE error when submitting to Mimir for Project 04, and so I feel I should address that in case anyone else is having a similar problem. 

Starting with this project, everything becomes a lot more function-based. It's common practice to put the main execution of your code into a function called main(), and so what will happen is you'll call each of your other functions from main() to accomplish the main task of the project. Included with every project from this point on is some starter code that you can find on the "[project files](https://www.cse.msu.edu/~cse231/Online/Projects/Project04/)" page. It lays out each of the functions you'll be writing with a `pass` in place of the function's code until you fill it in. Keep all of the functions that are laid out. Mimir will try to extract them from your code, but will get mad at you for removing them. Additionally, there's a special function that looks like this:

```
if __name__ == "__main__":
    main()
```

Do not delete this function. We'll talk about what this does at some point in the coming weeks. Mimir uses this function to extract code from your project, so it's important that you keep it. If you remove these functions, you'll get that annoying SIGPIPE error. 

I was also really happy to see some confidence from you guys coming out of exam 1. Most of the time people come out of those exams feeling confused and unsure if they get a good score or not. It seems like you guys are really on the right track!

Best,

Braedyn Lettinga
