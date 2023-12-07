FROM python:3.9
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY app/ server/app/
COPY migrations/ server/migrations/

COPY ./entrypoint.sh ./entrypoint.sh
COPY ./.env ./server/.env

RUN chmod u+x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]