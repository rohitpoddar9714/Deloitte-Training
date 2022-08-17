#!/usr/bin/env python
# coding: utf-8

# In[1]:


#define a function, to calculate variance
def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot = tot + (x - mean)**2
    return tot/len(X)


# In[2]:


z = [10, -20, 30, -40, 50, -60, 70, -80] 
print("variance is: ", variance(z))


# In[5]:


#define a function, to calculate Standard Deviation
def std(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot = tot + (x - mean)**2
    std_dev = (tot/len(X))**0.5
    return std_dev


# In[6]:


z = [10, -20, 30, -40, 50, -60, 70, -80] 
print("Standard deviation is: ", std(z))


# In[ ]:




