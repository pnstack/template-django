FROM python:3.11-alpine

WORKDIR /app

COPY . /app

# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

EXPOSE 5000
CMD ["python", "manage.py", "runserver", "5000"]