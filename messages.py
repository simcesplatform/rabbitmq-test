# -*- coding: utf-8 -*-
# Copyright 2021 Tampere University and VTT Technical Research Centre of Finland
# This software was developed as a part of the ProCemPlus project: https://www.senecc.fi/projects/procemplus
# This source code is licensed under the MIT license. See LICENSE in the repository root directory.
# Author(s): Ville Heikkilä <ville.heikkila@tuni.fi>
#            Otto Hylli <otto.hylli@tuni.fi>

"""This module contains a class for creating and holding messages for the RabbitMQ message bus."""

# import these for backwards compatibility
from message.abstract import BaseMessage, AbstractMessage      # pylint: disable=unused-import
from message.abstract import AbstractResultMessage, get_json   # pylint: disable=unused-import
from message.block import QuantityBlock                        # pylint: disable=unused-import
from message.block import ValueArrayBlock, QuantityArrayBlock  # pylint: disable=unused-import
from message.block import TimeSeriesBlock                      # pylint: disable=unused-import
from message.epoch import EpochMessage                         # pylint: disable=unused-import
from message.factory import MessageFactory                     # pylint: disable=unused-import
from message.general import GeneralMessage, ResultMessage      # pylint: disable=unused-import
from message.generator import MessageGenerator                 # pylint: disable=unused-import
from message.simulation_state import SimulationStateMessage    # pylint: disable=unused-import
from message.status import StatusMessage                       # pylint: disable=unused-import
from message.utils import get_next_message_id                  # pylint: disable=unused-import

from tools import FullLogger

LOGGER = FullLogger(__name__)
