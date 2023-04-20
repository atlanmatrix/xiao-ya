# -*- coding: utf-8 -*-
# @Author:  Claude Manchester
# Time   : 2023/2/17 11:14

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from backend.logs import logger


class PG:
    """
    数据库ORM配置类
    """

    def __init__(self, url):
        """
        :param url: postgresql database url
        """
        self.url = url
        logger.debug('=' * 50)
        logger.debug(f'Init PostgresSQL connection: {url}')

        self.engine = self.get_engine()
        logger.debug(f'Init PostgresSQL connection finished')
        logger.debug('=' * 50)

    def get_engine(self, **kwargs):
        return create_async_engine(
            self.url,
            future=True,
            pool_size=20,
            max_overflow=10,
            query_cache_size=20480,
            pool_recycle=1600,
            pool_pre_ping=True,
            pool_use_lifo=True,
        )

    async def connect(self):
        try:
            async with self.engine.connect():
                pass
            return True
        except ConnectionError as conn:
            print(f"连接数据库失败: {conn}")
            raise ConnectionError()
        except Exception as err:
            print(f"连接数据库失败: {err}")
            raise err

    async def close(self):
        try:
            await self.engine.dispose()
        except ConnectionError as conn:
            # logger.error(f"连接数据库失败: {conn}")
            print(f"关闭数据库连接失败: {conn}")
            raise ConnectionError
        except Exception as err:
            # logger.error(f"关闭数据库连接失败: {err}")
            print(f"关闭数据库连接失败: {err}")
            raise err
