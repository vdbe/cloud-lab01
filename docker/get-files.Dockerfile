ARG FILE=get-files

FROM python:latest as base

WORKDIR /usr/src/app

COPY scripts/requirements.${FILE}.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY scripts/${FILE}.py .

CMD [ "python", "./${FILE}.py" ]