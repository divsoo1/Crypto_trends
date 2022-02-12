#!/usr/bin/env python
# coding: utf-8

# In[171]:


#Importing libraries and reading the csv file

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")
plt.style.use('fivethirtyeight')

jan31= pd.read_csv(r'D:\Kaggle Datasets\Top 100 Cryptocurrency 2022.csv',index_col='Ranking')
jan31.head()


# In[172]:


jan31.info()


# In[173]:


jan31['Price_USD']=jan31['Price'].str.strip('$')
del jan31['Price']
jan31.head()


# In[ ]:





# In[174]:


jan31['Price_USD']=jan31['Price_USD'].str.replace(',','')
jan31['Price_USD']=jan31['Price_USD'].astype('float')


# In[175]:


print(jan31.columns)


# In[176]:


jan31['changes_24h']=jan31['Changes 24H '].str.replace('%','')
del jan31['Changes 24H ']
jan31.columns


# In[177]:


jan31['changes_24h']=jan31['changes_24h'].str.replace('$','')


# In[178]:


jan31['changes_24h']=jan31['changes_24h'].astype('float')


# In[179]:


jan31['changes_7d']=jan31['Changes 7D '].str.replace('%','')
del jan31['Changes 7D ']
jan31.columns
jan31['changes_7d']=jan31['changes_7d'].str.replace('$','')
jan31['changes_7d']=jan31['changes_7d'].astype('float')


# In[180]:


jan31['changes_30d']=jan31['Changes 30D '].str.replace('%','')
del jan31['Changes 30D ']
jan31.columns
jan31['changes_30d']=jan31['changes_30d'].str.replace('$','')
jan31['changes_30d']=jan31['changes_30d'].astype('float')


# In[181]:


jan31['changes_1y']=jan31['Changes 1Y'].str.replace('%','')
del jan31['Changes 1Y']


# In[182]:


jan31.head()


# In[183]:


jan31.loc[22]


# In[184]:


jan31.drop(index=22)


# In[185]:


jan31['changes_1y']=jan31['changes_1y'].astype('float')


# In[190]:


jan31['market_cap_billion']=jan31['Market Cap'].str.replace('B','')


# In[192]:


del jan31["Market Cap"]


# In[198]:


jan31['market_cap_billion']=jan31['market_cap_billion'].str.strip('$')


# In[199]:


jan31['market_cap_billion']=jan31['market_cap_billion'].str.strip('%')


# In[200]:


jan31['market_cap_billion']=jan31['market_cap_billion'].astype('float')


# In[201]:


jan31.head()


# In[204]:


jan31.sort_values('market_cap_billion',ascending=False)


# In[213]:


cap= jan31[['Crypto Name','market_cap_billion']].set_index('Crypto Name')


# In[217]:


cap10= cap.sort_values('market_cap_billion',ascending=False)[:10]


# In[218]:


cap10 = cap10.assign(market_cap_perc = lambda x: (x.market_cap_billion / cap.market_cap_billion.sum())*100)


# In[219]:


#Declaring these now for later use in the plots
TOP_CAP_TITLE = 'Top 10 market capitalization'
TOP_CAP_YLABEL = '% of total cap'
# Plotting the barplot with the title defined above 
ax = cap10.market_cap_perc.plot.bar(title=TOP_CAP_TITLE)

# Annotating the y axis with the label defined above
ax.set_ylabel(TOP_CAP_YLABEL);


# In[248]:


# Colors for the bar plot
COLORS = ['orange', 'green', 'orange', 'cyan', 'cyan', 'blue', 'silver', 'orange', 'red', 'green']

# Plotting market_cap_usd as before but adding the colors and scaling the y-axis  
ax = cap10.market_cap_billion.plot.bar(title=TOP_CAP_TITLE, logy=True, color = COLORS)

# Annotating the y axis with log(USD)
ax.set_ylabel('log(Billion USD)')

# Final touch! Removing the xlabel as it is not very informative
ax.set_xlabel('');


# In[224]:


# Selecting the id, percent_change_24h and percent_change_7d columns
volatility = jan31[['Crypto Name','changes_24h','changes_7d']]

# Setting the index to 'id' and dropping all NaN rows
volatility = volatility.set_index('Crypto Name').dropna()

# Sorting the DataFrame by percent_change_24h in ascending order
volatility = volatility.sort_values('changes_24h')

# Checking the first few rows
volatility.head()


# In[227]:


# Defining a function with 2 parameters, the series to plot and the title
def top10_subplot(volatility_series, title):
    # making the subplot and the figure for nrows and ncolumns
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))
    # Plotting with pandas the barchart for the top 10 losers with the color RED
    ax = volatility_series[:10].plot.bar(color="darkred", ax=axes[0])
    # Setting the main title to TITLE
    fig.suptitle(title)
    # Setting the ylabel to "% change"
    ax.set_ylabel('% change')
    # Same as above, but for the top 10 winners and in darkblue
    ax = volatility_series[-10:].plot.bar(color="darkblue", ax=axes[1])
    # Returning this for good practice, might use later
    return fig, ax

DTITLE = "24 hours top losers and winners"

# Calling the function above with the volatility.percent_change_24h series
# and title DTITLE 
fig, ax = top10_subplot(volatility.changes_24h, DTITLE)


# In[228]:


# Sorting in ascending order
volatility7d = volatility['changes_7d'].sort_values()

WTITLE = "Weekly top losers and winners"

# Calling the top10_subplot function
fig, ax = top10_subplot(volatility7d,WTITLE)


# In[229]:


# Selecting everything bigger than 10 billion 
largecaps = cap.query('market_cap_billion>10')

# Printing out largecaps
print(largecaps)


# In[237]:


highest_returns=jan31.sort_values('changes_1y',ascending=False)[:10][['Crypto Name','changes_1y']]
print(highest_returns)


# In[238]:


lowest_returns=jan31.sort_values('changes_1y',ascending=True)[:10][['Crypto Name','changes_1y']]
print(lowest_returns)


# In[253]:


highest_returns.plot.bar(x='Crypto Name',y='changes_1y',xlabel="Crypto",ylabel='Positive Precentage Change',title="Yearly Returns")

plt.show()


# In[251]:


lowest_returns.plot.bar(x='Crypto Name',y='changes_1y',xlabel="Crypto",ylabel='Nagative Precentage Change',title="Yearly Loss")

plt.show()


# In[ ]:














