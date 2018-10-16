# -*- coding: future_fstrings -*-

import asyncio
import ssl
import time
import uuid
from typing import Any, Dict, List, Optional, NewType, TypeVar

import aiohttp
import aiomqtt
import jsonpickle
import jsontofu
import paho
import random
import requests
import types
from aiohttp.client import ClientSession
from aiohttp.client_ws import ClientWebSocketResponse
from aiohttp.http_websocket import WSMessage
from dataclasses import dataclass
from requests.exceptions import HTTPError

UUID4 = NewType('UUID4', str)
TimeZone = NewType('TimeZone', str)
Email = NewType('Email', str)
Json = NewType('Json', str)
Timestamp = NewType('Timestamp', int)
T = TypeVar('T')


@dataclass
class Device:
    id: UUID4


class Rests:
    # TODO
    # throws Response exception if response.status_code > 200
    # allows custom exception serialization, for example:
    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url
        self.headers: Dict[str, str] = {}

    @staticmethod
    def raise_for_status(res: requests.Response) -> None:
        try:
            res.raise_for_status()
        except HTTPError as e:
            raise HTTPError(f"{str(e)}: {e.response.json()}", response=e.response)

    # TODO: payload: Optional[Dict|Json]
    def post(self, url: str, payload: Optional[Any] = None) -> requests.Response:
        """
        :exception HttpError
        """
        if not payload:
            res = requests.post(f"{self.base_url}{url}",
                                 headers=self.headers, data=None)
        elif type(payload) is dict:
            res = requests.post(f"{self.base_url}{url}",
                                 headers=self.headers,
                                 json=payload)
        else:
            res = requests.post(f"{self.base_url}{url}",
                                 headers=self.headers,
                                 data=jsonpickle.encode(payload, unpicklable=False))
        Rests.raise_for_status(res)
        return res

    def get(self, url: str) -> requests.Response:
        """
        :exception HttpError
        """
        res = requests.get(f"{self.base_url}{url}",
                            headers=self.headers)
        Rests.raise_for_status(res)
        return res

    def delete(self, url: str) -> requests.Response:
        """
        :exception HttpError
        """
        res = requests.delete(f"{self.base_url}{url}",
                               headers=self.headers)
        Rests.raise_for_status(res)
        return res


class SimpleMender(Rests):
    def __init__(self, base_url: str = "",
                 client_id: str = "", client_secret: Optional[str] = None) -> None:
        super().__init__(base_url=base_url)
        self.client_id: str = client_id
        self.client_secret: str = client_secret if client_secret else client_id
        self.headers['Content-Type']: str = 'application/json'
        self.token: Optional[OauthToken] = None

class Mender(SimpleMender):
    def login(self, username: Email, password: str) -> OauthToken:
        pass
