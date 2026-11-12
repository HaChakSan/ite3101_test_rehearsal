def main():
   while True:
    try:
        num = int(input("Type an integer:"))
        break
    except ValueError:
       print('please enter an integer.')

if num % 10 == "__main__":
    # execute only if run as a script
    main()
