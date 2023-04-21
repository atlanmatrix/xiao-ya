docker run --name xiaoya-postgres \
-itd \
-p 15432:5432 \
-e POSTGRES_USER=claude \
-e POSTGRES_PASSWORD=a21e12df-93d5-47aa-8d7d-b0cb52a71e8e \
-e ALLOW_IP_RANGE=0.0.0.0/0 \
-e PGDATA=/var/lib/postgresql/data/pgdata \
-v /home/claude/Documents/pg_data:/var/lib/postgresql/data \
--network xiaoya-network \
postgres:15.2
