# BIllCast


## For local development with docker-compose

1. `docker-compose up` create 3 containers
- db
- backend - uvicorn with live reload on port 8081
- frontend - vue-cli-service serve on port 5000
2. Create init db `docker-compose exec backend alembic upgrade head`
3. Add first superuser `docker-compose exec backend python bill_cast/initial_data.py`
