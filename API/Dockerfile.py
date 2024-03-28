FROM python:3.12.1
WORKDIR /api
COPY api/. /api
COPY api/app.py /api/app.py
COPY requirements.txt /api
RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD uvicorn --host 0.0.0.0 --port 8000 api.app:app
EXPOSE 8000