FROM mrismanaziz/man-userbot:buster

RUN git clone -b Zelda-Ubot https://github.com/nmiabdfhmy/Zelda-Ubot /home/zeldaubot/ \
    && chmod 777 /home/zeldaubot \
    && mkdir /home/zeldaubot/bin/

COPY ./sample_config.env ./config.env* /home/zeldaubot/

WORKDIR /home/zeldaubot/

CMD ["python3", "-m", "userbot"]
