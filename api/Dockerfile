FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install -r ./requirements.txt
ENTRYPOINT [ "uvicorn" ]
CMD [ "app:app" ,"--host" ,"0.0.0.0" ,"--port" ,"8000" ]
