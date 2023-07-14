import os
import platform

ENV = ''
DC_URL = ''
ARC_URL = ''


platform = platform.system()
if platform == "Windows":
    DC_URL = "https://dc-int.drivecaminc.xyz/"
    ARC_URL = "https://lytx-reviewcenter-ui-dev.aws.drivecaminc.xyz/"
    ENV = 'int'

else:
    DC_URL = os.getenv("DcUrl")
    ARC_URL = os.getenv("ArcURL")
    ENV = os.getenv('environmentName')
