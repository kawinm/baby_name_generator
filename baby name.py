import random

vowels, consonants, letters='aeiou','bcdfghjklmnpqrstvwxyz', vowels+consonants

terms = int(input("How many letters you want for your baby's name? "))

def babyname():
    j = []
    for i in range(1, terms+1):
        k = input("Would you like a [v]owel or [c]onsonant or any [l]etter? ")
        if k.lower() == 'v':
            j.append(random.choice(vowels))
        elif a[k] == 'c':
            j.append(random.choice(consonants))
        elif a[k] == 'l':
            j.append(random.choice(letters))
        else:
            print("Unkonown input " + k)
    print(''.join(j))
    
babyname()


    
            
        

    
