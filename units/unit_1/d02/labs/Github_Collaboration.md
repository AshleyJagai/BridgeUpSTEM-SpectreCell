# Paired Activity

By collaborating over Github, each pair will add something to a readme file in a shared repository via Git/Github workflow.

- Choose one member's new repo to be shared. The 'owner' should add the other member as a collaborator in settings.
- collaborator should accept invitation sent via email. Make sure to `git clone` in a new directory in terminal for a local version

### Create a new branch

Work your way through instructions as a team.

1. `cd` to your local repository
2. `git checkout -b dev` to create new branch called `dev`
  - the `master` branch should only be used for production-ready (aka working) code
3. pull from the master branch to update your code
4. COLLABORATOR: open readme.md and add your name.
5. COLLABORATOR: save, add, commit - **make sure your commit message is meaningful!**
6. COLLABORATOR: `git push origin dev` to submit changes to the `dev` branch.
7. COLLABORATOR: start a pull request on Github
8. OWNER: compare and merge teammate's changes on Github.
  - if no merge conflicts appear, then confirm merge with `master` branch.
9. pull from the master branch to update your code
10. OWNER: follow steps 4-8
11. pull from the master branch to update your code

That's it! Not bad, right? As we develop our code, this process will get more tricky, but we'll address issues as they come up.

## Fork a repository

Forking a repository lets you play with the code and save it to your own repo without affecting the owner's code!

 1. go to [lesson repo](https://github.com/amnh/BridgeUP-STEM-SpectreCell)
 2. click on the Fork button
 3. choose the account to save it to (should be your username)
 4. cd to an easy-to-find directory in terminal (we'll be using this all year after all!)
 5. clone it to your local computer
 6. add/commit/push like normal!

## Updates from original repo

 1. In terminal, add original repo with `git remote add upstream https://github.com/amnh/BridgeUP-STEM-SpectreCell.git`
    - doesn't have to be called "upstream", but that's the convention
 2. `git pull upstream master` to update your local copy

  <hr>
