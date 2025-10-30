max_number = 100 # integers > -1
dict = {
    3:"fizz",
    5:"buzz", } #changable by adding key:value pairs
people = ["Person 1","Person 2","Person 3"] # changeable by adding strings who are people
listOfKeys = list(dict.keys())
for i in range (1,max_number+1):
    said = True
    print(people[(i % len(people))-1],end = ": ")
    for j in range(len(dict)):
        if(i % listOfKeys[j] == 0):
            print(dict[listOfKeys[j]],end="")
            said = False
    if(said):
        print(i)
    else:
        print("")
    