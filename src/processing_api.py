
# coding: utf-8

# In[1]:

def look_up_data(data):
    for d in data:
        for key in d:
            print key, d[key]
        break
def read_data(file_name):
    data = []
    with open(file_name, 'r') as data_file:
        for line in data_file:
            data.append(json.loads(line))
    return data


# In[ ]:



