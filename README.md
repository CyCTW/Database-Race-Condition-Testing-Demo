# Database Race Condition Testing Demo

This repo aim to provide some implementation of common race condition cases *(ex: concurrent write, etc.)* when interacting with Database.

This Demo repo use [FastAPI](https://fastapi.tiangolo.com/) as Python WSGI framework and [PostgreSQL](https://www.postgresql.org/) as Database. In database operation, it use [SQLAlchemy](https://www.sqlalchemy.org/).

Also, this repo provides Docker deployment environment that every user can easily follow the instructions and run the demo in local.

## How to run?
### Run Docker containers (FastAPI & PostgreSQL)
```
docker-compose up --build
```
### Create Mock Data
```
cd scripts/MockData
./create_data.sh
```
### Run testing scripts
ex:
```
cd scripts/RaceCondition
./test_for_update.sh
```
This case tests the concurrent write for same data row. 

By using SQL command `SELECT ... FOR UPDATE NOWAIT`, the first transaction that accessed resource will lock the resources it needed. Then, slower transactions that accessed the same data will be blocked.

Finally, `SELECT ... FOR UPDATE NOWAIT` solves the problems of concurrent write by ensuring that only one transaction can be executed.
