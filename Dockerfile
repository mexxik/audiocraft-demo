FROM python:3.9-slim

RUN python -m pip install 'torch==2.1.0'
RUN python -m pip install setuptools wheel
RUN python -m pip install audiocraft

RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY demo.py /app/demo.py

WORKDIR /app

CMD [ "python", "demo.py" ]