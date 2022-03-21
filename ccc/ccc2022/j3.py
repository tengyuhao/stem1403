info = input()
info = list(info)
# print(info)
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
number = ["1",'2','3','4','5','6','7','8','9', '0']

# print(number)
syll = ''
syllL = []
# print(len(info))
for i in range(len(info)):
    if info[i] in abc:
        syll += info[i]
    if info[i] == '+':
        syll += " tighten "

    if info[i] == '-':
        syll += " loosen "

    if info[i] in number:
        syll += f"{info[i]}"
        # syllL.append(syll)

        if i != len(info)-1:
            # print(i)
            if info[i + 1] in number:
                pass
            else:
                syllL.append(syll)
                syll = ""
        elif i == len(info)-1:
            syllL.append(syll)


for i in syllL:
    print(i)