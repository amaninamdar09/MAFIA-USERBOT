FROM TheMafiaBot/MAFIA-USERBOT:alpine

#clonning repo 
RUN git clone https://github.com/amaninamdar09/MAFIA-USERBOT.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["bash","./H1M4N5HU0P/start.sh"]
