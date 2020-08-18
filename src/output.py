"""
src.output:
 * Output functions for use throughout the code.
"""

def log(txt=None, err=False, blank=False, pad=False, dunn=False):
    # Print a formatted log to the user
    if pad:
        print()
    if blank:
        print(txt)
    elif err:
        print(f' ! {txt}')
    elif dunn:
        print(' % All Dunn!\n')
    else:
        print(f' % {txt}')
    return

def show_usage(commands=[], sub=None):
    # Print a formatted usage statement.
    """
    commands: a list of strings to be printed as commands.
    sub: a string to be printed as a subcommand or a list of
     strings to be printed as a multiline subcommand.
    """
    print('\n Usage: ')
    for cmd in commands:
        print(f'  - mac {cmd}')
    if sub != None:
        if type(sub) == list:
            sub = '\n'.join(sub)
        print(f'  - mac {sub}')
    print()
    return

