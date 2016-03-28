# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering. 

Everything is new to me - so here goes nothing: <br>
pwd = print working directory <br>
hostname = my computer's network name<br>
mkdir = make directory<br>
mkdir -p = creates entire path<br>
touch = creates new empty file<br>
cd = change directory<br>
cd .. = move up directory path<br>
cd /home = move to home directory<br>
cd ~Documents = move to documents<br>
ls = list directory<br>
ls -1R = lists all folders in directory<br>
rmdir = remove directory<br>
pushd = push directory (save current dirctory to list, move to another directory)<br>
popd = pop dirctory (go to last pushed directory)<br>
cp = copy file or dirctory<br>
cp -r = copies directories with files in them<br>
mv = moves file or directory<br>
less = page through a file<br>
cat = print whole file to screen<br>
xargs = execute arguments<br>
grep = find inside files<br>
man = read a manual page<br>
apropos = find apropriate manual page<br>
env = look at your environment<br>
echo =print some arguments<br>
export = set a new environment variable<br>
exit = exit<br>
find = find<br>


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

ls = lists the contents of the directory<br>
ls -a = includes entries whose names begins with a dot (hidden files)<br>
ls -l = list in long format (displays all info about file)<br>
ls -lh = displays file size in human readable format<br>
ls -lah = lists all file in long, human readable format<br>
ls -t = displays files with newest items first<br>
ls -Glp = enables a colorized output and lists directories in long format with a slash after their name<br>


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -m = displays names as a file seperated list <br>
ls -R = displays subdirectories as well <br>
ls -1 = displays each entry on a line <br>
ls -u = displays files by file access time <br>
ls -F = flags filenames <br>


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

'xargs' constructs argument lists and invokes another utility. 'xargs' reads items from the standard input or pipes and executes the command  with any initial-arguments followed by items read from standard input. <br>
For instance, 'find . -name ".txt" | xargs grep "file"' will first find all the txt files from the current directory and then search each of those files for the word "file"


 

