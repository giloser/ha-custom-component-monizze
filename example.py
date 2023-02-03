import asyncio
import aiohttp

from custom_components.monizze.api import MonizzeAPI

async def main():
    async with aiohttp.ClientSession() as session:
        api = SodexoAPI(session)

        username = input("Enter your username.......: ")
        password = input("Enter your password.......: ")

        token = await api.login(username, password)
        details = await api.getAccountDetails(token)
        print(details.amount)
        print(details.updated)
        
asyncio.get_event_loop().run_until_complete(main())