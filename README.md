# AAcademyTestProject
---
### Развертывание
Для развертывания приложения требуется Docker и Docker-compose.
1. Создать корневую папку проекта
2. Склонировать репозиторий
3. ***ВАЖНО:*** Назначить права на выполнение файла ***./start.sh*** командой ***chmod +x ./start.sh***
4. ***ВАЖНО:*** Назначить права на запись и чтение в корневой директории командой ***chmod +rw .***
5. При необходимости отредактировать ***docker-compose*** файл
6. Выполнить ***sudo docker-compose up*** <br/>
Для запуска в фоне выполнить ***sudo docker-compose up -d*** <br/>
Для остановки выполнить ***sudo docker-compose down***
---
### Тесты
Тесты запускаются автоматически при запуске сервиса. Лог тестов сохраняется в файл ***test_logs.txt***
Для ручного запуска: ***python ./src/manage.py test*** (требуется установить зависимости в систему)

---
### Дроп базы данных
Чтобы очистить базу данных выполнить: ***sudo rm -rf ./data*** в корневой директории проекта
