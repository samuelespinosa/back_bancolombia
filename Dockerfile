FROM python:3.11.5-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE "bancolombia.settings"
ENV USERNAME 'admin'
ENV DATABASE 'ibmclouddb'
ENV PASSWORD 'ceefdaf113f2226a7a94eff050e8af9537eee9dafd2270c75a59'
ENV PGPASSWORD 'ceefdaf113f2226a7a94eff050e8af9537eee9dafd2270c75a59'
ENV HOST='b04fa70e-33f5-4118-b5b0-033a7529e5cc.bkvfv1ld0bj2bdbncbeg.databases.appdomain.cloud'
ENV PGSSLROOTCERT './db_bancolombia.pub'

WORKDIR /code/back_end

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
