# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

pwd = print working directory
hostname = my computer's network name
mkdir = make directory
mkdir -p = creates entire path
touch = creates new empty file
cd = change directory
cd .. = move up directory path
cd /home = move to home directory
cd ~Documents = move to documents
ls = list directory
ls -1R = lists all folders in directory
rmdir = remove directory
pushd = push directory (save current dirctory to list, move to another directory)
popd = pop dirctory (go to last pushed directory)
cp = copy file or dirctory
cp -r = copies directories with files in them
mv = moves file or directory
less = page through a file
cat = print whole file to screen
xargs = execute arguments
grep = find inside files
man = read a manual page
apropos = find apropriate manual page
env = look at your environment
echo =print some arguments
export = set a new environment variable
exit
find


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

ls = lists the contents of the directory
ls -a = includes entries whose names begins with a dot (hidden files)
ls -l = list in long format (displays all info about file)
ls -lh = displays file size in human readable format


---


---

What does `xargs` do? Give an example of how to use it.

xargs constructs argument lists and invokes another utility. xargs reads items from the standard input or pipes and executes the command  with any initial-arguments followed by items read from standard input. 
For instance, find . -name ".txt" | xargs grep "file" will first fina all the txt files from the current directory and then search each of those files for the word "file"


---

