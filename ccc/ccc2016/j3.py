word = input()
word = list(word)
num_count = 0
print(word)
long = len(word) - 1
print(long)
for i in range(long):
    print(i)
    if word[i] == word[long-i]:
        print("call")
        num_count += 1
    else:
        print("callll")
        word = word[i+1:]
        long -= 1

    # if long -1 == long //2 :
    #     break


print(num_count + 1)
