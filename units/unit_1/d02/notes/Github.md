# Terminal, Git, and Github: Keeping track of your files

## Learning Objectives

- Terminal
- What is Git?
- Creating and cloning a repository
- Create a branch
- Push branch to repo
- Create a pull request to the original repository
- Merge branches
- Fork a repository
- Update from original repo


<hr>

## Terminal

### Key Coding Characters

- `/` - slash or forward slash (above enter/return)
- `\` - backslash (shares key with ?)
- `~` - tilda (upper left, below the `esc` key)
- ` - backtick (shares key with ~)
- `()` - parenthesis
- `[]` - brackets
- `{}` - curlies (non-offial name)
- `|` - pipe (shares key with backslash)
- `&` - ampersand or and symbol
- `;`- semi-colon
- `:` - colon

### Open terminal
- `⌘ (Command) + Space`, or open Spotlight
- type "Terminal"
- `Enter`

#### Keep Terminal in your dock for easy access -- we'll be using it every day!!

### Commands in Terminal

- `pwd` - tells you the path to your location
- `ls` - lists everything in the current directory
- `cd` - navigate through directories
  - `cd ..` - shorthand for parent directory
- `mkdir` - make a new directory
- `touch` - easy way to create an empty file
- `jupyter notebook` - opens up jupyter notebook

Use TAB to complete file names and up/down arrows to reuse recent commands.



## What is Git?

Git is a tool that allows you to share files from your local (or personal) computer to another computer that acts as a hub, allowing you (and others) to access your files from any other computer.

<hr>

## Need to add an SSH key?
Set up an SSH key instead of having to log in all the time!
 https://help.github.com/articles/generating-an-ssh-key/

## Create a Repository

 1. Log into your [Github](https://github.com/) account
 2. Click on "+" sign or green "New Repository" button
 3. Name your new repo and create it!

## Clone Your Repository

 1. Copy the url from the "Quick Setup" section on the next page.
 2. cd to the folder you store your code in terminal (or make a new one)
 3. type "git clone " followed by your pasted repo url.

## Make Changes to Your Local Repository
 1. create a readme.md
 2. add some content and save
 3. stage it with `git add`
 4. `commit`
 5. `push` to remote repository
 6. `pull` from the repository to make sure you have the latest code.

 <hr>
