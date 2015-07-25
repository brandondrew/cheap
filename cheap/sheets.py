from cheap import cheatsheets
from cheap.utils import *
import os

def default_path():
    """ Returns the default cheatsheet path """

    # determine the default cheatsheet dir
    default_sheets_dir = os.environ.get('DEFAULT_CHEAP_DIR') or os.path.join(os.path.expanduser('~'), '.cheap')

    # create the DEFAULT_CHEAP_DIR if it does not exist
    if not os.path.isdir(default_sheets_dir):
        try:
            # @kludge: unclear on why this is necessary
            os.umask(0000)
            os.mkdir(default_sheets_dir)

        except OSError:
            die('Could not create DEFAULT_CHEAP_DIR')

    # assert that the DEFAULT_CHEAP_DIR is readable and writable
    if not os.access(default_sheets_dir, os.R_OK):
        die('The DEFAULT_CHEAP_DIR (' + default_sheets_dir +') is not readable.')
    if not os.access(default_sheets_dir, os.W_OK):
        die('The DEFAULT_CHEAP_DIR (' + default_sheets_dir +') is not writeable.')

    # return the default dir
    return default_sheets_dir


def get():
    """ Assembles a dictionary of cheatsheets as name => file-path """
    cheats = {}

    # otherwise, scan the filesystem
    for cheapdir in reversed(paths()):
        cheats.update(
            dict([
                (cheap, os.path.join(cheapdir, cheap))
                for cheap in os.listdir(cheapdir)
                if not cheap.startswith('.')
                and not cheap.startswith('__')
            ])
        )

    return cheats


def paths():
    """ Assembles a list of directories containing cheatsheets """
    sheet_paths = [
        default_path(),
        cheatsheets.sheets_dir()[0],
    ]

    # merge the CHEAPPATH paths into the sheet_paths
    if 'CHEAPPATH' in os.environ and os.environ['CHEAPPATH']:
        for path in os.environ['CHEAPPATH'].split(os.pathsep):
            if os.path.isdir(path):
                sheet_paths.append(path)

    if not sheet_paths:
        die('The DEFAULT_CHEAP_DIR dir does not exist or the CHEAPPATH is not set.')

    return sheet_paths


def list():
    """ Lists the available cheatsheets """
    sheet_list = ''
    pad_length = max([len(x) for x in get().keys()]) + 4
    for sheet in sorted(get().items()):
        sheet_list += sheet[0].ljust(pad_length) + sheet[1] + "\n"
    return sheet_list


def search(term):
    """ Searches all cheatsheets for the specified term """
    result = ''

    for cheatsheet in sorted(get().items()):
        match = ''
        for line in open(cheatsheet[1]):
             if term in line:
                  match += '  ' + line

        if not match == '':
            result += cheatsheet[0] + ":\n" + match + "\n"

    return result
