ARG FILE="main"
ARG IMAGE="python:3"

FROM ${IMAGE}

ARG FILE


WORKDIR /usr/src/app

COPY requirements.${FILE}.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ${FILE}.py main.py

CMD python ./main.py
