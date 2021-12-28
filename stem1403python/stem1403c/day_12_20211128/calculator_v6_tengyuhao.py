import math

ones = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

twos = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
        17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

tens = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
        100: 'Hundred'}

suffixes = ('', 'Thousand', 'Million', 'Billion')


def getGroup(num):
    x = len(str(num))
    result = math.ceil(x / 3)
    return result


def process(num):
    global final_result
    if num < 10:
        final_result += ones[num]
    elif num < 20:
        final_result += twos[num]
    else:
        res1 = num // 10
        # print(res1)
        if res1 == 0:
            final_result += tens[res1]
        elif res1 != 0 and res1 * 10 < 100:
            final_result += tens[res1 * 10]
            final_result += f" {ones[num % 10]}"

        elif res1 >= 10 and res1 > 11:
            final_result += f"{ones[res1 // 10]} hundred and"
            final_result += f" {tens[res1 % 10 * 10]}-"
            final_result += f"{ones[num % 10]}"

        elif res1 >= 10 and res1 == 11:
            final_result += f"{ones[res1 // 10]} hundred and"
            final_result += f" {twos[num % 100]}"

        elif res1 == 10 and res1 == 10:
            final_result += f"{ones[res1 // 10]} hundred and"
            if num % 100 == 0:
                pass
            else:
                final_result += f" {ones[num % 100]}"


num = int(input())

result = getGroup(num)
final_result = ""

if result == 1:
    process(num)

elif result == 2:
    num1 = num //1000
    process(num1)

    final_result += " thousand "
    num2 = num % 1000
    process(num2)
elif result == 3:
    #
    num1 = num // 1000000
    process(num1)
    # print(num1)
    final_result += " million "

    #
    num2 = num % 1000000 // 1000
    process(num2)
    final_result += " thousand "
    # print(num2)

    num3 = num % 1000000 % 1000
    # print(num3)
    process(num3)
else:
    print("Sorry, we don't accepted this number until now")
print(final_result)
