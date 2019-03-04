#!/usr/bin/python


def hexstr(s):
    """
    Get little endian hex words represenation of string
    Very similar to x/x in GDB when debugging a C program

    :param s: str - a string to process
    :return: str - a tab-delimited little endian hex words representation of s in rows of 4
    """

    stack = []
    out = ''
    words = 0

    for i in range(len(s)):
        if i > 0 and i % 4 == 0:
            out += '0x'
            while len(stack) > 0:
                out += stack.pop()
            words += 1
            if words == 4:
                out += '\n'
                words = 0
            else:
                out += '\t'
        stack.append(hex(ord(s[i]))[2:])

    # get last remaining bytes, if any
    if len(stack) > 0:
        out += '0x'
        out += '00' * (4 - len(stack))
        while len(stack) > 0:
            out += stack.pop()

    return out.strip()


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        sh = hexstr(sys.argv[1])
        print(sh)
