# Using Python Slim-Bullsye
FROM nekru/riam:ubot

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/Ncode2014/leaf-ubot /home/leaf-ubot/ \
    && chmod 777 /home/leaf-ubot \
    && mkdir /home/leaf-ubot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/leaf-ubot/

# Setup Working Directory
WORKDIR /home/leaf-ubot/

# Finalization
CMD ["python3","-m","userbot"]
