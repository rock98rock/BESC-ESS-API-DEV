import sys
sys.path.append('..')
from services import besc_host
from api import api
from model.keypair import KeyPair
import urllib3
import asyncio

kp = KeyPair("Test", "abc123")
host_client = besc_host.besc_ess_host.createDefault(besc_host.besc_ess_host)


async def getdata():
    try:
        response = await api.getLastData(host_client, kp)
        return print(response)

    except Exception as err:
        return print(err)


loop = asyncio.get_event_loop()
loop.run_until_complete(getdata())
loop.close()



