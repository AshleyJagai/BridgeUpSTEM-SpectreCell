# Git and Github: Keeping track of your files

## Learning Objectives

- Introduction to internship, department, and culture
- Communication tools
- Expectations/Daily happenings

<hr>

## What is Git?

Git is a tool that allows you to share files from your local (or personal) computer to another computer that acts as a hub, allowing you (and others) to access your files from any other computer.

<hr>

## Need to add an SSH key?
Set up an SSH key instead of having to log in all the time!
 https://help.github.com/articles/generating-an-ssh-key/

## Create a Repository

 1. Log into your [Github](https://github.com/) account
 2. Click on "+" sign or ]green "New Repository" button
 3. Name your new repo and create it!

## Clone Your Repository

 1. Copy the url from the "Quick Setup" section on the next page.
 2. cd to the folder you store your code in terminal (or make a new one)
 3. type "git clone " followed by your pasted repo url.

## Make Changes to Your Local Repository
 1. create a readme.md
 2. add some content and save
 3. stage it with "git add"
 4. commit
 5. push to remote repository
 6. pull from the repository to make sure you have the latest code.

 <hr>

## Fork a repository

Forking a repository lets you play with the code and save it to your own repo without affecting the owner's code!

 1. go to [lesson repo](https://github.com/colleencleary/BridgeUp-Ghost.git)
 2. click on the Fork button
 3. choose who you want to save it (should be your username)
 4. clone it to your local computer in terminal.
 5. add/commit/push like normal!

## Updates from original repo

 1. In terminal, add original repo with `git remote add upstream https://github.com/colleencleary/BridgeUp-Ghost.git`
    - doesn't have to be called "upstream", but that's the convention
 2. `git pull upstream master` to update your forked repo
