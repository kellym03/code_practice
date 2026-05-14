# Quick Lookup of commands
"""
git status
git add
git commit
git push
git pull
git log (--no-pager log -n 10)

git apply
git commit-tree
git hash-object
"""


#Learn git
#command syntax
#Arguments in angle brackets <> are mandatory and must be provided when running the command.
#Arguments in square brackets [] are optional and can be included if needed.

#Git manual 
git help git

#Manual shortcuts
"""
q: Quits the manual
j: One line down
k: One line up
d: Half page down
u: Half page up
/<term>: Search for "term"
n: Next search term
N: Previous search term
"""

#Git has porcelain commands and plumbing commands
#The porcelain is what I will interact with most in the course
#Some commands are
"""
git status
git add
git commit
git push
git pull
git log
"""
#Some plumbing commands are:
"""
git apply
git commit-tree
git hash-object
"""

#git status
"""
what can be returned by git status
untracked: Not being tracked by Git
staged: Marked for inclusion in the next commit
committed: Saved to the repository's history
The git status command shows you the current state of your repo. It will tell you which files are untracked, staged, and committed.
"""

#Staging
#The contents.md file has been created, but as we saw, it's untracked. We need to stage it (add it to the "index") with the git add command before committing it later.
#Without staging, no files are included in the commit – only the files you explicitly git add will be committed.

#git add <path-to-file OR pattern>

#git commit
#to save a snapshot of your repo you commit it to the repo. All snapshots contain a message with them. The command is below:
#git commit -m "my message"

"""
Learn what this means, command to check the previous commit?
git --no-pager log -n 1
"""

#git log
#A commit hash is a long string of numbers that acts as a unique identifier that uniquely identifies the commit.
# For convenience, you can refer to any commit or change within Git by using the first 7 characters of its hash. For mine, that's 5ba786f.
# -n and --no-pager options to limit the maximum number of commits shown, and more importantly, to run it without the interactive pager. E.g.:
git --no-pager log -n 10


#Commit Hashes
#All this to say that hashes are effectively unique in practice. While SHA-1 collisions are possible under contrived conditions, you won't accidentally create two different commits with the same hash, and because they're generated automatically for you, you don't need to worry too much about what goes into them right now.
#Hash = SHA - SHA-1 is just a cryptographic function 

#The plumbing
#Git is made up of objects that are stored in the .git/objects directory. A commit is just a type of object.
#ls -l .git/objects to list the contents of the .git/objects directory. -l means long and it will list all the contents in their long form

#cat-file
# cat-file allows us to see the contents of a commit without needing to futz around with the object files directly
# You can redirect the catfile command output to a file using the command, git cat-file -p 4aeaea0cdaccbd12f2479a3a500519afc701c1b3 > /tmp/catfileout.txt - the long number is the hash of the commit
# You can check the catfile by running that same command without the redirect 
# -p is for pretty print 

#Trees and blobs
#tree is git's way of storing a directory
#blob is git's way of storing a file
#When we run the cat file command we cannot see the contents of the file committed itself! That's because the blob object stores it.
#if we run git cat-file -p <tree hash> it will show the blob hash and then if we run the command with the blob hash we can see the contents itself of the committed file(s)
# the -p is really important on a commit has otherwise you're going to get a lot of text about the commit

#titles.md blob hash - 66693b8d72daef9170108c6ab4b3abd7f3950dd2

#Git Config
#Git stores author information so that when you're making a commit it can track who made the change. Here's how you might update your global Git configuration (don't do this yet):

git config set --global user.name "ThePrimeagen"
git config set --global user.email "the.primeagen@aol.com"

git config set --append webflyx.ceo "Warren" #By default, git config set refuses to write to a key that already has multiple values unless you specify how to handle them. Using --append tells Git to simply add your new value as an additional line for that key.



"""
git config: The command to interact with your Git configuration.
set: The subcommand to set a value – i.e., to add it if it doesn't already exist, or update it if it does.
--global: Flag stating you want this configuration to be stored globally in your ~/.gitconfig. The opposite is --local, which stores the configuration in the current repository only.
user: The section.
name: The key within the section.
"ThePrimeagen": The value you want to set for the key.
"""

#Git has a command to view the contents of your config:
git config list --local

#You can also just view the contents of your local config file directly:
cat .git/config

#get sub command 
# can get the values of keys using the get sub command - a bit like dictionaries in python git config get webflyx.valuation
git config get <key>

#Unset
#The unset subcommand is used to remove a configuration value. For example:
git config unset <key>
#Need to be specific with a key to unset

#Duplicates
#Typically, in a key/value store, like a Python dictionary, you aren't allowed to have duplicate keys. Strangely enough, Git doesn't care.
#Unset All
#The unset --all command is useful if you ever really want to purge all instances of a key from your configuration. 
# Conversely, the unset subcommand by itself only works with a single instance of a key.
git config unset --all example.key

#Remove section
git config remove-section <section>
#The dot notation allows you to define section within the git config

#Locations
#|--System
#|----Global - overrides system
#|------Local - overrides global
#|--------Worktree - overrides local

#these define the scope of the git config. 90% of the time it will be in global to set things like username and email, 9% of the time it will be in local and the other 1% it will be in system and worktree

## Branching
#If you want to work on a specific thing in a project you can create a branch rather than working directly on the whole project/master/main branch.
# If you like the changes you can merge the change back in or delete the branch if you don't like it

#A branch is just a pointer to a specific commit. A new branch is a new pointer to a specific commit
git branch #allows you to check what branch you're on

#hHw to rename a branch
git branch -m oldname newname

#How to change the default branch for all future projects
git config --global init.defaultBranch main

#New Branches
#Two Ways to Create a Branch
git branch my_new_branch

#This creates a new branch called my_new_branch. 
# The thing is, I rarely use this command because usually I want to create a branch and switch to it immediately. So I use this command instead:
git switch -c my_new_branch #-c is the create flag

#When you create the new branch you can imagine a branch coming out from the tree but you still need to commit something to it while you're working on it. 

#git checkout - the old way to switch branches
git switch prime

# or, the old way:
git checkout prime

#Log flags
git log --decorate=full # shows you everything that is going on 
git log --decorate=no # shows you the branch names that are no longer shown at all
git log --oneline # A more compact view of the log and much easier to see what is going on

#Git Files
#Remember, Git stores all its information in files in the .git subdirectory at the root of your project, even information about branches. The "heads" (or "tips") of branches are stored in the .git/refs/heads directory. 
# If you cat one of the files in that directory, you should be able to see the commit hash that the branch points to.

.git/refs/heads #contains one file for each branch, containing the commit hash that the branch points to 


cat .git/refs/heads/main
#contains one file for each 

#can get an ascii art of the branches
git log --oneline --graph --all

#Merges / Merging
git merge <branch name> #Will merge two branches in git

#The merge will:
#Find the "merge base" commit, or "best common ancestor" of the two branches. In this case, A.
#Replay the changes from main, starting from the best common ancestor, into a new commit.
#Replay the changes from vimchadsonly onto main, starting from the best common ancestor.
#Records the result as a new commit, in our case, F.
#F is special because it has two parents, C and E.
#A - B - C - F    main
#   \     /
#    D - E        vimchadsonly

#Note that you changed the default merge editor to vscode from vim
#the below code will show the pretty merge tree
git --no-pager log --oneline --decorate --graph --parents

#Each asterisk * represents a commit in the repository. 
# There are multiple commit hashes (7 digits) on each line because the --parents flag logs the parent hash(es) as well.

#Fast forward merge
#The simplest type of merge is a fast-forward merge. Let's say we start with this:
      C     delete_vscode
     /
A - B       main

#And then we run
git merge delete_vscode

#Because delete_vscode has all the commits that main has, Git automatically does a fast-forward merge. 
# It just moves the pointer of the "base" branch to the tip of the "feature" branch:
            delete_vscode
A - B - C   main

#Notice that with a fast-forward merge, no merge commit is created.
#This is a common workflow when working with Git on a team of developers:
#1. Create a branch for a new change
#2. Make the change
#3. Merge the branch back into main (or whatever branch your team dubs the "default" branch)
#4. Remove the branch
#5. Repeat

#Can delete the branches with -d flag, e.g.:
git branch -d add_classics


#Fast Forward Commit
#This is the result of a fast forward merge

#Rebase vs Merge
#Visualising rebase - say there is a tree like the below
A - B - C    main
   \
    D - E    feature_branch
#We're working on feature_branch, and want to bring in the changes our team added to main so we're not working with a stale branch. 
# We could merge main into feature_branch, but that would create an additional merge commit. 
# Rebase avoids a merge commit by replaying the commits from feature_branch on top of main. 
# After a rebase, the history will look like this:
A - B - C         main
         \
          D - E   feature_branch

#You can fork from specific commits into a new branch by providing the specific commit hash in the git switch command:
git switch -c update_dune COMMITHASH

#When running the rebase command (git rebase main) it will do the following:
#Identify the latest commit from main and use it as the temporary new base for the rebase process
#Replay each commit from <not main branch> one at a time onto this temporary location
#Update the <not main branch> to point to the last replayed commit in the temporary location, making this the new permanent <not main branch>.
#The rebase does not affect the main branch; <not main branch> now includes all changes from main.

#If you want to tack a commit onto the most previous commit you can amend it with the following command
git commit --amend --no-edit

#When to rebase
#git rebase and git merge are different tools.
#An advantage of merge is that it preserves the true history of the project. 
# It shows when branches were merged and where. 
# One disadvantage is that it can create a lot of merge commits, which can make the history harder to read and understand.
#A linear history is generally easier to read, understand, and work with. 
# Some teams enforce the usage of one or the other on their main branch, but generally speaking, you'll be able to do whatever you want with your own branches.

git rebase main 

#Warning
#You should never rebase a public branch (like main) onto anything else. 
# Other developers have it checked out, and if you change its history, you'll cause a lot of problems for them.
#However, with your own branch, you can rebase onto other branches (including a public branch like main) as much as you want.
#In other words, don't change the hisotry of a public main branch. But you can change the history of a your own private branches. So you'll be working on your branch and rebase with main but not working on main and rebasing with a different history.

#Git reset soft
#The git reset command can be used to undo the last commit(s) or any changes in the index (staged but not committed changes) and the worktree (unstaged and not committed changes).
git reset --soft COMMITHASH

#git reset hard
git reset --hard COMMITHASH
#DANGER - This will reset your working directory and index to the state of that commit, and all the changes made after that commit are lost forever.

#Git remote
#This is where the "distributed" in "distributed version control system" comes from. 
# We can have "remotes," which are just external repos with mostly the same Git history as our local repo.
#When it comes to Git (the CLI tool), there really isn't a "central" repo. 
# GitHub is just someone else's repo. Only by convention and convenience have we, as developers, started to use GitHub as a "source of truth" for our code.

#Adding the remote
#In git, another repo is called a "remote." 
# The standard convention is that when you're treating the remote as the "authoritative source of truth" (such as GitHub) you would name it the "origin".
#By "authoritative source of truth" we mean that it's the one you and your team treat as the "true" repo. 
# It's the one that contains the most up-to-date version of the accepted code.

git remote add <name> <uri>

#In the assignment i set up the new repo webflyx-local with the webflyx repo as the remote origin for the new "local" one. The command that was used this repo is the below
git remote add origin ../webflyx #it used a relative pathing for the uri of the repo

#Fetch
#check the contents of the new repo with 
find .git/objects

#to download copies of the content in the remote assigned repo you use
git fetch

#Log remote
#The git log command isn't only useful for your local repo. You can log the commits of a remote repo as well!
git log [<remote>/<branch>]

#For example, if you wanted to see the commits of a branch named primeagen from a remote named origin you would run:
git log origin/primeagen

#If you want to see the log of a specific branhc you could also use
git --no-pager log origin/update_dune --oneline

#Remote Merge
#Just as we merged branches within a single local repo, we can also merge branches between local and remote repos.
git merge [<remote>/<branch>]

#For example, if you wanted to merge the primeagen branch of the remote origin into your local main branch, you would run this inside the local repo while on the main branch:
git merge origin/primeagen

#github remote repo
#Add a remote repo on github for the local repo to push and pull from
git remote add origin https://github.com/your-username/repo-name.git

#git push
git push origin main

#can push a new branch you made locally to the remote repo with something like 
git push origin <new branch name>

#ensure git will merge on a pull
git config set pull.rebase false

#Pull requests
#When you push locally to a remote origin it will create a pull request sothat the maintainer of the repo can manage the incoming push request from the local repo
#Pull requests allow team members to see what changes are being proposed and to discuss them before they are merged into the main codebase.

#Prime's Workflow
#While on the topic of pull requests, I want to share a note on my simple workflow. 90% of the time, you're only using a handful of git commands to get your coding work done.

#Keep Stuff on GitHub
#I keep all my serious projects on GitHub. That way if my computer explodes, I have a backup, and if I'm ever on another computer, I can just clone the repo and get back to work.

#Rebase vs. Merge
#I've configured Git to rebase by default on pull, rather than merge so I keep a linear history. If you want to do the same, you can add this to your global Git config:

git config set --global pull.rebase true

#Prime's Solo Workflow
#When I'm working by myself, I usually stick to a single branch, main. I mostly use Git on solo projects to keep a backup remotely and to keep a history of my changes. I only rarely use separate branches.

#Make changes to files
git add . (or git add <files> if I only want to add specific files)
git commit -m "a message describing the changes"
git push origin main
#It really is that simple for most solo work. git log, git reset, and some others are, of course, useful from time to time, but the above is the core of what I do day-to-day.

#My Team Workflow
#When you're working with a team, Git gets a bit more involved (and we'll cover more of this in part 2 of this course). Here's what I do:

#Update my local main branch with git pull origin main
#Checkout a new branch for the changes I want to make with git switch -c <branchname>
#Make changes to files
git add .
git commit -m "a message describing the changes"
git push origin <branchname> (I push to the new branch name, not main)
#Open a pull request on GitHub to merge my changes into main
#Ask a team member to review my pull request
#Once approved, click the "Merge" button on GitHub to merge my changes into main
#Delete my feature branch, and repeat with a new branch for the next set of changes

#Git Ignore
.gitignore
#A problem arises when we want to put files in our project's directory, but we don't want to track them with Git. 
# A .gitignore file solves this. For example, if you work with Python, you probably want to ignore automatically generated files like .pyc and __pycache__. 
# If you are building a server, you probably want to ignore .env files that might hold private keys. 
# If you (I'm sorry) work with JavaScript, you might want to ignore the node_modules directory.

#Here's example contents of a .gitignore file, which exists at the root of a repo:

node_modules
.env

#This will ignore every path containing node_modules as a "section" (directory name or file name). It ignores:

node_modules/code.js
src/node_modules/code.js
src/node_modules
#It does not ignore:

src/node_modules_2/code.js
env/node_modules_3
src/node_modules.js
#This will also ignore the .env file preventing you from committing sensitive environment variables (like API keys, DB credentials, etc.) ...cause that would be bad.

#work out what the below does
git show --name-only --pretty=""

#Patterns
#It would be rough if .gitignore files only accepted exact filepath section names. Luckily, they don't!

#Let's go over some of the most common patterns.

#Wildcards
#The * character matches any number of characters except for a slash (/). For example, to ignore all .txt files, you could use the following pattern:

#*.txt

#This would ignore files like /princess_diaries.txt and /contacts/your_mom.txt since they're both .txt files.

#Rooted Patterns
#Patterns starting with a / are anchored to the directory containing the .gitignore file. For example, this would ignore a main.py in the root directory, but not in any subdirectories:

#/main.py

#This ignores /main.py but not /src/main.py since /src is a subdirectory.

#Negation
#You can negate a pattern by prefixing it with an exclamation mark (!). For example, to ignore all .txt files except for important.txt, you could use the following pattern:

#*.txt
#!/important.txt

#This would not ignore /important.txt, but would ignore /self_affirmations/important.txt.

#Comments
#You can add comments to your .gitignore file by starting a line with a #. For example:

# Ignore all .txt files
#*.txt

#Comments are especially helpful when doing something unconventional or complex, especially when collaborating.

#Order Matters
#The order of patterns in a .gitignore file determines their effect, and patterns can override each other. For example:

#temp/*
#!temp/instructions.md

#Everything in the temp/ directory would be ignored except for instructions.md. If the order were reversed, instructions.md would be ignored.

#What to Ignore
#We've talked about how to ignore files, but the deeper question is what should you ignore? Here are some rules of thumb for coding projects:

#Ignore things that can be generated (e.g. compiled code, minified files, etc.)
#Ignore dependencies (e.g. node_modules, venv, packages, etc.)
#Ignore things that are personal or specific to how you like to work (e.g. editor settings)
#Ignore things that are sensitive or dangerous (e.g. .env files, passwords, API keys, etc.)