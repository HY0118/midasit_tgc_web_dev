# midasit_tgc_todo_db_py
version python.


## install

### fastapi 사용

```
pip install fastapi
pip install "uvicorn[standard]"
```
### Maria DB 사용
```
pip install sqlalchemy pymysql
```


## launch

### Db 실행
- .env 작성
- `docker` 폴더 내에서 명령어 실행 `$ docker-compose up -d`

### Server 실행

```
$ uvicorn main:app --reload --host 0.0.0.0
$ uvicorn "$main위치":app --reload --host 0.0.0.0

//example : main이 app 하위에 있을 경우
$ uvicorn app.main:app --reload --host 0.0.0.0 --port 8081
$ python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8081

```

## Swagger

뒤에 `/docs` 붙이면 됩니다

`http://localhost:8000/docs`