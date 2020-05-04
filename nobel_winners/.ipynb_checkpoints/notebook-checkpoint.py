#!/usr/bin/env python
# coding: utf-8

# # Nobel Prize Winners

# In[1]:


# import pandas, matplotlib.pyplot and numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


# loading DataFrame from 'data/nobel_raw.csv'
nobel_raw = pd.read_csv('~/project_spring_2020/data/nobel_raw.csv')


# In[3]:


# removing the rows when there are missing values in 'firstname' and 'surname' columns
nobel_rm_fs = nobel_raw.dropna(how='any', subset=['firstname', 'surname'])


# In[4]:


# extracting necessary columns
nobel_col = nobel_rm_fs[['firstname', 'surname','born', 'borncountry', 'gender', 'year', 'category', 'share']]


# In[5]:


# assert that there are no missing values
assert nobel_col.notnull().all().all()


# In[6]:


# deduplication
nobel_clean = nobel_col.drop_duplicates().reset_index()


# ### Visualizing the distribution of Nobel winners' birth countries

# In[7]:


# counting the number of Nobel winners for each country
country_count = nobel_clean['borncountry'].value_counts()


# In[8]:


# modifying the name 'the Netherlands' to 'Netherlands'
country_count.replace('the Netherlands','Netherlands',inplace=True)


# In[9]:


# visualizing the distribution of Nobel winners' birth countries
country_count.head(15).plot(kind='bar')
plt.title('Nobel winners birth countries')
plt.xlabel('Country')
plt.show()


# ### What is the percentage of female Nobel winners?

# In[10]:


nobel_gender = nobel_clean['gender'].value_counts()


# In[11]:


nobel_gender.plot(kind='pie',labels=['Male','Female'], autopct='%.2f',colors=['g', 'c'], figsize=(6, 6))
plt.show()

