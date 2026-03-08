def romantoInt(romanInput):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 5, 'I': 1}
    resultInteger = 0
    for i in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] <[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
    else:
        resultInteger += roman[romanInput[i]]
    return resultInteger + roman[romanInput[-1]]

# Take roman as input from user
roman = input("Input roman numeral : ")

# Print the integer
print("Integer equivalent : ",romantoInt(roman) )