# Git Bin

A utility that allows you to quickly clone github repos and automatically add them to your path.

## Structure

- gb
  - install (Install git repos)
  - remove  (Remove installed repos)
  - upgrade (Upgrade installed repos)

## Setup

1. Run the following:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/macuyler/gitbin/master/bin/install.sh)"
```

2. Add the following to your shell rc file (bashrc, zshrc, etc.)

```
export PATH="$PATH$(cat ~/.gitbin/.path)"
```

## Upgrading

To upgrade your version of _gitbin_, you can use the following command:

```
gb upgrade gitbin
```
