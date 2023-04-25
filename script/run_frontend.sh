docker run --name xiaoya-frontend \
-itd \
-p 23122:22 \
-p 2315:2315 \
-v /home/claude/Projects/xiao-ya:/srv/www/xiao-ya \
--network xiaoya-network \
xiaoya:0.0.1
