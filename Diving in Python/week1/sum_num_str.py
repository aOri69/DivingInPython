import sys


if __name__ == '__main__':
    sum_str = (0)
    if not sys.argv[1].isdigit():
        raise TypeError
    digit_string = sys.argv[1]
    for digit in digit_string:
        sum_str += int(digit)
    print('Сумма цифр в веденной строке: ' +
          sys.argv[1] + ' равна: ' + str(sum_str))
