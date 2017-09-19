
# coding: utf-8

# In[1]:


# a=24
# b=21
# c=a+b
# print(c)


# In[20]:


import numpy as np
import urllib.request as ur

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = ur.urlopen(url)


# In[21]:


# mystr=print(u.read())


# In[27]:


with open('iris.csv', 'wb') as f:
    f.write(u.read())
    f.close()

