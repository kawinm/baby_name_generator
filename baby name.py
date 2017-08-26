import random

vowels, consonants, letters='aeiou','bcdfghjklmnpqrstvwxyz', vowels+consonants

terms = int(input("How many letters you want for your baby's name? "))

def babyname():
    choices = []
    for x in range(terms):
        k = input("Would you like a [v]owel or [c]onsonant or any [l]etter? ")
        choices.append(k)
        
    for x in range(10):
        j = []
        for k in choices:
            if k.lower() == 'v':
                j.append(random.choice(vowels))
            elif k.lower() == 'c':
                j.append(random.choice(consonants))
            elif k.lower() == 'l':
                j.append(random.choice(letters))
            else:
                print("Unkonown input " + k)
        print(''.join(j))
    
babyname()


    
            
        

    
