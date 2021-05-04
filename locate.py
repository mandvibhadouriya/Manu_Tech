# Give your Phone number and see its location

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import phonenumbers


# In[2]:


from phonenumbers import geocoder


# In[8]:


num1 = phonenumbers.parse("+123456789")
print(geocoder.description_for_number(num1,'en'))

