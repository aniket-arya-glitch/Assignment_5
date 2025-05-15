#Create a Dictionary of Student Marks

names={'Alice':82, 'Max':79, 'Tennyson':50, 'Gwen':96, 'Aniket':70, 'Krishanth':99, 'Robert':100}
n= input ("Enter student's name:").capitalize()
if (n in names):
    print ('Student name is:',n)
    print (n,'marks=',names[n])
else:
    print('Student not found!')




#Demonstrate List Slicing

o=[i for i in range(1,11)]
print('Original list:',o)
ff=o[:5]
print('Extracted first five elements:',ff)
print('Reversed extracted elements:',ff[::-1])
