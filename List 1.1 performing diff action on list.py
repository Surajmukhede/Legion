# changing, adding and removing element from  a list 
# modifying 
list=['suraj','karan','sushil','varun']
list[3]='ajay'
print(list)

# adding element in list; 1) varible.append()--> it will add elent at end of list
feature_moveies=['avatar','mi','pursuit of happyness']
feature_moveies.append('dark age')
print(feature_moveies)

# inserting element in list 2) variable.insert(position, name of element to be adding)
list=['suraj','karan','sushil','varun']
list.insert(2, 'ashish')
print(list)

# Removing an item form list using 1) del variable[position ]


# removing an item by using variable.pop()method---> it wil removes last item from a list but it lets you work with that item after removing it
fav_colour=['pink','black','brown','orange']
colour_unlike=fav_colour.pop(1)    # we can also popped element from list with position 
print(colour_unlike)

fruit=['apple','orange','guavas','straberry']
msg=fruit.pop(2)
print(msg.title()+' '+ ' is no longer is my favourite food.')

# removing item by its value using variable.remove() function --> we can use this function only whrn we know the value of item 
motorcycles=['honda','ducati','duke','apache']
motorcycles.remove('ducati')
print(motorcycles)
too_expansive='duke'
motorcycles.remove(too_expansive)
print(motorcycles)print("\nA "+too_expansive.title()+' '+ 'is too expensive for me. ')
