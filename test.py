# -*- coding: utf-8 -*-
# Copyright 2021 Tampere University and VTT Technical Research Centre of Finland
# This software was developed as a part of the ProCemPlus project: https://www.senecc.fi/projects/procemplus
# This source code is licensed under the MIT license. See LICENSE in the repository root directory.
# Author(s): Ville Heikkilä <ville.heikkila@tuni.fi>

"""Code for testing external access to the RabbitMQ message bus."""

import asyncio
import os
from client_receive import start_receiver
from client_send import start_sender
from tools import FullLogger

LOGGER = FullLogger(__name__)


async def start_test(host: str, port: int):
    """start_test"""
    LOGGER.info("Starting the message receiver")
    receiver_task = asyncio.create_task(start_receiver(host, port))

    LOGGER.info("Waiting 2 seconds to allow the receiver process to initialize")
    await asyncio.sleep(2)

    LOGGER.info("Starting the message sender")
    sender_task = asyncio.create_task(start_sender(host, port))

    LOGGER.info("Waiting for the sender and receiver to finish")
    await sender_task
    await receiver_task
    LOGGER.info("Closing the test process")


if __name__ == '__main__':
    host = os.getenv("RABBITMQ_HOST", "localhost")
    port = int(os.getenv("RABBITMQ_PORT", "5672"))
    asyncio.run(start_test(host, port))
