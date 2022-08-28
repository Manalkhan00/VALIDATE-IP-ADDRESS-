#!/usr/bin/env python
# coding: utf-8

# # VALIDATE IP ADDRESS                                          MANAL EB20102055

# In[ ]:


Goal is given an ip string,validate if it is either IPv4 or IPv6 or neither.
First,rules for IPv4 are:
    No leading 0's for eg 012.6.7.8 is not allowed
    Range of no.s (0-255) for eg 250.124.192.1
    should have exactly 4 cells
    should have an INTEGER in each cell.
Second,rules for IPv6 are:
    Leading 0s are allowed. for eg 0AEF:0000:0:1
    0s can be compresses to just 1 zero for eg 0000=0
    Must have 8 cells.
    Nos in hexadecimal range (0000=FFFF) 1 f=15
    No cells should be empty.


# In[ ]:


2.3.89.56 #valid ip


# In[ ]:


258.4.365.0 #not valid


# In[5]:


import re
ip= input("enter IP address to check for validity: ")
pattern= "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

if(re.search(pattern,ip )):
    print(f"({ip}) is valid address")
else:
    print(f"({ip}) in Invalid address")


# In[ ]:


0-99 - [1-9]?[0-9]


# In[ ]:


100-199 -[0-9][0-9]


# In[ ]:


200-249 -2[0-4][0-9]


# In[ ]:


250-255 - 25[0-5]

