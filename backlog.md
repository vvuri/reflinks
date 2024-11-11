## FastAPI
- рефакторин router и различные файлы
- TypeSpec дописать -> openapi -> Swagger -> ?
- API функции описать базовые команды
- уникальный id для файлов и ответов
- Swagger протестировать функции
- JWT видео -> интегрировать
- Добавить html формы и доступ к ним
- Пишем Auth html + show auth
- Logs добавить -> Console
- Debuging по шагам
- Сохранение фото 
- MongoDB сохранение линков
- Redis для очередей и переделать на очереди
- Vue формы создать
- Docker-compose + nginx + static Vue
- Metrics + Prometheus
- OpenTelemetry
- ML сервис разбора фото
- Golang переделать основной сервис

## REST API
- put: /addlink <- id unic
- put: /addimage <- id unic
- get: /ref/{id} <- image
- get: /refinfo/{id} <- image info
- get: /refpreview/{page} <- набор превьюшек и линки  
- post: /refupdate {id, новая инфа } <- 200 OK
