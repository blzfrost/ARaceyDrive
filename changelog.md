Feb 15   2hr  
I uploaded the initial state of the program.  
Still getting used to github so changes are expected.  
I'll continue to utilize this repo throughout the project and provide updates in this readme.  
Currently, it's just the core files. It will need an environment that contains pygame in order to run.  
I can include the virtual environment that I use if you want, but it looks like that's bad practice here.  

I'll try to figure out how to create a requirements file at some point.  
Expect a bulk of the improvements to occur during spring break.

March 4th  2hr
Added README.md to project (not just GitHub)  
fixed typo  
added colors list  
Tried working with classes...  
    It's slow progress  
Spent some time staring at the code...  
    Inspiration isn't my friend right tonight.  

March 6th  2hr  
Worked on UML diagrams  
Stared a lot mindlessly  
Worked on the car and thing classes  
Decided to scrap the data class and found I could just have the data declared up top to do what I wanted.  
Learned that two spaces at the end of a line in .md creates a new line!  
Decided that I'm going to rewrite a new version of the script instead of trying to re-engineer the original.  

March 15th 3.5h  
Tried to split the classes and some data into its own file again.  
Finding it challenging.  
Got them separated!  
Working on getting things to show up on the map.  
That took a minute. Now working staggering entrance.  
Test drove. Got bored around 150. Need to tweak challenge.  
Increased global multi from 0.5 to 0.8.  
1) That made it much more engaging. 
2) It reminded me I haven't implemented crash physics. Need to get on that  

Increased thing size from 50 to 75, decent change.
Played with thing speed  
Started implementing lines.  
  Kind of a disaster so far.

March 18th 2hr
Bringing in things sooner.  
Looked into lane dividers a bit. Back burner for now.    
Looked into adding music.  
Found a track called "Energy" from 
> https://freemusicarchive.org/music/Scott_Holmes/media-music-mix/energy-1  

Changed thing 2 start from 10 to 5 and thing 3 start from 30 to 15  
Implemented 3 lives and crash system.  
___Need to implement a continue screen.  
Fixed line dividers by making their own class.  

Mar 22nt 3 hours  
Added more crash messages  
Randomized messages  
Added smart logic to messages  
Made a continue screen  
Added optional size control argument to message_display()  
Decreased default message_display() size  
Implemented a persistent high score system  
Deleted old "Thing.py" file  

Mar 26  2 hours
Renamed this document to changelog.md  
Created Readme that actually describes the program and offers instructions on how to play  
Added reduce_numbers to Thing class to manage speed and size after crash  
Updated Car upgrade method  
Balanced several values  
Cleaned up code

Mar 30 2 hr
Tweaks and balancing  
Shrunk resolution  
Worked on making the dividers adjust with screen size  
Drastically reduced volume. From .5 - .1  
added colors  
worked on thing y reset_pos method  
Updated Readme.md  
Restructured the entire file structure for presentation  
Fixed bug