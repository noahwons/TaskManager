# TaskManager
#### Video Demo:  https://youtu.be/MFiSZ3vivt8
#### Description: A program designed to store tasks and allow the user to edit saved input

**What is TaskManager?**
The initial idea that I had for this program was to create a text-based program that had the ability to store my ideas in one place.
I decided that the implementation of something useful would help me maintain motivation to continue my progression. I myself am personally
extremely forgetful and seem to benefit from writing down tasks or creating a to-do list, so that all of my goals are in one place.
TaskManager was designed to digitalize this idea and simplify the implementation so that it could potentially be used in everyday life.

**Problems I Faced**
Though the code is not perfect, it was an achievement for me to be able to have the program run and run properly. Along with the development of
the program, I struggled with learning how to delete information from a CSV file, learning how to modify information in a CSV file and work
thoroughly with dictionaries. Along the way, I began to discover new ways to solve my problems. For example, I was struggling to index into a
dictionary at the proper location because I was unaware of a function called "index" that could locate the index of a dictionary within a string.
This function proved helpful during my implementation of the "complete" command.

**Where Did the Idea Come From?**
After I reached the final week of CS50p I was trying to find an idea that would make sense for me to implement in Python. Eventually, I brought
it up in my 7th-period physics class where a friend of mine recommended that I created a task-managing, text-based software. At first, I looked at
him in disbelief because I was not confident enough in my abilities. As I looked for other ideas I eventually decided that the task-manager software
would make sense because it is a program that could potentially benefit me and have an actual application in my everyday life. So I began work on the
project. It proved to be a very difficult task, however, I was able to solve the problems I faced and constantly look for new ideas to implement. I am
very grateful for the idea from my friend because without it, who knows if I would have ever finished!

**What are the roles of each file?**
the most important file: "project.py" contains the main function of the program and a few other associated functions that display the commands and
validate them as well. The class for a "Task" object is contained in "tasks_classes" where the input is validated and stored in "tasks.csv." "tasks.csv" is the file
that contains the basic information of a task such as the description, category, priority level, and id. The id is a very important piece of information
associated with each task because it is the number that the program will use to associate the commands that the user inputs and the task they are attempting
to edit. The "tasks_functions" file contains all code that is associated with the "tasks.csv" file, basically ensuring that the commands entered into the prompt
inside of the main function actually do what they are intended to. Similarly, the code in "dates_fuctions" contains code for the "dates.csv" file, a file containing the
id #s of tasks that have been scheduled for a date. "dates_functions" will also ensure that the commands run properly and will also provide the user with chances
to "reschedule" a task without this being an actual command from the commands list. The file "test_project.py" is the testing file that tests multiple functions to
ensure that they run properly and provide the expected output.

**Who's it for?**
If you are anything like me, trying to focus on goals and acomplishing tasks can prove to be very difficult. Oftentimes, having everthing that needs to be done in
one location may seem to be a luxury that you never realized you needed. With tasks all in one location it can allow you to sort out what it is that you need to do
and complete such activities based upon their given priority level. tasks with a lower priority level would mean that they are more important ie: studying for a
Calculus exam may have a priority level of 1 when being compared to taking out the trash which may have a priority level of 3 or 4.
