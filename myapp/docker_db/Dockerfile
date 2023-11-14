# /myapp/docker_db/Dockerfile

# 공식 PostgreSQL 이미지를 베이스로 사용합니다.
FROM postgres:latest


# ARG를 사용하여 빌드 시점에 값을 받습니다.
ARG POSTGRES_DB_ARG=mydb  # 기본값을 설정할 수 있습니다.
ARG POSTGRES_USER_ARG
ARG POSTGRES_PASSWORD_ARG

# ENV를 사용하여 환경 변수로 설정합니다.
ENV POSTGRES_DB=$POSTGRES_DB_ARG
ENV POSTGRES_USER=$POSTGRES_USER_ARG
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD_ARG


# 초기화 스크립트 추가 (옵션)
# Docker 공식 PostgreSQL 이미지는 /docker-entrypoint-initdb.d/ 디렉토리에 있는 모든 .sh, .sql, .sql.gz 파일을 실행합니다.
# 이 디렉토리에 초기화 스크립트를 추가하면 데이터베이스가 처음 시작될 때 이 스크립트가 실행됩니다.
# COPY ./init.sql /docker-entrypoint-initdb.d/

# # 도커-콤포즈를 통하지 않고 직접 빌드하고 실행해볼 때에는 아래 명령어를 사용
# # 이 도커 이미지를 빌드할 때 아래 명령어로 환경 변수를 설정해야 한다.
# docker build -t my_docker_db \
#   --build-arg POSTGRES_USER_ARG=postgres \
#   --build-arg POSTGRES_PASSWORD_ARG=postgres \
#   --build-arg POSTGRES_DB_ARG=daera_clear \
#   ./docker_db 

# # 또는 빌드하면서 바로 실행까지 해볼 수 있다.
# docker build -t my_docker_db \
#   --build-arg POSTGRES_USER_ARG=postgres \
#   --build-arg POSTGRES_PASSWORD_ARG=postgres \
#   --build-arg POSTGRES_DB_ARG=daera_clear \
#   ./docker_db && docker run -d -p 5432:5432 --name my_running_db my_docker_db

