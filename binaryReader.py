import sys
import argparse
import math

def tohex(s):
    return ''.join([hex(ord(i))[2:] for i in s]).upper()

def todots(s):
    return ''.join([unichr(0x2800 + ord(i)) for i in s])

def todots_pprint(s):
    s = todots(s)
    l = len(s)
    n_line = int(math.ceil(len(s)/64.))
    lines = []
    for i in range(n_line):
        no = hex(i)[2:]
        line = '0x' + '0'*(6-len(no)) + no + ' '
        line += ' '.join([s[i*64+j*8:i*64+j*8+8] for j in range(8)])
        lines.append(line)
    lines.append('')
    return '\n'.join(lines)

def tohex_pprint(s):
    s = tohex(s)
    l = len(s)
    n_line = int(math.ceil(len(s)/64.))
    lines = []
    for i in range(n_line):
        no = hex(i)[2:]
        line = '0x' + '0'*(6-len(no)) + no + ' '
        line += ' '.join([s[i*64+j*8:i*64+j*8+8] for j in range(8)])
        lines.append(line)
    lines.append('')
    return '\n'.join(lines)


def info(s):
    return "Length of input in bytes: %d\n" % len(s)


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--info',
    dest='info',
    action='store_true')
parser.add_argument('-p', '--pprint',
    dest='pprint',
    action='store_true')
parser.add_argument('--hex',
    dest='view_type',
    action='store_const',
    const='hex')
parser.add_argument('--dots',
    dest='view_type',
    action='store_const',
    const='dots')
parser.add_argument('--out-file', '--out', '-o',
    dest='out_file',
    nargs='?',
    type=argparse.FileType('wb'),
    default=sys.stdout)
parser.add_argument('--file', '-f',
    dest='in_file',
    nargs='?',
    type=argparse.FileType('rb'),
    default=sys.stdin)

if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])
    s = args.in_file.read()
    if args.info:
        args.out_file.write(info(s))
    if args.pprint:
        if args.view_type == 'hex':
            args.out_file.write(tohex_pprint(s))
        elif args.view_type == 'dots':
            args.out_file.write(todots_pprint(s))
    else:
        if args.view_type == 'hex':
            args.out_file.write(tohex(s))
        elif args.view_type == 'dots':
            args.out_file.write(todots(s))
        else:
            args.out_file.write(s)
    


