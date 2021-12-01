one_To_nineteen = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
              6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
after_nineteen = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def process(num):
    if num >= 1 or num <= 19:
        # eval(num)
        return one_To_nineteen[num]

    elif num >= 20 or num <= 99:
        num2 = list(num)[0]
        num3 = list(num)[1]
        # return after_nineteen[num2], one_To_nineteen[num3]
        return num2, num3
    else:
        print("")


inp = eval(input("Please enter a number between 0 and 99: "))
print(process(inp))
