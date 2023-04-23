docker run --name xiaoya-nginx \
-itd \
-p 5032:80 \
-v /home/claude/Projects/xiao-ya/script/nginx/nginx.conf:/etc/nginx/nginx.conf \
-v /home/claude/Projects/xiao-ya/script/nginx/default.conf:/etc/nginx/conf.d/default.conf \
--network xiaoya-network \
nginx:stable-alpine-perl
