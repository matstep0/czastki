#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("Wenu.csv")
print(df.info())
print(df.head())


# In[3]:


typeQ=df.loc[:,["Q","type"] ]


# In[4]:


EB1=len(typeQ.loc[(typeQ.Q==1) & (typeQ.type=="EB")])
EBm1=len(typeQ.loc[(typeQ.Q==-1) & (typeQ.type=="EB")])
EE1=len(typeQ.loc[(typeQ.Q==1) & (typeQ.type=="EE")])
EEm1=len(typeQ.loc[(typeQ.Q==-1) & (typeQ.type=="EE")])
data={-1: [EBm1,EEm1] ,1: [EB1,EE1] }
pd.DataFrame(data,index=["EB","EE"])


# In[5]:


runy=typeQ=df.loc[:,["Q","type","Run"] ]


# In[6]:


def fun(typeQ):
    EB1=len(typeQ.loc[(typeQ.Q==1) & (typeQ.type=="EB")])
    EBm1=len(typeQ.loc[(typeQ.Q==-1) & (typeQ.type=="EB")])
    EE1=len(typeQ.loc[(typeQ.Q==1) & (typeQ.type=="EE")])
    EEm1=len(typeQ.loc[(typeQ.Q==-1) & (typeQ.type=="EE")])
    return [EEm1,EBm1,EE1,EB1, EB1+EBm1+EE1+EEm1]
    


# In[7]:


groped=runy.groupby("Run").apply(fun)
groped


# In[8]:


print(df.columns)


# In[9]:


zakres=['pt', 'eta', 'phi', 'Q', 'MET',
       'phiMET' ]


# In[10]:


typeEB=df.loc[(df.type=="EB")]
typeEE=df.loc[(df.type=="EE")]


# In[11]:


i=0
name=zakres[i]
plt=typeEB[name].plot(kind="hist",bins=50,range=[20,120])
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EB/EB_'+name+'.pdf')


# In[12]:


i=1
name=zakres[i]
plt=typeEB[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EB/EB_'+name+'.pdf')


# In[13]:


i=2
name=zakres[i]
plt=typeEB[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EB/EB_'+name+'.pdf')


# In[14]:


i=3
name=zakres[i]
plt=typeEB[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EB/EB_'+name+'.pdf')


# In[ ]:





# In[15]:


i=4
name=zakres[i]
plt=typeEB[name].plot(kind="hist",bins=50,range=[0,150])
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EB/EB_'+name+'.pdf')


# In[16]:


i=5
name=zakres[i]
plt=typeEB[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EB/EB_'+name+'.pdf')


# In[17]:


i=0
name=zakres[i]
plt=typeEE[name].plot(kind="hist",bins=50,range=[20,120])
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EE/EE_'+name+'.pdf')


# In[18]:


i=1
name=zakres[i]
plt=typeEE[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EE/EE_'+name+'.pdf')


# In[19]:


i=2
name=zakres[i]
plt=typeEE[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EE/EE_'+name+'.pdf')


# In[20]:


i=3
name=zakres[i]
plt=typeEE[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EE/EE_'+name+'.pdf')


# In[21]:


i=4
name=zakres[i]
plt=typeEE[name].plot(kind="hist",bins=50,range=[0,150])
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EE/EE_'+name+'.pdf')


# In[22]:


i=5
name=zakres[i]
plt=typeEE[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EE/EE_'+name+'.pdf')


# In[23]:


i=0
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50,range=[20,120])
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EBEE/_'+name+'.pdf')


# In[24]:


i=1
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EBEE/_'+name+'.pdf')


# In[25]:


i=2
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EBEE/_'+name+'.pdf')


# In[26]:


i=3
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EBEE/_'+name+'.pdf')


# In[27]:


i=4
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50,range=[0,150])
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EBEE/_'+name+'.pdf')


# In[28]:


i=5
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('EBEE/_'+name+'.pdf')


# In[29]:


data=df.loc[df.pt>25]


# In[30]:


i=0
name=zakres[i]
plt=data[name].plot(kind="hist",bins=50,range=[20,120])
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('ciete25/_'+name+'.pdf')


# In[31]:


i=1
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('ciete25/_'+name+'.pdf')


# In[32]:


i=4
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
fig = plt.get_figure()
fig.savefig('ciete25/_'+name+'.pdf')


# In[33]:


i=5
name=zakres[i]
plt=df[name].plot(kind="hist",bins=50)
plt.set_xlabel(name)
plt.set_ylabel("Number of events")
>fig = plt.get_figure()
fig.savefig('ciete25/_'+name+'.pdf')


# In[ ]:




