
# Macuyler's Automation Cli (MAC)
This is a cli tool for automating all the things I don't want to do!    

## Structure
- mac
  - install (Install scripts from github into a bin)
  - remove  (Remove installed scripts)
  - upgrade (Upgrade an install scripts)

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



