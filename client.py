# -*- coding: utf-8 -*-
# Copyright 2021 Tampere University and VTT Technical Research Centre of Finland
# This software was developed as a part of the ProCemPlus project: https://www.senecc.fi/projects/procemplus
# This source code is licensed under the MIT license. See LICENSE in the repository root directory.
# Author(s): Ville Heikkilä <ville.heikkila@tuni.fi>

"""This module contains code example to instantiate RabbitmqClient object."""

from clients import RabbitmqClient


def get_client(host: str, port: int) -> RabbitmqClient:
    """Returns a RabbitmqClient instance."""
    # Replace the parameters with proper values for host, port, login and password
    # Change the value of exchange if needed.
    #
    # For any parameter that is not given here, the client tries to use a value from an environment variable
    # and most of the parameters also have a default value that is used if neither the constructor parameter
    # nor the environmental variable exist.
    # See tools/clients.py for details about the environmental variables and the default values.
    return RabbitmqClient(
        host=host,
        port=port,
        login="",
        password="",
        exchange="procem.test.exchange",
        ssl=False,
        ssl_version="PROTOCOL_TLS",
        exchange_autodelete=False,
        exchange_durable=False
    )
