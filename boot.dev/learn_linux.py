#Welcome to learn Linux
#Goals of this course
#Understand the difference between a shell and a terminal
#Learn how to navigate and use the file system using the command line
#Learn how to install software using the command line
#Understand how to manage your PATH and environment variables
#Learn how to manage permissions and execute programs

#Ch1 Terminals and shells
#Reasons to not use the GUI
#They're weak. You are given much more control over your computer through a CLI. With a GUI you're limited to the options that the developer of the GUI has given you.
#They're slow. Once you know the commands to type, it's much faster to type them than to click through endless menus with a mouse.
#They're not as reproducible. If you want to share a set of instructions, you can just copy and paste commands without worrying about screen sizes and user preferences.
#They're not automatable. It's easy to write code that manipulates text (as you've seen in Python), but it's much harder to write code that manipulates GUIs.
#They're not as cool. You will be invited to 90% fewer romantic outings if you are a GUI user.

#Terminal emulators are programs that allow you to issue text based commands
#Shells are programs that take those commands and actually run them 
#Shells are often referred to as "REPL"s. REPL stands for
#Read
#Eval (evaluate)
#Print
#Loop

#Both Bash and Zsh are shells, and they also happen to be powerful programming languages. They have variables, functions, loops, and more. That said, only crazy people write large programs in shell languages... shells are optimized for running other programs and writing small scripts, not for writing large applications.

#variable creation
name="Lane"
#Notice there are no spaces between the variable name, assignment operator = and value "Lane".

#Usign a variable
$ echo $name
Lane
#Starting a line with the $ symbol is a convention to show it's a shell prompt, and it should not be typed. The actual command is echo $name.
#Unlike in Python, where you can just use a variable's name, in your shell you need to prefix the variable name with a $ to use it, else it would just print name instead of the value.
$ echo Hello $name
Hello Lane

#history command will print full history of terminal to terminal
#You can use the clear command to clear the terminal if it is feeling cluttered
#You can cycle through commands in terminal with the up and down arrow Key

#Ch2 File Systems

#Commands
#pwd is print working directory
#ls is the list files and folders in current directory
#lsblk: Lists all block devices, excluding RAM disks, in a tree format.
#cd is the change directory command
#cd .. will back out of the current directory
#cat file1.txt file2.txt - Concatenate the contents of multiple files and print them to the terminal
#head -n 10 file1.txt - The head command prints the first n lines of a file. The -n flag specifies n as shown:
#tail -n 10 file1.txt - The tail command prints the last n lines of a file. The -n flag specifies n as shown:
# less -N 2023.csv - will show the file line by line with line number because fo -N, can use enter to go down a line and b to go back up a page and q to exit this mode 
# touch new_file.txt - will update the timestamp of the given file but will also create it if it doesn't exist
# touch some_file.txt some_other_file.txt - can also create multiple
# mkdir my_directory
# mv some_file.txt some_other_name.txt - Renaming a file:
# mv some_file.txt some_directory/some_file.txt - Moving a file from the current directory to another nested directory:
# mv some_file.txt ../some_file.txt - Moving a file from the current directory, to the parent directory:
# mv some_file.txt some_directory/ - If you don't want to rename the file and you're just moving it to a different directory, you can omit the filename:
# rm some_file.txt - The remove command deletes a file or empty directory:
#grep "hello" words.txt - This will print out every line in words.txt that contains the word hello. It's a case-sensitive search, so it will only match hello, not Hello or HELLO.
#grep "hello" hello.txt hello2.txt - grep multiple files
#grep -r "hello" . - recursive search in a directory and all of its folders and subfiles
#sudo - superuser command 
#chmod - change mode / change permissions of a folder or file -rwxrwxrwx
#chown command, which stands for "change owner," allows you to change the owner of a file or directory, and it requires root privileges.
# which sh - The which command tells you the location of an installed command line program.
#export NAME="Lane" - To set a variable in your shell, use the export command:
# man grep # manual for grep tool - can man for any manual for a program that has one
# -h or --help flag in a command will return something of a quick start gfuide for the command
# ./ represents the current working directory, so you can put this before a script's name and it will execute the script
# echo $? - In a shell, you can access the exit code of the last program you ran with the question mark variable ($?). For example, if you run a program that exits with a non-zero exit code, you can see what it was with the echo command:
#kill <PID> - PID stands for "process ID." Every process that's running on your machine has a unique ID. The ps, "process status" command can be used to list the processes running on your machine, and their IDs:
#ps aux - processing services and aux is all processes
#edit a text file in command line - nano filename.md



#/Users/wagslane
#The first slash (/) represents the root directory. It's the tippy-top of the filesystem tree.
#The next part (Users) is the name of a directory inside the root directory.
#Finally, the last part (wagslane) is the name of a directory inside the Users directory.

#Relative Paths
#When inside the top-level vehicles directory, the relative path to the mustang.txt file is:
#cars/fords/mustang.txt
vehicles
├── cars
│   ├── fords
│   │   ├── mustang.txt
│   │   └── focus.txt

#Absolute paths
# An absolute path is a path that starts at the root of the filesystem. On Unix-like systems (macOS/Linux), the root is denoted by a forward slash /. 
# So, if the vehicles directory is in the filesystem root, the absolute path to the mustang.txt file is
#/vehicles/cars/fords/mustang.txt

#cat command
#The cat command is used to view the contents of a file. It's short for "concatenate", which is a fancy way of saying "put things together". 
# It can feel like a confusing name if you're using the cat command to view a single file, but it makes more sense when you're using it to view multiple files at once.
# Print the contents of a file to the terminal
cat file1.txt
# Concatenate the contents of multiple files and print them to the terminal
cat file1.txt file2.txt

#Head and tail commands
head -n 10 file1.txt - The head command prints the first n lines of a file. The -n flag specifies n as shown:
tail -n 10 file1.txt - The tail command prints the last n lines of a file. The -n flag specifies n as shown:

#More and Less
#The more and less commands let you view the contents of a file, one page (or line) at a time.
#When you run less Notice that you're now in an interactive mode and you've lost your shell prompt! That's because less has taken over your terminal window.
#Press "enter" a few times to scroll down a few lines, just to see how that works. 
# Press "q" to exit the less program and return to your shell prompt.
# Re-run the less command, but this time, pass in the -N flag to show line numbers:
less -N 2023.csv

#Touch
# The touch command updates the access and modification timestamps of a file. 
# By default, if the specified file does not exist, touch will create an empty file with the given filename. 
# Because of this side-effect, you'll often see this command used to quickly create new empty files.
touch new_file.txt
# touch some_file.txt some_other_file.txt - can also create multiple

#Make directory
#The "make directory" command creates a new directory inside (or relative to) the current directory.
mkdir my_directory

#Move
#The move command moves a file or directory from one location to another. 
#You can use it to rename a file or to move it to a different directory altogether. 
#Your working directory can't be the directory you're moving.

#Renaming a file:
mv some_file.txt some_other_name.txt

#Moving a file from the current directory to another nested directory:
mv some_file.txt some_directory/some_file.txt

#Moving a file from the current directory, to the parent directory:
mv some_file.txt ../some_file.txt

#If you don't want to rename the file and you're just moving it to a different directory, you can omit the filename:
mv some_file.txt some_directory/

# Both the target and destination have to be valid paths from the current working directory. 
# Use pwd to see where you are and adjust the source and destination paths accordingly. 
# Use ls to verify that the file has been moved correctly. 
# If you mess up the mv command, you'll need to figure out where you accidentally moved the file to, then move it from that location back to where it belongs.

#Remove
#The remove command deletes a file or empty directory:
rm some_file.txt
#You can optionally add a -r flag to tell the rm command to delete a directory and all of its contents recursively. 
# "Recursively" is just a fancy way of saying "do it again on all of the subdirectories and their contents."
rm -r some_directory

#Copy
cp source_file.txt destination/
#Can copy recursively like remove command
cp -R my_dir new_dir

#Home
#In a Unix-like operating system, a user's home directory is the directory where their personal files are stored. 
# It is also the directory that a user starts in when logging into the system.
# I recommend doing all of your development work in your home directory. 
# For example, I like to create a workspace directory in my home directory, and all my programming projects live in subdirectories there.
# The ~ alias
# My home directory (on Mac) is located at /Users/wagslane. The ~ character is an alias for your home directory. 
# So when I want to go home, I don't have to type out cd /Users/wagslane, I can just type:
cd ~

#GREP BABYYYYYYYYYYY LETS GOOOOOOOO
#The grep command allows you to search for text in files. It has a ton of capability, and we'll only be scratching the surface of its true power.
#Basic Usage
#The most basic use for grep is to search for a string in a file. For example, if we wanted to search for the word "hello" in the file words.txt, we could run:
grep "hello" words.txt
#This will print out every line in words.txt that contains the word hello. It's a case-sensitive search, so it will only match hello, not Hello or HELLO.
# I wonder if you can grep from outside of the folder the file is in for something, you can recursive search for something in all sub directories
#grep multiple files
grep "hello" hello.txt hello2.txt
#recursive search in a directory and all of its folders and subfiles
grep -r "hello" . #. is a special alias for the current directory.

#Find
#The find command is a powerful tool for finding files and directories by name, not by their contents.
#Let's say you're looking for a file named hello.txt somewhere in your home directory. You can use the find command to search for exactly that title:
find some_directory -name hello.txt
#Pattern Search
#The find command can also search for files that match a pattern. For example, if you wanted to find all files that end in .txt, you could run:
find some_directory -name "*.txt"
#The * character is a wildcard that matches anything. If you're trying to find filenames that contain a specific word, you can use the * character to match the rest of the filename:
# Find all filenames that contain the word "chad"
find some_directory -name "*chad*"
#(base) mkelly7@MACGM6Y7PJ2TV worldbanc % find public/products -name "*joint*" - The find command assumed I was at least in the parent directory of worldbanc and then searched the public/products directory and then searched the names of files for the words "joint" with the wild cards

#Permissions
#sudo means superuser do 
#Let's break down each character. The first one just tells you whether you're looking at a file or a directory:
-: Regular file (e.g. -rwxrwxrwx)
d: Directory (e.g. drwxrwxrwx)
#The next 9 characters are broken up into 3 sets of rwx and represent the permissions themselves for the "owner," "group," and "others," in order. Each group of 3 represents the permissions for reading, writing, and executing, in order. So, for example:
rwx: All permissions
rw-: Read and write, but not execute #unless you're specifically in a group, the middle 3 of the 3 you're likely in others, only sysadmins worry about groups
r-x: Read and execute, but not write

#The chmod command lets you change the permissions of a file or directory. It's short for "change mode" (I wish it was called "change permissions," but alas)
chmod -R u=rwx,g=,o= DIRECTORY # The owner can read, write, and execute, The group can do nothing, Others can do nothing. The 'u' is user which is just the owner, don't get confused with o which is other
#Remember, . is a special alias for the current directory.
#chmod command has a convenient -x flag that will simply remove the executable permission from the file
chmod -x genids.sh

#Executables
#Files with a .sh extension are shell scripts. They're just text files that contain shell commands. You can run a file in your shell by typing its filepath:
mydir/program.sh
#Interestingly, if the program is in the current directory (in this example, the mydir directory), you need to prefix it with ./ to run it:
./program.sh
# As far as file paths go, ./program.sh and program.sh are the same. The dot (.) is an alias for the current directory. 
# We need the prefix when running executables so that the shell knows we're trying to run a file from a file path, not an installed command like ls, mkdir, chmod, etc.

#root is a superuser
#chown command, which stands for "change owner," allows you to change the owner of a file or directory, and it requires root privileges.
#You must be in the parent folder of the folder you want to change the permissions on when putting in the directory to the command
sudo chown -R root contacts

#Programs
# Compiled programs
#A compiled program is a program that has been converted from human-readable source code into machine code (binary). Machine code is a set of instructions that a computer can execute directly: your computer's CPU is hardware that's been designed to execute machine code.
#Programming languages like Go, C, and Rust produce compiled programs.

#Intepreted programs
#Programming languages like Python, Ruby, and JavaScript, are typically interpreted as they run, which means your computer needs to have the interpreter installed to run the program.
# The shell .sh is also an interpreted language

#The which command tells you the location of an installed command line program. In this case, we're asking for the location of the sh (shell) program.

#Shebang
#A "shebang" is a special line at the top of a script that tells your shell which program to use to execute the file that needs to be interpreted
#You can see at the top of the file, /private/bin/genids.sh the top of the file has the shebang which is required to interpret it, in this case bash

#Bourne Shell
#sh: The Bourne shell. This is the original Unix shell and is POSIX-compliant. It's very basic and doesn't have many quality-of-life features.
#bash: The Bourne Again shell. This is the most popular shell on Linux. It builds on sh, but also has a lot of extra features.
#zsh: The Z shell. This is the most popular shell on macOS. Like bash, it does what sh can do, but also has a lot of extra features.
#Both zsh and bash are "sh-compatible" shells, meaning they can run .sh scripts, but they also have extra features that generally make them more pleasant to use. 
# For your purposes, the differences between zsh and bash are not super significant. Everything we do in this course will work in both shells.
#you restart your shell after changing a shell configuration file because the config file only runs when you start a new shell session

#Environment variables
#There is another type of variable called an environment variable. They are available to all programs that you run in your shell.
#You can view all of the environment variables that are currently set in your shell with the env command.
#To set a variable in your shell, use the export command:
export NAME="Lane"

#PATH
#If it weren't for the PATH, you'd have to remember the filesystem path of every executable you wanted to run in your shell. 
# Instead of just running ls, you'd have to run /bin/ls (or whatever the location of the ls executable is on your system).

#Change your path
#A common problem you'll run into in the future is that you install a new program on your machine, but when you try to run it from your terminal, you get an error like:
$ my-new-program
-bash: my-new-program: command not found
# Nine times out of ten, it's because the program is installed in a directory that's not in your PATH variable. 
# Oftentimes when you install a program using the CLI, it will print a message during the installation process that tells you where the command was installed. 
# Don't let your eyes glaze over when your terminal prints important messages! Sometimes you just gotta rtfm (read the fucking manual).

echo PATH to see the path variables
# To add a variable to your path directory you'll need to add the absolute path, not the relative path. 
# You can get the absolute path by running pwd in the worldbanc/private/bin directory, or by using the realpath command.
# To add a directory to your PATH without overwriting all of the existing directories, use the export command and reference the existing PATH variable:
export PATH="$PATH:/path/to/new"

#In the path variable changes are only applicable to the existing shell session. You'll need to update the shell config file in order to not have to run the shell command every sesion.

#Man (command)
#The man command will only work for programs that it has a manual for, but most built-in commands and Unix programs are supported. You just pass the name of the command as an argument. 
# The most intuitive place to start, of course, is reading the manual's manual:
man man
man grep # manual for another tool
#You can use / in order to search the manual
#when searching it will find results line by line, for example, if a line has the result of what you're looking for then it if you go to the next result with 'n' it will skip past that result on the same line.
# You can use 'n' to go to the next result. You can use 'N' (shift+n) to the previous result on the page
#q key to quit the manual

#Flags
#many commands will have flags like -l, -a, etc
#You can combine them with -al
#Flag Conventions
#Whether or not a command takes flags, and what those flags are, is up to the developer of the command. That said, there are some common conventions:
#Single-character flags are prefixed with a single dash (e.g. -a)
#Multi-character flags are prefixed with two dashes (e.g. --help)
#Sometimes the same flag can be used with a single dash or two dashes (e.g. -h or --help)

wc -c pr_ideas.txt #got the number bytes of the file in this directory

#Help
#-h or --help is often like a quick start guide rather than a manual
#curl command allows you to run network requests from the command line

#Exit Codes
# Exit codes (sometimes called "return codes" or "status codes") are how programs communicate back whether they ran successfully or not.
# 0 is the exit code for success. Any other exit code is an error. 
# 9 times out of 10, if a non-zero exit code is returned (meaning an error) it will be 1, which is the "catch-all" error code.

#standard output - stdout
#print function in python
#echo function in bash 
#returns standard text output

#standard error - stderr
#used for error messages

#redirecting streams
#You can redirect stdout and stderr to different places using the > and 2> operators. > redirects stdout, and 2> redirects stderr.

echo "Hello world" > hello.txt
cat hello.txt
# Hello world

cat doesnotexist.txt 2> error.txt
cat error.txt
# cat: doesnotexist.txt: No such file or directory
#In this example, cat is used to intentionally generate an error message (since the file doesn't exist), which is then redirected to error.txt.

#command for standard error assignment
worldbanc/private/bin/process_transactions.sh worldbanc/private/transactions/2020.csv 2> /tmp/worldbanc.log
#In order to run this command I had to navigate to the parent directory of the worldbanc directory. In this case it for ~Documents/GitHub/code_practice

#Standard in
#"Standard Input", usually called "standard in" or stdin, is the default place where programs read their input. It's just a stream of data that programs can read from as they run.

# execution stops until the user types
# something (in this case "Lane") and presses enter
name = input("What is your name? ")

print("Hello,", name)
# Hello, Lane

# When you run the worldbanc/private/bin/worldbanc.sh program again. Notice that it makes use of stdin to read your name and email. In the code output it uses the read command:
echo "Please enter your name:"
read NAME

echo "Please enter your email:"
read EMAIL

#Piping
#The | is able to take the standard output from a command and put into the standard input of a command.
grep -R "Bob" worldbanc/private/transactions --exclude-dir="backups" | wc -l
#This command searches transactions for "Bob" and then takes that and put it into the word count command with the -l flag which counts the lines and it return the value of 3973 which is the count of lines Bob appeared in

#Interrupt
#You can use ctrl+c to interrupt a command or quit a command this sends a SIGINT which is designed to end a command

#Kill
#Sometimes a program is in such a bad state (or is so malicious) that it doesn't respond to the SIGINT, 
# in which case the best option is to use another shell session (new terminal window) to manually kill the program.
#Syntax
kill <PID>
#PID stands for "process ID." Every process that's running on your machine has a unique ID. The ps, "process status" command can be used to list the processes running on your machine, and their IDs:
ps aux
#The "aux" options just mean "show all processes, including those owned by other users, and show extra information about each process."
#If a process is out of control and not listening you may need to enter the kill command from another terminal to stop the process with the process ID
#To find the ID I used, ps aux | grep worldbanc/private/bin/malicious.sh

#UNIX philosophy
#Write programs that do one thing and do it well
#write programs that work well together
#Write Programs to Handle Text Streams, Because That Is a Universal Interface
# This point is more the "how" of the previous point. Programs work together easily when they all use the same interface: text streams. 
# A text stream is just a sequence of characters that can be read or written sequentially. In other words, a text stream is just text.

#Top
# The top command is a powerful tool that allows you to see which programs are using the most resources on your computer. It is like task manager for windows but for command line
# By default, top sorts the processes by CPU usage, with the most CPU-intensive processes at the top. 
# Another useful resource to sort by is memory (RAM) usage. To sort by memory usage, press M (uppercase) while top is running. 
# On macOS, you can either start top sorted by memory with top -o mem from the shell, or, while top is running, press o, then type mem and press Enter to sort by memory.
# to exit top you press q to quit

＃Package Managers
#Package managers help you with:
#Downloading software from official sources
#Installing software
#Updating software
#Removing software
#Managing dependencies

Common paackage managesr include:
# APT for Ubuntu (this is default)
# Brew for MacOS (there is no default for MacOS but Homebrew is the most popular)
#the command for Brew is brew e.g. brew install
#For your edification, take a look at where your package manager installed nvim on your filesystem. The which command will help: which nvim

#Neovim
#Don't be fooled, exiting Vim (or Neovim) is one of the greatest hurdles you must overcome as a developer. It's a rite of passage. It's a badge of honor.
#You must switch between modes in neovim, normal and insert mode
#Enter insert mode by by pressing i in normal mode
#Escape insert mode by pressing escape
# write to a file while in Vim using :w
# Quit vim by using :q

#Webi
# Webi lets you install command line tools directly from the web, with no need for a traditional package manager like apt or brew. 
# You don't need to install Webi itself at all; instead, you just run a shell command that downloads and runs a given tool's official installer script.
# Installed lsd, LS Deluxe, whihc is like the ls command but with more feature. 
#curl -sS https://webi.sh/lsd | sh; \
#source ~/.config/envman/PATH.env

#lsd
#lsd --tree will print a folder tree
#lsd -- classic will print things without the colours