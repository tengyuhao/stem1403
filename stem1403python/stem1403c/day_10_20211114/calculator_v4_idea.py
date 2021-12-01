# Number to Words

# Main Logic
ones = {0: 'Zero', 1: 'One', 2: 'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}

twos = {10: 'Ten', 11: 'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}

tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']

suffixes = ('', 'Thousand', 'Million', 'Billion')


N = input()
long = len(N)
res = ""
print("This calculator just accept long of 4")
# N = int(N)
if long == 1:
    res = ones.get(int(N))
    print(res)

elif long == 2 and long <= 10 and long > 20:
    print(twos[int(N)])

elif long == 2:
    new_number = N[:1]
    # print(new_number)
    N = int(N)
    for i in range(2, 10):
        # print(i)
        if int(new_number) == i:
            res += tens[i-2]
    """
    .... 
    """
    N = str(N)
    new_number = N[1:]
    new_number = int(new_number)
    res += f" {ones.get(new_number)}"

elif long == 3:
    new_number = N[:1]
    for i in range(2, 10):
        # print(i)
        if int(new_number) == i:
            res += ones[i]
        elif int(new_number) == 1:
            res += "One"
            break
    res += " Hundred"
    new_number = N[1:2]
    # print(new_number)
    N = int(N)
    for i in range(2, 10):
        # print(i)
        if int(new_number) == i:
            res += tens[i - 2]
    """
    .... 
    """
    N = str(N)
    new_number = N[2:]
    new_number = int(new_number)
    res += f" {ones.get(new_number)}"

elif long == 4:
    new_number = N[:1]
    for i in range(2, 10):
        # print(i)
        if int(new_number) == i:
            res += ones[i]
        elif int(new_number) == 1:
            res += "One"
            break
    res += " thousand "
    new_number = N[1:2]
    for i in range(2, 10):
        # print(i)
        if int(new_number) == i:
            res += ones[i]
            res += " Hundred "
        elif int(new_number) == 1:
            res += "One"
            res += " Hundred"
            break

    new_number = N[3:]
    # print(new_number)

    """
    .... 
    """
    N = str(N)
    new_number = N[3:]
    new_number = int(new_number)
    res += f" {ones.get(new_number)}"


elif long == 5:
    new_number = N[:2]
    print(new_number)
    if int(new_number) < 20:
        res += twos[int(new_number)]
    else:
        # print(new_number)
        new_number = N[:1]
        N = int(N)

        for i in range(2, 10):
            # print(i)
            if int(new_number) == i:
                res += tens[i-2]
        """
        .... 
        """
        N = str(N)
        new_number = N[1:2]
        new_number = int(new_number)
        res += f" {ones.get(new_number)}"

    res += " thousand "
    new_number = N[3:4]
    for i in range(2, 10):
        # print(i)
        if int(new_number) == i:
            res += ones[i]
            res += " Hundred "
        elif int(new_number) == 1:
            res += "One"
            res += " Hundred "
            break

    new_number = N[3:4]
    # print(new_number)
    print(new_number)
    if int(new_number) < 20:
        new_number = int(new_number)
        res += f"{twos[new_number]}"


    else:
        for i in range(2, 10):
            # print(i)
            if int(new_number) == i:
                res += tens[i - 2]

        N = str(N)
        new_number = N[4:]
        new_number = int(new_number)
        res += f"{ones.get(new_number)}"

print(res)
