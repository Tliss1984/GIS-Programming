#!/usr/bin/env python
# coding: utf-8

# ## Welcome to your notebook.
# 

# #### Run this cell to connect to your GIS and get started:

# In[5]:


from arcgis.gis import GIS
gis = GIS("home")


# #### Now you are ready to start!

# In[6]:


map1  =gis.map("boston")


# In[9]:


map1


# In[12]:


# Item Added From Toolbar
# Title: Boston Income and Growth | Type: Feature Service | Owner: lisa_berry
item = gis.content.get("b8c35f6b170340ca9f90c94724423851")
item


# In[14]:


map1.add_layer(item)


# In[ ]:





# In[ ]:





# In[ ]:




