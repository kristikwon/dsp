# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
   - `pwd`: print working directory
   - `mkdir` [option…] directory… : make directories. Option “-p” create parent directories as necessary. No error is reported if a specified directory already exists
   - `cd`: move into specified directory
   - `ls` [option]… [file]… : list out the contents of the directory you are currently in
   - `pushd`: push directory; saves the current working directory in memory/stack so it can be returned to at any time.
   - `popd`: pop directory; returns to the path at the top of the directory stack
   - `cp`: copy a file or directory. Command cp origfile newfile makes a copy of a file in the working directory. If the file already exists, it will be overwritten without a confirmation prompt (option –i to be prompted). To copy a file into another directory with a new name: cp origfile /directory/subdirectory/newfile. To copy an entire directory structure into another location: cp –R /one/two /three/four. Directory /three must already exist for this command to work, but if the directory four does not already exist in /three, it will be created.
   - `mv`: move a file or directory. Renames file SOURCE to DEST (mv source dest), or moves the SOURCE file(s) to DIRECTORY (mv source directory) (mv –t directory source)
   - `less`: page through a file; the output displays summary of what program shows
   - `find`: find files; Within each directory tree specified, evalues the given expression from left to right, until the outcome is known. Find moves on to the next path until all paths have been searched
   - `grep` [options] pattern [file…]: “global regular expression print”. Processes text line by line and prints any lines which match a specified pattern
   - `echo`: displays a line of text. This is like print command in python
   - `exit`: exit the shell. If you have jobs running in the background, the shell will remind you that they are running. Issuing exit again will terminate those jobs and exit the shell 


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

> > 
   - `ls`: lists all files in the directory
   - `ls -a`: displays all files
   - `ls -l`: displays the long format listing (total files in the directory and subdirectories, names of the files in the current directory, their permissions, the number of subdirectories in directories listed, the size of the file, and the date of last modification)
   - `ls -lh`: lists files with sizes in human-readable format (e.g. 1K, 234M, 2G)
   - `ls -lah`: lists all files print sizes in human readable format
   - `ls -t`: list files, sorted by modification time newest first
   - `ls -Glp`: displays long format listing, suppressing group names, and append “/” indicator to directories


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

