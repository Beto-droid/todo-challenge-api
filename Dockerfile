FROM python:3.13.0
LABEL authors="alberto"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Port Django
EXPOSE 8000

# Commands
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]