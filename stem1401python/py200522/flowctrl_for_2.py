"""
for loop

summary
product
"""

# summary of  1...100
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + ... + 100

# goal?
# initial value?
# conditions of termination
# what job to repeat

summary = 0

# (current)summary <- (last)summary + i
#
# summary 1 <- 0 + 1
# summary 3 <- 1 + 2
# summary 6 <- 3 + 3
# summary 10 <- 6 + 4
# ...
# summary ? <- summary + 100

for i in range(1, 101):
    summary = summary + i

print("summary of 1 to 100 is {}".format(summary))


# homework - 1
# product of 1...20
# 1 * 2 * 3 * 4 * 5 * 6 * 7 * ... * 100
# homework - 2
# quiz 9 (don't do for loop)
