docker run --name xiaoya-redis \
-itd \
-p 16379:6379 \
-v /home/claude/Documents/redis_data:/data \
--network xiaoya-network \
redis redis-server --save 60 1 --loglevel warning
