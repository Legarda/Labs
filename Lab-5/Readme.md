Прочитав все, що стосується "docker-compose" та бібліотеки "Flask".

Створив папку "my_app" і папку "tests".

Перевірив працездатність проекту за допомогою команд "pipenv --python 3.7", "pipenv install -r requirements.txt", "pipenv run python app.py".

Виникли 2 помилки. Перша полягала у "redis-server" він не був встановлений і запущений, друга полягала у відсутності папки "Logs", створив вручну і все запрацювало.

Провів тести за допомогою команди "pipenv run pytest test_app.py --url http://localhost:5000" всі вони пройшли успішно.

Перевірив роботу сайту та перейшов на всі його сторінки.

Очистив середовище, після чого створив два файла "Dockerfile.app" та "Dockerfile.tests", а також "Makefile" для автоматизації процесу.

Описую кожну директиву "Makefile":

REPO - змінна для зберігання назви Docker репозиторію PHONY - дозволяє оголошувати фальшиві цілі STATES - змінна для зберігання директив run - директива для створення мережі test-app - директива для запуску контейнера з моніторингом docker-prune - видалення контейнерів, волюмів, мереж i імеджів $(STATES) - директива для білда самого контейнера docker-delete - директива для видалення імелжів 9. Завантажив імеджі до Docker Hub репозиторію: https://hub.docker.com/r/denysitis/labpy4/tags?page=1&ordering=last_updated

Переходжу до Docker-compose, перевірив чи встановлений "Docker-compose" та запустив його за допомогою команди "docker-compose -p lab5 up"

Веб-сайт працює, адреса для переходу на сайт - http:/0.0.0.0/ Скрішоти сторінок сайту:

![Image alt](https://github.com/Legarda/Labs/raw/main/Lab-5/screenshot_1.jpg)
![Image alt](https://github.com/Legarda/Labs/raw/main/Lab-5/screenshot_2.jpg)