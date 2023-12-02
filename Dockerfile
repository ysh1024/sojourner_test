FROM python:3.8.3

# 현재 디렉토리의 모든 파일들을 컨테이너의 /app 디렉토리에 복사한다.
COPY . /app

# 작업 위치가 /app이라는 뜻
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 8000

#CMD ["python", "/app/manage.py", "makemigrations"]
#CMD ["python", "/app/manage.py", "migrate"]
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]