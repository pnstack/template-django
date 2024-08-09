FROM python:3.11-slim

RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc && \
  apt-get install -y ffmpeg libsm6 libxext6 && \
  apt-get install -y zbar-tools && \
  apt-get install -y libzbar-dev

WORKDIR /app

COPY . /app

# install environment dependencies
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

EXPOSE 5000
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]