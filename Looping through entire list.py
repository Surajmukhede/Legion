# when you want to do the same action with every item in a list, you can use Python For loop
from tkinter.font import names
from uuid import NAMESPACE_DNS


names=['rockey','arjun','vickey']
for name in names:
    print(name.title())

#doing more work within loop and after the loop
students=['ram','sham','sheeta','jamun']
for student in students:
    print(student.title()+',is one of the brightest student of the class'+".\n")
    print("best of luck"+" "+student.title()+"\n")
    #indenting unnecessarily after the loop
    print("we glad that  your the student of our college")
    ame= 'iron man'
