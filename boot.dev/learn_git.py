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

