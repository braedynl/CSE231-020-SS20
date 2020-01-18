Subject: CSE231 Sec 020 - Pre-Lab Whoopsie, The Debugger Debacle and `pass` (Week of 1/12/20)

Sent: Sat 1/18/2020 4:03PM

_________________________________________________________

Howdy ya'll, 

Okay so yesterday in class, I was told by some of you that you guys were unable to complete the pre-lab on the day of lab. That was very much my fault for telling you guys you could do that. When I took the course you were able to, but I guess Dr. Enbody changed it. For anyone that was affected by this, you should see on D2L that I gave you credit for this week's pre-lab. I'm extremely sorry about the misinformation. So from here on out, pre-labs are due the day before lab at 11:59PM. I'll still get you credit if you happen to have problems with accessing the pre-labs or D2L in general.  Again, super sorry about this. 

As always, [you can find my in-class presentation, demonstration code, and an example lab02 answer here](https://github.com/braedynl/CSE231-020-SS20/tree/master/Lab%2002). There's a commented version labeled with a 'c' in its name. From this point on, everyone's code is probably going to look extremely different. I think it's implicit then that this is just one way of solving lab02. There are many, many ways you could go about doing it. 

I know that lab02 also introduced the Spyder debugger a little and people were having trouble with it, including myself (I've always used a different code editor). Next week I'll try and get everything sorted with that for anyone that wants to use it, but I personally think [PythonTutor](http://pythontutor.com/) is a far more superior debugger as of right now. PythonTutor has a lot of limitations when we get to some later topics, but if you're just trying to diagnose problems with a small chunk of code, I would say that it's probably better than the debugger of any code editor. 

At some point this weekend, I'll also be getting back to you guys with your Project 01 grades. Mimir should notify you when I release them, and you'll be able to see some comments I left on your code. The project grades will also be reflected in D2L (this is where your "true" grade for the class is).

Lastly, something that I didn't touch on in-class was the 'pass' keyword in Python. It's not something that is commonly used, but a lot of you found it useful, as did I when I did lab02 myself. 'pass' does exactly what you would expect it to. The line that contains 'pass' does absolutely nothing, which can be useful in very specific circumstances. As one example, let's say you had an if-statement. You know what condition you want to check, but you don't know what kind of algorithm you want it to run yet. 

```
x = 5

if x == 6:    # SyntaxError: unexpected EOF while parsing (<string>, line 3)
```

When we have a loose if-statement, we get an error. Python expects to run something after you write an if/elif/else statement. But we really want to have this if-statement here because we're going to use it later. So we can just add 'pass' for right now and come back to filling it in later. 

```
x = 5

if x == 6:
  pass
```

We now no longer get an error as shown, and so the code runs perfectly fine. Our if-statement in this case doesn't do anything, but now I can have my code do other things beyond lines 3-4 if I have something below that I want to be ran. This of course is just one example of using 'pass', you can probably think of many other places to use it. This is just what I use it for most often.

I think that's all for right now, then. As always, email me if you have questions, comments or concerns. Mimir Exercises 02 are due tonight at 11:59PM (1/18/20), and Project 02 is due on Monday at 11:59PM (1/20/20). Get started early!

Best,

Braedyn Lettinga
