import sys
sys.path.append('..')
from services.besc_host import besc_ess_host
from api import api
from model.keypair import KeyPair
from model import device, project_data
from utils import dateConvert
import asyncio


keypair = KeyPair("Testing", "abc123")
host_client = besc_ess_host.createDefault(besc_ess_host)
Device = device.Device
ProjectData = project_data.ProjectData

projectData = ProjectData.createWithCurrenTime(ProjectData,
                                               "Testing",
                          [
                              Device("A1", 40),
                              Device("B2", 70)
                          ],
                          119,
                          78,
                          "101.123, 123.122"
                          )



async def sendprojdata():
    try:
        response = await api.sendProjectData(host_client, keypair, projectData)
        print(response)

    except Exception as err:
        print(err)


loop = asyncio.get_event_loop()
loop.run_until_complete(sendprojdata())
loop.close()

