

def main():
    lst = []
    while True:
        value: str = input('Enter a value: ')
        if value == '':
            break
        lst.append(value)
    print(f"Here's the list: {lst}")

if __name__ == '__main__':
    main()