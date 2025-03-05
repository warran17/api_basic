#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
import requests

# API - to fetch temperature of a city
city_name = input('Enter a City Name:')
api_key = '648d396676dab5f3ef31500189625fa7'

# To build the Api URL
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information = requests.get(api_url)
data = get_server_information.json()
print(data)


# In[ ]:




