# 기본 이미지로 python과 postgresql이 설치된 이미지를 사용
FROM python:3.9-slim-buster

# PostgreSQL 패키지 저장소 추가 및 설치
RUN apt-get update && apt-get install -y wget gnupg
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list

RUN apt-get update && apt-get -y install postgresql-13

# 작업 디렉토리 설정
WORKDIR /myapp

# Python 패키지 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 모든 애플리케이션 파일 복사
COPY . .

# PostgreSQL 초기 설정 및 테이블 생성
USER postgres
RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
    createdb -O docker docker &&\
    psql docker -f ./myapp/init.sql

# >> postgresql을 중지시키는 명령어, 일단 주석!
# # 이 부분에서 bash -c를 사용해 복잡한 명령을 실행합니다.
# RUN bash -c "/etc/init.d/postgresql stop"

# 일단 개발 단계에서는 backend/app.py를 실행하지 않는다.
# # 백엔드 애플리케이션 실행 (예: Flask)
# CMD /etc/init.d/postgresql start && python backend/app.py