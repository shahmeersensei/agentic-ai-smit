"""Error handling examples."""

if __name__ == '__main__':
    try:
        print(1 / 0)
    except ZeroDivisionError:
        print('caught division by zero')
