import math


class Calculator:
    def __init__(self, number):
        self.init_num = number
        self.number = None
        self.group = None
        self.final_result = ""
        self.res1 = self.init_num // 10
        self.ones = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                     9: 'Nine'}

        self.twos = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                     17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

        self.tens = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                     90: 'Ninety', 100: 'Hundred'}

        self.suffixes = ('', 'Thousand', 'Million', 'Billion')

    def get_group(self):
        x = len(str(self.init_num))
        self.group = math.ceil(x / 3)

    def process(self):

        self.res1 = self.number // 10
        if self.number < 10:
            self.final_result += self.ones[self.number]
        elif self.number < 20:
            self.final_result += self.twos[self.number]
        else:
            if self.res1 == 0:
                self.final_result += self.tens[self.res1]
            elif self.res1 != 0 and self.res1 * 10 < 100:
                self.final_result += f"{self.tens[self.res1 * 10]} {self.ones[self.number % 10]}"

            elif self.res1 >= 10 and self.res1 > 11:
                self.final_result += f"{self.ones[self.res1 // 10]} hundred and {self.tens[self.res1 % 10 * 10]}-{self.ones[self.number % 10]}"

            elif self.res1 >= 10 and self.res1 == 11:
                print(self.res1 // 10, "12")
                self.final_result += f"{self.ones[self.res1 // 10]} hundred and {self.twos[self.number % 100]}"

            elif self.res1 == 10 and self.res1 == 10:
                self.final_result += f"{self.ones[self.res1 // 10]} hundred and"
                if num % 100 == 0:
                    pass
                else:
                    self.final_result += f" {self.ones[self.number % 100]}"

    def process2(self):
        self.get_group()
        if self.group == 1:
            self.number = self.init_num
            self.process()

        elif self.group == 2:
            self.number = self.init_num // 1000
            # print(self.number)
            self.process()
            self.final_result += " thousand "
            self.number = self.init_num % 1000
            # print(self.number)
            self.process()

        elif self.group == 3:
            self.number = self.init_num // 1000000
            self.process()
            self.final_result += " million "
            #
            self.number = self.init_num % 1000000 // 1000
            self.process()
            self.final_result += " thousand "

            #
            self.number = self.init_num % 1000000 % 1000
            self.process()
        else:
            print("Sorry, we don't accepted this number until now. ERROR TYPE: Number too big.")

    def __str__(self):
        return self.final_result


num = int(input())
process_main = Calculator(num)
process_main.process2()
print(process_main)
