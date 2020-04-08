#!/usr/bin/env python
# coding: utf-8

# In[24]:


filename=input("입력 파일 이름: ")
infile=open(filename,"r")
count={}
for line in infile:
    line=line.rstrip()
    for ch in line:
        count[ch]=count.get(ch,0)+1
print(count)  


# In[ ]:




