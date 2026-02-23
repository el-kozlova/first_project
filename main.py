#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Импорт load_dotenv.
from dotenv import load_dotenv 
# Импорт библиотеки для работы с окружением.
import os  


# In[2]:


def print_author():
    # Загрузка переменных из .env
    load_dotenv(dotenv_path='C://Users//Laborant//Desktop//Python_ya//first_project//first_project//author.env')
    
    # Теперь переменные доступны через os.environ
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}") 

