import sys
sys.path.append('..')
from services.besc_host import besc_ess_host
from api import api
from model.keypair import KeyPair
from model import project_data
import urllib3
import asyncio

keypair = KeyPair("Testing", "abc123")

queryOptions = project_data.options

host_client = besc_ess_host.createDefault(besc_ess_host)

print(queryOptions)


async def getprojdata():
    try:
        response = await api.getProjectData(host_client, keypair, queryOptions)
        print(response)

    except Exception as err:
        print(err)


loop = asyncio.get_event_loop()
loop.run_until_complete(getprojdata())
loop.close()

