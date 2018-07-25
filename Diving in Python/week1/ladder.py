import sys


if __name__ == '__main__':
    SHARP = '#'
    SPACE = ' '
    NUM_STEPS = int(sys.argv[1])
    j = NUM_STEPS-1
    for i in range(1, NUM_STEPS+1):
        print(SPACE*j + SHARP*i)
        j -= 1
