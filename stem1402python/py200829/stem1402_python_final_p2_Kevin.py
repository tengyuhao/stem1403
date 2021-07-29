"""
1. Calculating TF  (30’)
Description
Term Frequency (TF) is one of  important concerns in many fields of Text Analysis, Data Mining, Machine Learning, Natural Language Processing (NLP) and etc.
The formula of calculating TF is given as following:
TF = Number of occurrence of a word in an article  / Total number of words in an article
Removing stop words, punctuations, symbols and unnecessary numbers
Stop words are the words to be eliminated before processing in order to save resources and improve efficiency.
Possible stop words includes:  'the', 'a', 'an', 'is', 'are', 'was', 'were', 'been', 'of'
Punctuations along with white spaces are also unnecessary to this text processing.
Numbers like [1], [15][18] should also be removed.
Hint:  You may put content to be removed into a list
Problem
1. Please write a python program to calculate the TF of every filtered word in the given article.
Output the result properly. (15')
2. In addition, find out the 3 most frequently occurring words of them.
Output the result in descending order. (15')
"""

# Article
article = """
Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data.
Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural-language generation.
In the early days, many language-processing systems were designed by symbolic methods, i.e., the hand-coding of a set of rules, coupled with a dictionary lookup:[12][13] such as by writing grammars or devising heuristic rules for stemming.
More recent systems based on machine-learning algorithms have many advantages over hand-produced rules:
The learning procedures used during machine learning automatically focus on the most common cases, whereas when writing rules by hand it is often not at all obvious where the effort should be directed.
Automatic learning procedures can make use of statistical inference algorithms to produce models that are robust to unfamiliar input (e.g. containing words or structures that have not been seen before) and to erroneous input (e.g. with misspelled words or words accidentally omitted). Generally, handling such input gracefully with handwritten rules, or, more generally, creating systems of handwritten rules that make soft decisions, is extremely difficult, error-prone and time-consuming.
Systems based on automatically learning the rules can be made more accurate simply by supplying more input data. However, systems based on handwritten rules can only be made more accurate by increasing the complexity of the rules, which is a much more difficult task. In particular, there is a limit to the complexity of systems based on handwritten rules, beyond which the systems become more and more unmanageable. However, creating more data to input to machine-learning systems simply requires a corresponding increase in the number of man-hours worked, generally without significant increases in the complexity of the annotation process.
"""

# 1. Remove list
# remove1 = ['the', 'a', 'an', 'is', 'are', 'was', 'were', 'been', 'of']
article = article.replace(',', ' ')
article = article.replace('.', ' ')
article = article.replace('-', ' ')
article = article.replace('(', ' ')
article = article.replace(')', ' ')
article = article.replace(':', ' ')
article = article.replace('[12]', ' ')
article = article.replace('[13]', ' ')
article = article.replace(' the ', ' ')
article = article.replace(' a ', ' ')
article = article.replace(' is ', ' ')
article = article.replace(' are ', ' ')
article = article.replace(' was ', ' ')
article = article.replace(' were ', ' ')
article = article.replace(' been ', ' ')
article = article.replace(' of ', ' ')
article = article.replace(' to ', ' ')
article = article.replace(' and ', ' ')
article = article.replace(' more ', ' ')

# Split
print("===================== Term Frequency =======================")
count_total = 0
article = article.split()
for i in article:
    count_total += article.count(i)
    print(article.count(i))
print(count_total)
res_before = 0
for i in article:
    res = article.count(i) / count_total
    print(i, res)

print("================== \u2191 \u2191 \u2191 Term Frequency \u2191 \u2191 \u2191 ==================")

# Three most frequently occurring words
import collections
count1 = collections.Counter(article)
res_three = count1.most_common(3)
print(res_three)


print("========================================================================================")


"""
2. Data Analysis and Sorting (20')
Description
There held an International FIRST LEGO Robotic Competition. 
You are helping the organizer to determine the 1st, 2nd, 3rd places for the teams based on their scores.
Each team got 2 chances and accordingly had 2 scores for the game. 
The final score for each team is calculated by selecting the larger one of the 2 scores.
Problem
1. Please write a python program to show the rank list of each team in descending order by their final score.   
Output result must include the team name, the final score, and rank number which can be 1,2,3,..
"""
# Information
information = [
    ["Robert Master", 220, 340],
    ["Montreal Sprite", 320, 270],
    ["Smart Maker", 115, 405],
    ["Nova Robert", 450, 380],
    ["10 Stars", 100, 330]

]
res = []

# Operator logical
for i in range(len(information)):
    if information[i][1] > information[i][2]:
        res.append(information[i][1])

    elif information[i][1] < information[i][2]:
        res.append(information[i][2])
    else:
        print("Error")
com = 0
res.sort(reverse=True)
print(res)

# Output
for i in information:

    if res[0] in i:
        print("First", i)
    elif res[1] in i:
        print("Second", i)
    elif res[2] in i:
        print("Third", i)
    else:
        print("Error")

# End
