"""
client app
version 5
"""

import petsys as ps
# main
def showMyPets(petList):
    for p in petList:
        print(p.petClass)


p1 = ps.Cat("cat")
p2 = ps.Dog("dog")
p3 = ps.Pet()
p4 = ps.Cat("cat")
p5 = ps.Dog("dog")
p6 = ps.Pet()
p8 = ps.Hamster("hamster")
mypets = [p1, p2, p3, p4, p5, p6, p8]

peter = ps.Person("Peter", mypets)

# jack = Person("Jack")

# before
showMyPets(peter.getPets())
for pi in peter.mypets:
    # Peter feeds his pet
    peter.feed(pi)
    print()

print("============")
# after
p7 = ps.Dog("dog")
peter.adopt(p7)
showMyPets(peter.getPets())
peter.feed(p7)

p9 = ps.Hamster("hamster")
peter.adopt(p9)

showMyPets(peter.getPets())
peter.feed(p9)

