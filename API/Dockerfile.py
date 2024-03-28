FROM python:3.11.8
WORKDIR /api
COPY api/. /api
COPY /api/XGBoost_artifacts.pkl/. /api/XGBoost_artifacts.pkl
COPY api/app.py /api/app.py
COPY requirements.txt /api
RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD "api.app:app", "--host", "0.0.0.0", "--port", "8000"
EXPOSE 8000