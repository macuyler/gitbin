
# Macuyler's Automation Cli (MAC)
This is a cli tool for automating all the things I don't want to do!    

## Features
 - **macbin**: A utility that allows you to quickly clone github repos and automatically add them to your path.

## Structure
- mac
  - install (macbin | Install repos from github)
  - remove  (macbin | Remove installed repos)
  - upgrade (macbin | Upgrade installed repos)

## Setup
1. Run the following:
```
cd /some/dir
git clone https://github.com/Macuyler/mac.git
```
2. Add the following to your shell rc file (bashrc, zshrc, etc.)
```
export PATH="$PATH:/some/dir/mac"
export PATH="$PATH$(cat ~/.macbin/.path)"
```
***Note**: You will get an error until the `~/.macbin/.path` file is created. It is recommended that you either install a script with `mac install` or manually create that file to prevent this error.*



