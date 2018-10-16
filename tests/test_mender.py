# -*- coding: future_fstrings -*-

import jsonpickle

from mender import Mender

import responses
import requests
import uuid
import os
import json
import pytest
from unittest.mock import MagicMock

from typing import Any, Callable, Dict, List, Optional, Union, NewType, Iterable, TypeVar

@responses.activate
def test_login():
    token: OauthToken = OauthToken(
        access_token="ffffffff",
        token_type="Bearer",
        user_id=UUID4(str(uuid.uuid4())),
        refresh_token="",
        expires_in=0)
    responses.add(responses.POST, 'https://xxx',
                  json=jsonpickle.encode(token, unpicklable=False), status=200)
    #json={
    #    'access_token': str,
    #    'token_type': str,
    #    'user_id': UUID4
    #}, status=200)

    mender: Mender = Mender()
    res: OauthToken = mender.login(username=Email("yongjhih@gmail.com"), password="")
    assert res == token
