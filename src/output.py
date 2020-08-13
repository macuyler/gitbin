
def show_usage(commands=[], sub=None):
    print('\n Usage: ')
    for cmd in commands:
        print(f'  - mac {cmd}')
    if sub != None:
        print(f'  - mac {sub}')
    print()
    return

