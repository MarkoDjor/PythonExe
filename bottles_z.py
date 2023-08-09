def verse(n):

    print(f'{n} bottles of beer on the wall,')
    print(f'{n} bottles of beer,')
    print(f'Take one down, pass it around,')
    print(f'{n-1} bottles of beer on the wall!\n\n')

def main():

    n = 10

    for i in reversed(range(2,n+1)):

        verse(i)

    print(f'1 bottles of beer on the wall,')
    print(f'1 bottles of beer,')
    print(f'Take one down, pass it around,')
    print(f'No more bottles of beer on the wall!\n')

if __name__ == "__main__":
    main()
