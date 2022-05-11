
right = 0
wrong = 0
print("in order from closet to the sun what plants are in our solar system ")
print('''
1)
Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

2) 
Mercury, Venus, Earth, Mars, Jupiter, Saturn, Neptune, Uranus 

3) 
Uranus, Neptune, Saturn, Jupiter, Mars, Earth, Venus, Mercury

4) 
Venus, Earth, Mercury, Jupiter, Earth, Neptune, Uranus, Mars
''')
answer_1 = int(input("answer : "))

if answer_1 == 1:
    right = right+1
else:
    wrong = wrong + 1
print("inertia is a crucial part of physics?")
print('''
1) false

2) true
''')
answer_2 = int(input("answer: "))
if answer_2 == 2:
    right = right + 1
else:
    wrong = wrong + 1

print("where are many asteroids located")
print('''
1) asteroid ring 

2) meteor belt 

3) asteroid belt 

4) mercurys surface 
''')
answer_3 = int(input("answer: "))
if answer_3 == 3:
    right = right + 1
else:
    wrong = wrong + 1

print("what is the sun made up of")
print('''
1) hydrogen and helium 

2) oxygen

3) iron 

4) a lot of fire 
''')
answer_4 = int(input("answer: "))
if answer_4 == 1:
    right = right + 1
else:
    wrong = wrong + 1
print("what is our biggest planet in our solar system")
print('''
1) Jupiter

2) Venus

3) Saturn 

4) Uranus 
''')
answer_5 = int(input("ansewr: "))
if answer_5 == 1:
    right = right + 1
else:
    wrong = wrong + 1
print("a comet is a piece of rock")
print('''
1) False

2) True 
''')
answer_6 = int(input("answer: "))
if answer_6 == 1:
    right = right + 1
else:
    wrong = wrong + 1
print("Stars are _________________")
print('''
1) balls of flame 

2) 1 and 2

3) balls of gas 

4) Stars 
''')
answer_7 = int(input("answer: "))
if answer_7 ==2:
    right = right + 1
else:
    wrong = wrong + 1
print("what is the boiling point of water in celsius")
print('''
1) 20 degree celsius

2) 200 degree celsius 

3) -70 degree celsius 

4) 100 degree celsius 
''')
answer_8 = int(input("answer: "))
if answer_8 == 4:
    right = right + 1
else:
    wrong = wrong + 1
print("is metal a good conductor of heat and electricity")
print('''
1) True 

2) False 
''')
answer_9 = int(input("answer: "))
if answer_9 == 1:
    right = right + 1
else:
    wrong = wrong + 1
print("what is the different between an animal cell and a plant cell")
print('''
1) animal cell has mitochondria and plant cell dones't 

2) plant cell doesnt have a nucleus while animal cell does 

3) plant cell has a cell wall while animal cell doesnt 

4) none of the above
''')
answer_10 = int(input("answer: "))
if answer_10 == 3:
    right = right + 1
else:
    wrong = wrong + 1

print(f'well done, you got {right} answers correct and {wrong} answers incorrect')






