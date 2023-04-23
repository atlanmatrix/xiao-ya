docker run --name xiaoya-backend \
-itd \
-p 23022:22 \
-p 2305:2305 \
-e POSTGRES_USER=claude \
-e POSTGRES_PASSWORD=a21e12df-93d5-47aa-8d7d-b0cb52a71e8e \
-v /home/claude/Projects/xiao-ya:/srv/www/xiao-ya \
--network xiaoya-network \
xiaoya:0.0.1
