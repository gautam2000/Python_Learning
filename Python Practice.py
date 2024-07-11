#!/usr/bin/env python
# coding: utf-8

# # 1.Print meow three times

# In[3]:


print("meow")
print("meow")
print("meow")


# # 2.

# In[14]:


print("meow\n" *3,end="")


# # 3.Print meow using loop

# In[6]:


i=0

while i<3:
    print("meow")
    i=i+1


# # 4.Print using for loop

# In[15]:


for _ in range(3):
    print("meow")


# # 5.User input

# In[18]:


while True:
    n=int(input("what is n "))
    if n>0:
        break
for _ in range(n):
    print("meow")


# # 6.Using a function to get user input

# In[25]:


def get_number():
    while True:
        n=int(input("what is n?"))
        if n>0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")
        
def main():
    number=get_number()
    meow(number)
    
    
main()


# # 7.Using a function to use loops

# In[26]:


def get_number():
    while True:
        n=int(input("what is n?"))
        if n>0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")
        
def main():
    number=get_number()
    meow(number)
    
    
main()


# # 8.Lists

# In[31]:


students=["Hermoine","Harry","Ron"]
print(students[0])
print(students[1])
print(students[2])


# # 9.Iteration

# In[33]:


students=["Hermoine","Harry","Ron"]
for student in students:
    print(student)


# # 10.for loop

# In[36]:


for i in range(len(students)):
    print(i+1,students[i])


# In[37]:


get_ipython().run_line_magic('pinfo', 'range')


# # 11.Dictionaries

# In[ ]:


students=["Hermoine","Harry","Ron","Draco"]
houses=["Gryffindor","Gryffindor","Gryffindor","Slytherin"]


# In[42]:


students={"Hermoine":"Gryffindor",
           "Harry":"Gryffindor",
         "Ron":"Gryffindor",
         "Draco":"Slytherin"}
students


# # 12.Dictionary Iteration

# In[46]:


print(students['Hermoine'])
print(students['Harry'])
print(students['Ron'])
print(students['Draco'])


# In[52]:


for i in students:
    print(i,students[i],sep=',')


# # 13.Lists of dictionaries

# In[54]:


students=[{'name':'Hermoine','house':'Gryffindor','patronus':'Otter'},
         {'name':'Harry','house':'Gryffindor','patronus':'Stag'},
         {'name':'Ron','house':'Gryffindor','patronus':'Jack Russell'},
         {'name':'Draco','house':'Slytherin','patronus':'None'}
         ]
students


# # 14.Iteration through Lists of dictionaries

# In[58]:


for student in students:
    print(student['name'],student['house'],student['patronus'],sep=',')


# # 15.Nested Loops

# In[73]:


def main():
    
   # print_row(4)
    #print_column(3)
    print_square(3)
    
def print_column(height):
    print("#\n"*height,end='')

def print_row(width):
    print("?"*width)
    
def print_square(size):
    for i in range(size):
        for j in range(size):
            print('#',end='')
        print()
            

main()

