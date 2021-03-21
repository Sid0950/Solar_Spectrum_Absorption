#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('Spectrum3.csv')
data['W/m2'] = data['Wvlgth nm']* data['Direct+circumsolar W*m-2*nm-1']
data.loc[data['Wvlgth nm']<=380, 'abs_coeff'] = 5
data.loc[(data['Wvlgth nm']>380) & (data['Wvlgth nm'] < 800), 'abs_coeff'] = 0
data.loc[data['Wvlgth nm']>=800, 'abs_coeff'] = 100

#For calculating the energy out
pen_depth = 0.018
data['W/m2/nm_out'] = data['Direct+circumsolar W*m-2*nm-1']*(2.718)**(-pen_depth*data['abs_coeff'])

#Wavelenghts absorbed by water film
data['W/m2/nm_abs'] = data['Direct+circumsolar W*m-2*nm-1'] - data['W/m2/nm_out']


# In[35]:


data.head()


# In[36]:


data.tail(5)


# In[37]:


data[['Direct+circumsolar W*m-2*nm-1', 'W/m2/nm_out']].plot()


# In[38]:


print(len(data))


# In[1]:


#finding the area under the curve for incoming radiation
a = []
for i in range(1,2002):
    a.append(i)
print(a)


# In[40]:


area_incoming = []
for n in a:
    h_i = data['Direct+circumsolar W*m-2*nm-1'].loc[n-1]
    d_i = data['Wvlgth nm'].loc[n] - data['Wvlgth nm'].loc[n-1]
    area_incoming.append(h_i*d_i)
x = sum(area_incoming)
x


# In[41]:


b = []
for j in range(1,2002):
    b.append(j)
area_outgoing = []
for m in b:
    h_o = data['W/m2/nm_out'].loc[m-1]
    d_o = data['Wvlgth nm'].loc[m] - data['Wvlgth nm'].loc[m-1]
    area_outgoing.append(h_o*d_o)
y = sum(area_outgoing)
y


# In[42]:


energy_abs = x-y
energy_abs


# In[43]:


#absorption by second fluid layer
data['W/m2/nm_out2'] = data['W/m2/nm_out']*(2.718)**(-pen_depth*data['abs_coeff'])


# In[44]:


data.tail()


# In[45]:


data[['Direct+circumsolar W*m-2*nm-1','W/m2/nm_out','W/m2/nm_out2']].plot(xlim=(200,2500),ylim = (0,1.6))


# In[46]:


c = []
for k in range(1,2002):
    b.append(k)
area_outgoing2 = []
for w in b:
    h_o2 = data['W/m2/nm_out2'].loc[w-1]
    d_o2 = data['Wvlgth nm'].loc[w] - data['Wvlgth nm'].loc[w-1]
    area_outgoing.append(h_o2*d_o2)
p = sum(area_outgoing2)
p


# In[47]:


data['Direct+circumsolar W*m-2*nm-1'].plot()


# In[54]:


p = data[data['Wvlgth nm']<=380]


# In[55]:


p['Direct+circumsolar W*m-2*nm-1'].plot()


# In[56]:


q = data[(data['Wvlgth nm']>380) & (data['Wvlgth nm'] < 800)]


# In[57]:


q['Direct+circumsolar W*m-2*nm-1'].plot()


# In[58]:


e = data[data['Wvlgth nm']>=800]


# In[59]:


e['Direct+circumsolar W*m-2*nm-1'].plot()

