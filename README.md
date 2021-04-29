
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
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/macuyler/mac/master/bin/install.sh)"
```

2. Add the following to your shell rc file (bashrc, zshrc, etc.)
```
export PATH="$PATH$(cat ~/.macbin/.path)"
```

## Upgrading
To upgrade your version of _mac_, you can use the following command:
```
mac upgrade mac
```
