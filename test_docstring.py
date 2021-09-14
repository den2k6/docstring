#! /usr/bin/env python3

def myfunc(msg):
    """description of myfunc

    Args:
        msg (str): message

    Returns:
        bool: always True
    """

    print(msg)
    return True


def main ():
    print(myfunc('hello'))

if __name__ == '__main__':
    main()
