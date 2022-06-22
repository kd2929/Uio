FROM python:3.9.7-slim-buster


WORKDIR .
RUN apt -qq update && apt -qq upgrade
COPY . .
RUN pip3 install -r requirements.txt
RUN apt install ffmpeg

CMD ["python3", "main.py"]
