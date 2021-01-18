---
1. Ознайомився з Docker, запустив перевірку версії, виведення допомоги та тестовий імедж. Все в "work.log."
---
2. Створив власний репозиторій на Docker Hub - legarda/lab4/
---
3. Виконав команду для запуску веб-сервера "sudo docker run -it --name=django --rm -p 8000:8000 legarda/lab4:django"
---
4. Створив Dockerfile.site
---
5. Виконав команди імеджа: sudo docker build -t legarda/lab4:monitoring . --file Dockerfile.site sudo docker images sudo docker push legarda/lab4:monitoring
---
6. Щоб отримати логи виконав команди: sudo docker run -it --name=django --rm -p 8000:8000 legarda/lab4:django sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log legarda/lab4:monitoring
