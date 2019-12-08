# -*- coding: utf-8 -*-

import logging

from .api import AudibleAPI
from .markets import AudibleMarket
from .auth import (
    AccessTokenAuth,
    SignAuth,
    FileAuthHandler,
    LoginAuthHandler,
    AuthManager
)
from ._logging import LogHelper
from ._version import *


logger = logging.getLogger(__name__)

# the next two steps are necessary to reset logger on Pythonista
# or interactive console
logger.setLevel(logging.NOTSET)
logger.handlers = []

logger.addHandler(logging.NullHandler())

