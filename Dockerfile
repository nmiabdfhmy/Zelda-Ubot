FROM fhmyngrh/zeldaubot:buster

RUN git clone -b ZeldaUbot https://github.com/fhmyngrh/ZeldaUbot /home/zeldaubot/ \
    && chmod 777 /home/zeldaubot \
    && mkdir /home/zeldaubot/bin/

COPY ./sample_config.env ./config.env* /home/zeldaubot/

WORKDIR /home/zeldaubot/

CMD ["python3", "-m", "userbot"]
