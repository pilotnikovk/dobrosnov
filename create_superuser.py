#!/usr/bin/env python
"""
Скрипт для создания суперпользователя
Запустите: python create_superuser.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = input('Введите username: ')
email = input('Введите email: ')
password = input('Введите password: ')

if User.objects.filter(username=username).exists():
    print(f'Пользователь {username} уже существует!')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Суперпользователь {username} успешно создан!')
