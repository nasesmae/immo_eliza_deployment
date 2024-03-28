FROM python:3.12.1
WORKDIR /API
COPY API/. /API
COPY API/app.py /API/app.py
COPY requirements.txt /API
RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD ["app:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000

