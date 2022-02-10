# adding multiple string and add concate them using + sign 
name= 'iron man'
greeting= 'welcome to marvel universe '
msg=greeting + ', '+ name.title() 
print(msg)
# concating them using string  formatting
name= 'iron man'
greeting= 'welcome to marvel universe '
msg='{}, {}. voodoo!'.format(greeting, name )
print(msg)
# f string --> behind using f string is to make string formattinh as simple as possible
name= 'iron man'
greeting= 'welcome to marvel universe '
msg=f'{greeting}, {name}. welcome! '