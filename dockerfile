FROM python:3.10 AS base
 
ENV APP_HOME=/app
ENV APP_USER=app
 
RUN groupadd -r $APP_USER && \
    useradd -r -g $APP_USER -d $APP_HOME -s /sbin/nologin -c "Docker image user" $APP_USER
 
WORKDIR $APP_HOME
 
ENV TZ 'Europe/Madrid'
RUN echo $TZ > /etc/timezone && apt-get update && \
    apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean
 
RUN pip install --upgrade pip
 
FROM base
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
COPY requirements.txt .
RUN pip install -r requirements.txt
 
ADD app .
 
RUN chown -R $APP_USER:$APP_USER $APP_HOME
USER $APP_USER
CMD [ "uvicorn", "main:app", "--lifespan", "on", "--workers", "1", "--host", "0.0.0.0", "--port","3000" ]
