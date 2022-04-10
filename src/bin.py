"""
src.bin:
 * Source code for all gitbin functionallity.
"""

from pathlib import Path
from subprocess import PIPE, Popen

from src.output import log, show_usage

NO_FOD = 'No such file or directory'
FATAL = 'fatal: '
COULD_NOT_READ = 'Could not read from remote repository.'


def get_installed():
    """Return a list of installed packages."""

    installed = []
    proc = Popen('ls ~/.gitbin', shell=True, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    if NO_FOD in err.decode():
        Popen('mkdir ~/.gitbin', shell=True).communicate()
    elif b'\n' in out:
        installed = list(map(lambda pkg: pkg.decode(), out.split(b'\n')))
        installed = list(filter(lambda pkg: len(pkg) > 0, installed))
    return installed


def install(args):
    """Install a package to your gitbin."""

    install_usage = [
        'install git-repo [-p]\n',
        '  # Options:',
        '    * -p /path/to/bin',
        '      (Example: -p /bin) (Note: Must start with / )'
    ]

    pkgs = get_installed()
    if len(args) >= 1:
        url = args[0]
        binpath = ''
        if len(args) == 3 and args[1] == '-p':
            binpath = args[2]
        elif len(args) != 1:
            show_usage(sub=install_usage)
            return
        url_split = url.split('/')
        name = url_split[len(url_split) -1].replace('.git', '')
        log(f'Cloning {name} from {url}', pad=True)
        if name not in pkgs:
            _, err = Popen(f'cd ~/.gitbin/ && git clone {url}',
                           shell=True, stderr=PIPE).communicate()
            if FATAL not in err.decode():
                with open(f'{Path.home()}/.gitbin/.path', 'a')  as path:
                    path.write(f':{Path.home()}/.gitbin/{name}{binpath}')
                    path.close()
                log(f'Successfully installed {name}!')
            else:
                log(err.decode(), blank=True, pad=True)
                log(f'Failed to install {name}!', err=True)
        else:
            log(f'Package called "{name}" already installed!', err=True)
        log(dunn=True)
    else:
        show_usage(sub=install_usage)
    return


def remove(args):
    """Remove a package from your gitbin."""

    pkgs = get_installed()
    if len(args) == 1:
        name = args[0]
        log(f'Removing {name} from gitbin', pad=True)
        if name in pkgs:
            Popen(f'rm -rf ~/.gitbin/{name}', shell=True).communicate()
            new_path = []
            with open(f'{Path.home()}/.gitbin/.path', 'r') as path:
                path_split  = path.readline().strip().split(':')
                fps = list(filter(lambda x: x.replace(f'{Path.home()}/.gitbin/', '')
                                  .split('/')[0] != name, path_split))
                new_path = ':'.join(fps)
                path.close()
            with open(f'{Path.home()}/.gitbin/.path', 'w') as path:
                path.write(new_path)
                path.close()
            log(f'Successfully removed {name}')
        else:
            log(f'Package called "{name}" not installed!', err=True)
        log(dunn=True)
    else:
        show_usage(sub='remove pkg-name')


def upgrade(args):
    """Upgrade a package in your gitbin."""

    pkgs = get_installed()
    if len(args) == 1:
        name = args[0]
        log(f'Upgrading {name} from gitbin', pad=True)
        if name in pkgs:
            _, err = Popen(f'cd ~/.gitbin/{name} && git pull',
                           shell=True, stdout=PIPE, stderr=PIPE).communicate()
            if COULD_NOT_READ in err.decode():
                log(err.decode(), blank=True, pad=True)
                log(f'Failed to upgrade {name}!', err=True)
            else:
                log(f'Successfully upgraded {name}!')
        else:
            log(f'Package called "{name}" not installed!', err=True)
        log(dunn=True)
    else:
        show_usage(sub='upgrade pkg-name')
