FROM python:3.11.1-slim-buster


COPY dashboard.py ./
COPY app.py ./
COPY df_eda.pickle ./
COPY requirements.txt ./
COPY dashboard.yaml ./



RUN python -m pip install --upgrade pip && pip install -r requirements.txt
RUN python dashboard.py

LABEL authors="enjoy@data-silence.com"
LABEL app_name='explainer'

EXPOSE 9050
ENTRYPOINT ["python3", "app.py"]
