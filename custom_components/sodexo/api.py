"""API to Sodexo."""
import aiohttp
import logging
import json
from bs4 import BeautifulSoup

from .const import LOGIN_URL, MYACCOUNT_URL
from .lib import AccountDetails, parse_html

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class MonizzeAPI:
    """Interfaces to https://my.monizze.be/"""
    
    def __init__(self, websession):
        self.websession = websession
        self.json = None

    async def login(self, username, password):
        """Issue LOGIN request."""
        try:
            _LOGGER.debug("Logging in...")
            async with self.websession.get(
                LOGIN_URL, 
                params = { 'email': username, 'pass': password }
            ) as res:
                if res.status == 200 and res.content_type == "application/javascript":
                    text = await res.text()
                    obj = json.loads(text)
                    if obj['sucess']:
                        cookie = res.headers['set-cookie']
                        return cookie[0:cookie.find(';')]
                    else:
                        raise Exception("Login failed!", obj['mensagem'])
                raise Exception("Could not retrieve token for user, login failed")
        except aiohttp.ClientError as err:
            _LOGGER.exception(err)
    
    async def getAccountDetails(self, token: str) -> AccountDetails:
        """Issue ACCOUNT DETAILS requests."""
        try:
            _LOGGER.debug("Getting account details...")
            async with self.websession.get(
                MYACCOUNT_URL, 
                headers = { 
                    "Cookie": token 
                }
            ) as res:
                if res.status == 200 and res.content_type == "text/html":
                    html = await res.text()
                    data = parse_html(html)
                    amount = float(data[2].strip().replace(",", "."))
                    return AccountDetails(amount, data[4])
                raise Exception("Could not retrieve account information from API")
        except aiohttp.ClientError as err:
            _LOGGER.exception(err)