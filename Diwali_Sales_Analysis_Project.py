#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv(r'C:\Users\slgos\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv', encoding= 'unicode_escape')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[12]:


pd.isnull(df)


# In[7]:


pd.isnull(df).sum()


# In[9]:


df.dropna(inplace=True)


# In[10]:


df['Amount']= df['Amount'].astype('int')


# In[11]:


df['Amount'].dtypes


# In[12]:


df.columns 


# In[13]:


df.describe()


# In[14]:


df[['Orders','Amount']].describe()


# # Exploratory Data Analytics (EDA)

# # Gender

# In[29]:


ax = sns.countplot(x= 'Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)
    +
sns.set(rc={'figure.figsize':(5,5)})


# In[19]:


df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[30]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x= 'Gender', y= 'Amount', data=sales_gen)

sns.set(rc={'figure.figsize':(5,5)})


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men.

# # Age

# In[44]:


ax = sns.countplot(data=df, x='Age Group', hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)
    
sns.set(rc={'figure.figsize':(10,5)})    


# In[42]:


sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)

sns.set(rc={'figure.figsize':(10,5)})


# From above graphs we can see that most of the buyers are of age group 26-35 years female.

# # State

# In[50]:


sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,8)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[51]:


sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively

# # Marital Status

# In[53]:


ax = sns.countplot(data = df, x = 'Marital_Status')

for bars in ax.containers:
    ax.bar_label(bars)

sns.set(rc={'figure.figsize':(7,5)})    


# In[54]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# # Occupation

# In[55]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[56]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# # Product Category

# In[57]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[58]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[59]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[62]:


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
