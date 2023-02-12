from typing import AsyncGenerator

import aio_pika
from aio_pika.pool import Pool

from src.infrastructure.message_broker.factories import ChannelFactory, ConnectionFactory

from .config import EventBusConfig


def build_rq_connection_pool(event_bus_config: EventBusConfig) -> Pool[aio_pika.abc.AbstractConnection]:
    rq_connection_pool = Pool(ConnectionFactory(event_bus_config.rabbitmq_uri).get_connection, max_size=10)
    return rq_connection_pool


def build_rq_channel_pool(rq_connection_pool: Pool[aio_pika.abc.AbstractConnection]) -> Pool[aio_pika.abc.AbstractChannel]:
    rq_channel_pool = Pool(ChannelFactory(rq_connection_pool).get_channel, max_size=10)
    return rq_channel_pool


async def build_rq_channel(
    rq_channel_pool: Pool[aio_pika.abc.AbstractChannel],
) -> AsyncGenerator[aio_pika.abc.AbstractChannel, None]:
    async with rq_channel_pool.acquire() as channel:
        yield channel