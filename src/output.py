
def log(txt=None, err=False, blank=False, pad=False, dunn=False):
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
    print('\n Usage: ')
    for cmd in commands:
        print(f'  - mac {cmd}')
    if sub != None:
        print(f'  - mac {sub}')
    print()
    return

