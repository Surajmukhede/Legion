# tuple is like list;  it used () instead of []
square_measure = (200, 10)
print(square_measure[0])
print(square_measure[1])
# we cant alter the tuples value 
square_measure = (200, 10)
square_measure[0]=50

# lopping through tuples
fact = ('sun', 'moon','earth','air')
for nonchangeable in fact:
    print(fact)