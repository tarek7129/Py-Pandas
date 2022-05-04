#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


series = pd.Series ([7,3,2, np.nan, 6,9])


# In[ ]:





# In[3]:


series


# In[4]:


type(series)


# In[6]:


datas = pd.date_range('20180101')


# In[7]:





# In[8]:


datas = pd.date_range('20180101',period = 6)


# In[9]:


datas = pd.date_range('20180101',periods = 6)


# In[10]:


datas


# In[16]:


df = pd.DataFrame(np.random.randn(6,4), index = datas, columns = list("ABCD"))


# In[ ]:





# In[17]:


df


# In[ ]:




