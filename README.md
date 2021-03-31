Hello world! My name is Ryan Huffman, and I made this game as part of an honors project.  
The project itself is based on a tutorial originally created by SentDex.  
> You can find his tutorial at  
> https://pythonprogramming.net/pygame-python-3-part-1-intro/  

I highly recommend checking it out if you want to build something like this yourself!

For those looking to jump right in, we'll keep it simple.  
> You will need to download and install Python  
> https://www.python.org/downloads/release/python-392/  

> You'll also need to download and install pygame  
> https://www.pygame.org/wiki/GettingStarted

In the game itself, you'll control the race car.  
You can use either 'a' & 'd', or the left and right arrows to move.  
If you want something else, feel free to modify the code to your liking.  
You do you. :D

While you're enjoying your pleasant drive,  
probably doing something noble like getting groceries for you grams,  
random things appear trying to stop you!  

Of course, you won't let that stop you.  
You'll make it past as many of these things as you can (within 3 lives).

I hope you enjoy!!!

----------------

This project is near and dear to me as it's a continuation of the project that got me into coding.  
It's the project that helped me convince myself to get into college,  
so being able to return to it was really fun!

This was the first time I had incorporated git and GitHub in a project,  
so that was a fun learning experience.  
It took a bit to understand commit notes, my readme was more of a changelog, etc.  
But by the end of the project I was more comfortable with the process of managing multiple branches,  
Was more specific with my commit notes, and streamlined the push process.  
This is also my first time using .md, and I can tell I'll need some practice,  
but I'm getting there.

The project itself was a nice change of pace.  
Instead of something scripted, the rehashed programs with known goals and values,  
it was nice to have a project that was only limited by my innovation,  
where I could take it anywhere I wanted.  
This also meant I had to go about it more strategically.  

It was clear after playing with the original code that I needed a plan.  
So I went to lucid charts to design myself a UML plan  
> Lucid Charts https://lucid.co/

One of the goals I set out was to clean up the game loop.  
I wanted a game loop that was mostly there to check variables and execute the proper code,  
but not to be the actual code itself.  
I wanted it to handoff control to other functions and classes for that,  
this way it was easy to follow the flow of information.  

I also wanted to convert the thing, player, and variables into their own classes.  
I knew I wanted to expand the features beyond just functions and variables.  
I wanted to encapsulate them and make them more robust.  

Finally, I wanted to split the data into two scripts,  
one for the core game logic and display related functions,  
and one for the tokens and variables.  
I wanted to expand on my experience working with interconnected files.  

So I got to rebuilding.  
Getting the initial files set up wasn't hard,  
but it required me to set up a lot of it before I could debug anything.  
After I could display the car, things got better.  
Then it was time to implement the things.  

I realized that having the variables in their own class was a horrible idea.  
(Ok, I went back and forth on this for some time)  
The inspiration was from my time with Java and C++ code structure.  
But, I realize, Python isn't Java or C++, and I shouldn't treat it as such.  
So I embraced public EVERYTHING and went to work with the variables up top.  

Hit some errors and combined the two scripts into one.  
Horrible idea.  
Split them up and cleaned up my code.  

A lot of time was spent trying to tune the numbers so there was more of a curve.  
With the numbers growing linearly, the challenge was ramping up to fast.  
It felt less like a game, and more like an insane gauntlet.  
But, with a few tweaks, (over a long period of time) I found a rhythm that was tolerable.  

From this point on it was just trying to play with and implement features that were lacking.  
I left the crash feature out for a while,  
relying on a message in the console to let me know when I crashed.  
So much easier to debug that way.  
(Who knew a car crash could take you out of your groove. ¯\_(ツ)_/¯ )  

The lane dividers took some work.  
I originally tried to repurpose the thing class to do it,  
creating all kinds of exceptions.  
Not the best way.  
Ended up giving them their own class to make my life easier.  
Balancing them took some time.  
It wasn't until I took away the "magic numbers" and based them off of resolution,  
(for an unrelated upgrade) that they clicked into place.  

Then to enhance I found a cool music track, implemented the crash functions,  
set up some lives, made a high score feature,  designed a continue screen, and continued tweaking.  
Creating a file for high scores required returning to my old book and searching the web a little.  
It's been awhile since I took my class. It was a good refresher!

I'll continue to work on this over time, so if you see any improvements,  
feel free to shoot a comment to me at rhuffman@mail.pima.edu or open a ticket!

------------

Data found in ClassObjects.py is game logic  
Data found in ARaceyDriveV2.py relates to flow and display.

Have fun playing with values in ClassObjects  
display_height/display_width (Your road, your rules)  
start2/start3 (The scores needed for more things)  
starting_score (It's not cheating, it's looking ahead!)  
FPS (clock speed modifier)  
global_multi (thing and car speed multi)  
lives (more is better, right?!?!)  