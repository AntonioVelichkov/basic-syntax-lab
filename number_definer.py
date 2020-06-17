num = float(input())

if num == 0:
    print(f'zero')
elif num < 0:
    if abs(num) < 1:
        print(f'small negative')
    elif abs(num) > 1000000:
        print(f'large negative')
    else:
        print(f'negative')
elif num > 0:
    if abs(num) < 1:
        print(f'small positive')
    elif abs(num) > 1000000:
        print(f'large positive')
    else:
        print(f'positive')
