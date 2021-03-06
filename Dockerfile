FROM python:3 as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --no-warn-script-location --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY . /app
WORKDIR /app

CMD ["python", "./main.py"]

