# Инструкция по деплою на Railway

## Что было исправлено

1. ✅ Добавлен **WhiteNoise** для раздачи статических файлов в продакшене
2. ✅ Настроен middleware и storage для статики
3. ✅ Исправлена конфигурация DEBUG (теперь корректно читается из переменных окружения)
4. ✅ Создан Procfile для запуска приложения
5. ✅ Создан build.sh скрипт для сборки статики и миграций
6. ✅ Создан railway.json с конфигурацией

## Настройка переменных окружения в Railway

В панели Railway нужно добавить следующие переменные окружения:

### Обязательные переменные:

```bash
SECRET_KEY=ваш-секретный-ключ-сгенерируйте-новый
DEBUG=False
ALLOWED_HOSTS=your-app.railway.app,dobrosnov.shop
CSRF_TRUSTED_ORIGINS=https://your-app.railway.app,https://dobrosnov.shop

# Для автоматического создания суперпользователя при деплое:
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=ваш-надежный-пароль
```

**Важно:**
- `CSRF_TRUSTED_ORIGINS` должен включать протокол `https://`!
- Суперпользователь будет создан автоматически при первом деплое, если указаны `DJANGO_SUPERUSER_*` переменные

### Генерация SECRET_KEY

Выполните в терминале:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Опционально (если используете PostgreSQL):

```bash
DATABASE_URL=postgresql://user:password@host:port/dbname
```

## Шаги для деплоя

1. **Загрузите код на GitHub** (если еще не загружен)

2. **Подключите Railway к репозиторию:**
   - Зайдите на railway.app
   - Создайте новый проект
   - Выберите "Deploy from GitHub repo"
   - Выберите ваш репозиторий

3. **Добавьте переменные окружения:**
   - Перейдите в Variables
   - Добавьте SECRET_KEY, DEBUG, ALLOWED_HOSTS

4. **Railway автоматически:**
   - Установит зависимости из requirements.txt
   - Выполнит build.sh (collectstatic + migrate)
   - Запустит приложение через gunicorn

5. **Проверьте деплой:**
   - Откройте URL вашего приложения
   - Статика должна загружаться корректно!

6. **Суперпользователь создается автоматически!**

   Railway использует новую базу данных. Если вы добавили переменные окружения:
   - `DJANGO_SUPERUSER_USERNAME`
   - `DJANGO_SUPERUSER_EMAIL`
   - `DJANGO_SUPERUSER_PASSWORD`

   То суперпользователь создастся автоматически при деплое! Просто войдите в `/admin/` с указанными данными.

   **Если нужно создать вручную:**

   Запустите локально (если railway CLI настроен):
   ```bash
   railway run python manage.py createsuperuser
   ```

   Или добавьте переменные окружения выше и сделайте редеплой в Railway (Settings → Redeploy)

## Важно!

- После первого деплоя добавьте домен Railway в `ALLOWED_HOSTS` и `CSRF_TRUSTED_ORIGINS`
- Пример `ALLOWED_HOSTS`: `your-app.railway.app,dobrosnov.shop`
- Пример `CSRF_TRUSTED_ORIGINS`: `https://your-app.railway.app,https://dobrosnov.shop`
- Для production обязательно `DEBUG=False`
- **CSRF_TRUSTED_ORIGINS требует протокол https:// в начале каждого домена!**

## Локальная разработка

Для локальной разработки оставьте в `.env`:
```bash
SECRET_KEY=ваш-локальный-ключ
DEBUG=True
```

## Проверка статики локально

Чтобы проверить как работает статика в production режиме локально:

```bash
python manage.py collectstatic
DEBUG=False python manage.py runserver
```

Статика должна отдаваться через WhiteNoise даже при DEBUG=False.
