#!/usr/local/bin/python3

def mdc(num):
    def calc(div):
        return div if sum(map(lambda x: x % div, num)) == 0 \
            else calc(div - 1)
    return calc(min(num))

if __name__ == '__main__':
    print(mdc([21, 7]))
    print(mdc([125, 40]))
    print(mdc([9, 564, 66, 31]))
    print(mdc([50,25]))