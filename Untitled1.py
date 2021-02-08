#!/usr/bin/env python
# coding: utf-8

# In[74]:


from platform import python_version
print(python_version())


# In[75]:


# filename.py
"""This is the file header.
The header contains basic information about the file.
"""
if __name__ == "__main__":
 pass


# In[76]:


if __name__ == "__main__":
    print("Hello, world!")


# In[77]:


help(print)


# In[78]:


x = 5
y = 2**2 +1
x == y

x,y = 5, 2**(2+1)
x == y


# In[79]:


def add(x,y):
    return x+y
add(2,5)


# In[80]:


def compare(x,y):
    return (x < y) - (x > y)
compare(2, 5)


# In[81]:


def add(x,y):
    return x,y, x + y
FV, SV, S=add(2,5)
print ("first veriable is {} seconed veribale is {} and summation is {}".format(FV,SV,S))


# In[82]:


pi = 3.14159
r= 6.0
V= 4.0/3.0*pi* r**3
if __name__ == "__main__":
 print('The volume of the sphere is: ',V)


# In[83]:


def information (Course,professor,level='8'):
    print(Course + 'is in' + level +'whitch is delevired by' +professor)
    if name == "__ main __":
        Course= "IS-372 Data mining & Data warehouse"
        professor= "A/prof.Mohamed Al-Sarem"
        information(Course,professor)


# In[84]:


Course_Name = "IS-372 Data mining & Data warehouse"
print(Course_Name[2])


# In[85]:


Course_Name = "IS-372 Data mining & Data warehouse"
print(Course_Name[-1])


# In[86]:


Course_Name = "IS-372 Data mining & Data warehouse"
print(Course_Name[5])


# In[87]:


Course_Name = "IS-372 Data mining & Data warehouse"
print(Course_Name[6])


# In[88]:


my_list = ["Hello", 93.8, "world", 10]


# In[89]:


my_list[0]


# In[90]:


my_list[-2]


# In[91]:


my_list[:2] 


# In[92]:


my_list = [1, 2]
my_list.append(4)
my_list


# In[93]:


my_list.insert(2, 3)
my_list


# In[94]:


my_list.remove(3)
my_list


# In[95]:


my_list.pop()


# In[96]:


my_list


# In[97]:


list_ops = ["bear", "ant", "dog", "cat"]
list_ops.append(1)
list_ops.pop(2)


# In[98]:


# Initialize some sets. Note that repeats are not added.
Datamining_proffessor = {"Muhanad Almuhameed",  "Faisal, Saeed", "Mohamed, Alsarm "}
print(Datamining_proffessor)

Datamining_proffessor.add("Wadi,Bolila") # Add an object to the set.
Datamining_proffessor.discard("Muhanad-Almuhameed") # Delete an object from the set.
print(Datamining_proffessor)

Database_proffessor = {"Muhanad Almuhameed", "", "Faisal, Saeed", "Mohamed, Alsarm ,""Wadi,Bolila"}

Datamining_proffessor.intersection(Database_proffessor)
Datamining_proffessor.difference(Database_proffessor)


# In[99]:


datascintece_Trake = {"IS-372": "Datamining & Datawerahouse",
                      "IS-472": "Desion support System",
                      "IS-476": "information search,Rettreval,Viualization",
                      "IS-453": "Spataial topics in data manager"}
print(datascintece_Trake["IS-453"])
datascintece_Trake.keys()
datascintece_Trake.values()


# In[100]:


i = 0
while i<=10:
    print(i, end='')
    i += 1


# In[101]:


colors = ["red","green","blue","yellow"]
for entry in colors:
 print(entry + "!")


# In[102]:


s = "stab"
for i in range(len(s)):
 print (s[0 : i : 1])

