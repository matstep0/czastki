#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv("Wenu.csv")
print(df.info())
print(df.head())


# In[14]:


typeEB=df.loc[(df.type=="EB")]
typeEE=df.loc[(df.type=="EE")]


# In[59]:


zmienna=["sigmaEtaEta","HoverE","isoTrackpt","isoEcalpt","isoHcalpt"]
ciecia={}
ciecia["EB"]=[0.011,0.045,0.1,0.08,0.1]
ciecia["EE"]=[0.033,0.025,0.04,0.06,0.03]
newdata = pd.DataFrame().assign(type=df.type,
                            sigmaEtaEta=df.sigmaEtaEta, 
                            HoverE=df.HoverE, 
                            isoTrackpt=df.isoTrack/df.pt, 
                            isoEcalpt=df.isoEcal/df.pt,
                            isoHcalpt=df.isoHcal/df.pt)


# In[ ]:





# In[90]:


region="EB"
all=len(newdata.loc[(newdata.type==region)])
for i in range(len(zmienna)):
    print(len(newdata.loc[(newdata[zmienna[i]]<ciecia[region][i]) & (newdata.type==region)])/all)
    


# In[91]:


region="EE"
all=len(newdata.loc[(newdata.type==region)])
for i in range(len(zmienna)):
    print(len(newdata.loc[(newdata[zmienna[i]]<ciecia[region][i]) & (newdata.type==region)])/all)


# In[99]:


region="EB"
all=len(newdata.loc[(newdata.type==region)])
for i in range(len(zmienna)+1):
    data=newdata.loc[newdata.type==region]
    for j in range(len(zmienna)):
        if(j!=i): data=data.loc[(data[zmienna[j]]<ciecia[region][j]) & (data.type==region)]
    print(len(data)/all)


# In[98]:


region="EE"
all=len(newdata.loc[(newdata.type==region)])
for i in range(len(zmienna)+1):
    data=newdata.loc[newdata.type==region]
    for j in range(len(zmienna)):
        if(j!=i): data=data.loc[(data[zmienna[j]]<ciecia[region][j]) & (data.type==region)]
    print(len(data)/all)


# In[110]:


x=newdata.loc[(newdata.type==region)]
plt.hist(x.sigmaEtaEta)


# In[104]:


plt.hist(newdata.sigmaEtaEta,bins=50)


# In[105]:


region="EB"
data=newdata.loc[(newdata.type==region)]
for i in range(zmienna):
    name=zmienna[i]
    x=data.name
    y=data.loc[(data.name<ciecia[region][i])]
    plt.hist()
    plt=typeEB[name].plot(kind="hist",bins=50,range=[20,120])
    plt.set_xlabel(name)
    plt.set_ylabel("Number of events")
    fig = plt.get_figure()
    fig.savefig('EB/EB_'+name+'.pdf')


# In[ ]:




