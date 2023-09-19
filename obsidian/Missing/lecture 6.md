
https://learngitbranching.js.org/

**Useful git commands:**
`git init` will set up a folder for use with git.
`git status` will give info about the status of git
`git cat-file <hash>` will sho something similar to git log
`git log` shows info about the latest(?) commit
`git commit -a` commits all changes since last commit, but does not include new files
`git log --all --graph --decorate` shows graph of commits
`git checkout <hash>` moves the head (and state of the files that are kept track of) to that node in the tree. 
`git diff` shows differences between current commit and another one (by default the last one)
`git remote add <name> <url>` adds a new remote
`git push remote <local branch>:<remote branch>` pushes changes to the remote
`git clone <url> <local dir>` download the remote version to a directory
`git branch --set-upstream-to=<remotename/branch>` this allows you to do `git push` without parameters. The branches are synced.
`git fetch` will check for remote changes
`git pull` will fetch remote changes and merges them with local machine. 


