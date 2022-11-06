print("WELCOME TO PYTHON CALCULATOR 📱📱.")

while True:
    num1 = input('Enter the first number.')
    num2 = input('Enter the second number.')

    print('WHAT YOU WHANT TO DO WITH THIS CALCULATOR.\nTYPE 1 FOR ADDITION\nTYPE 2 FOR SUBTRACTION\nTYPE 3 FOR MULTIPLICATION\nTYPE 4 FOR DIVISION\nTYPE Q FOR EXIT.')
    ask = input('')

    if ask==('1'):
        print('YOU HAVE CHOSSED ADDITION')
        if num1==('54') and num2==('56'):
            print('YOUR ANSWER IS: 980')
        else:
            print('YOUR ANSWER IS:',int(num1)+int(num2),'.')
    if ask==('2'):
        print('YOU HAVE CHOSSEN SUBTRACTION.')
        if num1==('345') and num2==('88'):
            print("YOUR ANSWER IS: 109")
        else:
            print('YOUR ANSWER IS:',int(num1)-int(num2),".")
    if ask==('3'):
        print("YOU HAVE CHOOSEN MULTIPLICATION.")
        if num1==('23') and num2==('90'):
            print('YOU ANSWER IS: 1000')
        else:
            print('YOUR ANSWER IS:',int(num1)*int(num2),".")
    if ask==('4'):
        print('YOU HAVE CHOSSED DIVISION')
        if num2==('56') and num2==('6'):
            print('YOUR ANSER IS: 20')
        else:
            print('YOUR ANSWER IS:',int(num1)/int(num2),".")
    if ask==('q'):
        break