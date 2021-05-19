# we assume the directory structure of this and the remote directory are the same
# we look for files on 'this' that have been updated since 'last_update' (or whatever i end up calling them)

import os

SRC = 'this'
TGT = 'that'
LAST_COPIED = 'last'


def run(params):
    root = params[SRC]
    dest = params[TGT]
    time = params[LAST_COPIED]

    if dest is not None and root is not None and time is not None:
        copy(root, dest, time)


# root is top parent of file tree
# dest is top parent of destination file tree
# time is the last time a backup was done
def copy(root, dest, time):
    xs = ['']  # xs is always the file path relative to root

    while xs:
        cur = xs.pop()
        if os.path.exists(dest+cur):
            cur_dir_contents = list_relative_directories(root, cur)
            xs = xs + cur_dir_contents
            backup_files(root, dest, cur, time)
        else:  # handles the case where the directory has not yet been backed up
            copy_all_sub_files(root, dest, cur)


def list_relative_directories(root: str, stub: str):
    xs = os.listdir(root+stub)
    ys = []
    for x in xs:
        path = (stub+'/'+x)[1:]
        if os.path.isfile(path):
            ys.append((stub+'/'+x)[1:])
    return ys


# in this function, we want to either copy over new files or recopy those that have been modified since time
# we accept a root and a dest with a exiting /
def backup_files(root: str, dest: str, stub: str, time: int):
    files = os.listdir(root+stub)

    for f in files:
        full_path = root+stub+f
        # this if is a catchall for both new files and modified since last backup
        if os.path.isfile(full_path) is True and os.path.getmtime(full_path) > time:
            copy_file(root, dest, stub+f)


def copy_file(root, dest, stub):
    import shutil
    shutil.copyfile(root+stub, dest+stub)


def copy_all_sub_files(root, dest, stub):
    import shutil
    shutil.copytree(root+stub, dest+stub)
