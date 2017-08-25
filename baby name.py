import random

vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
letters=vowels+consonants

name = input("Enter the name of file: ")
terms = int(input("How many letters you want for your baby's name? "))

with open(name +".txt",'w+') as file:
    i = 1
    while i <= terms:
        a = {'v':'v','c':'c','l':'l'}
        k = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
        if a[k] == 'v':
            j=random.choice(vowels)
        elif a[k] == 'c':
            j=random.choice(consonants)
        elif a[k] == 'l':
            j = random.choice(letters)
        else:
            j = a[i]
        i = i + 1
        file.write(j)

done = open(name+".txt",'r')      
x = done.read()
print(x)
    
            
        

    
