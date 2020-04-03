#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


###Listeye rastgele sayı atama###
def get_n_random_numbers(n=10,min=-5,max=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers


# In[3]:


get_n_random_numbers()


# In[4]:


###Dictionary kullanarak Histogram bulma###
def my_frequency_with_dict(list):
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict


# In[5]:


list_1=get_n_random_numbers(6,-3,3)
print(list_1)
my_frequency_with_dict(list_1)


# In[6]:


###Tuple kullanarak Histogram bulma###
def my_frequency_with_list_tuples(list):
    frequency_list=[]
    for i in range(len(list)):
        s=False
        for j in range(len(frequency_list)):
            if(list[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list[i],1])
    return frequency_list


# In[7]:


my_frequency_with_list_tuples(list_1)


# In[8]:


###Dictionary kullanarak listenin modunu bulma###
def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        if(my_hist_d[key]>frequency_max):
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max


# In[9]:


my_hist_d=get_n_random_numbers()
print(my_hist_d)
my_list=my_frequency_with_dict(my_hist_d)
print(my_list)
my_mode_with_dict(my_list)


# In[10]:


###Tuple kullanarak listenin modunu bulma###
def my_mode_with_tupes(my_hist_d):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_d:
        print(item,frequency)
        if(frequency>frequency_max):
            frequency_max=frequency
            mode=item
    return mode,frequency_max


# In[11]:


my_list=my_frequency_with_list_tuples(my_hist_d)
print(my_hist_d)
my_mode_with_tupes(my_list)


# In[12]:


###Bir elemanın listede olup olmadığını bulma###
def my_linear_search(my_list,item_search):
    n=len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found=(my_list[indis],indis)
    return found


# In[13]:


my_list=get_n_random_numbers(10,-5,5)
my_list


# In[15]:


my_linear_search(my_list,-4)


# In[16]:


###Listenin Ortalamasını bulma###
def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean_=t/s
    return mean_


# In[17]:


my_list=get_n_random_numbers()
print(my_list)
my_mean(my_list)


# In[18]:


###Bubble Sort ile listeyi sıralama###
def bubble_sort(my_list):
    n=len(my_list)
    print(my_list)
    for i in range (n-1,-1,-1):
        for j in range(0,i):
            if not (my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list


# In[19]:


my_list
bubble_sort(my_list)


# In[20]:


###Binary Search###
def my_binary_search(my_list,item_search):
    low=0
    high=len(my_list)-1
    while low<=high:
        mid=(low+high)//2
        if my_list[mid]==item_search:
            return my_list[mid],mid
        elif my_list[mid]>item_search:
            high=mid-1
        else:
            low=mid+1
    return 0


# In[21]:


my_list_1=get_n_random_numbers(10)
print("liste",my_list_1)
my_list_2=bubble_sort(my_list_1)
print("sıralı liste",my_list_2)
my_binary_search(my_list_2,3)


# In[22]:


###Listenin medyanını bulma###
def my_median(my_list_1):
    my_list_2=bubble_sort(my_list_1)
    print(my_list_2)
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)
        median=my_list_2[middle]
    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)-1]
        median=(middle_1+middle_2)/2
    return median


# In[23]:


my_list=get_n_random_numbers(5,-5,8)
print(my_list)
my_median(my_list)


# In[ ]:




