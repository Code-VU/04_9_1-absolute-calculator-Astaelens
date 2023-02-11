def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))

    if in_num>=21:
        abs_num=2*(in_num-21)
    else:
        abs_num=21-in_num
    print("Result:", abs_num)
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
