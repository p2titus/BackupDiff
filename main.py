import diff_copy
import json

PARAM_FILE = 'params.json'


def main():
    print('welcome to diff backup updater')
    print('please check %s to ensure all fields are correct' % PARAM_FILE)
    x = '1'
    # x = input('enter 1 to perform a remote backup using the specified parameter json\n')
    if x == '1':
        import diff_copy
        params = get_params(PARAM_FILE)
        diff_copy.run(params)
        success(params, PARAM_FILE)
    print('program terminating')


def success(params, write_file):
    import time
    import calendar

    cur_time = calendar.timegm(time.gmtime())
    params[diff_copy.LAST_COPIED] = cur_time
    to_write = json.dumps(params)

    file = open(write_file, 'w')
    file.write(to_write)
    file.close()


def get_params(filename):
    """return {diff_copy.SRC: '~/Documents/test/src/',
            diff_copy.TGT: '~/Documents/test/dest/',
            diff_copy.LAST_COPIED: 0}"""  # default values
    import os

    if filename is not None and os.path.exists(filename):
        with open(filename, 'r') as file:
            data = file.read()
            params = json.loads(data)

    else:
        dct = {}
        src_dir = input('please input the top level of the source to be backed up\n')
        dct[diff_copy.SRC] = src_dir
        dest_dir = input('please input the top level of the destination directory\n')
        dct[diff_copy.TGT] = dest_dir
        # assume first time
        dct[diff_copy.LAST_COPIED] = 0
        params = dct

    return params


if __name__ == '__main__':
    main()

