# %%
"""
# Nobel Prize Winners
"""

# %%
# import pandas, matplotlib.pyplot and numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
# loading DataFrame from 'data/nobel_raw.csv'
nobel_raw = pd.read_csv('~/project_spring_2020/data/nobel_raw.csv')

# %%
# removing the rows when there are missing values in 'firstname' and 'surname' columns
nobel_rm_fs = nobel_raw.dropna(how='any', subset=['firstname', 'surname'])

# %%
# extracting necessary columns
nobel_col = nobel_rm_fs[['firstname', 'surname','born', 'borncountry', 'gender', 'year', 'category', 'share']]

# %%
# assert that there are no missing values
assert nobel_col.notnull().all().all()

# %%
# deduplication
nobel_clean = nobel_col.drop_duplicates().reset_index()

# %%
"""
### Visualizing the distribution of Nobel winners' birth countries
"""

# %%
# counting the number of Nobel winners for each country
country_count = nobel_clean['borncountry'].value_counts()

# %%
# modifying the name 'the Netherlands' to 'Netherlands'
country_count.replace('the Netherlands','Netherlands',inplace=True)

# %%
# visualizing the distribution of Nobel winners' birth countries
country_count.head(15).plot(kind='bar')
plt.title('Nobel winners birth countries')
plt.xlabel('Country')
plt.show()

# %%
"""
### What is the percentage of female Nobel winners?
"""

# %%
nobel_gender = nobel_clean['gender'].value_counts()

# %%
nobel_gender.plot(kind='pie',labels=['Male','Female'], autopct='%.2f',colors=['g', 'c'], figsize=(6, 6))
plt.show()