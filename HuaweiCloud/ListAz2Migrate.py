# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkdds.v3.region.dds_region import DdsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkdds.v3 import *

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    # ak = os.environ["CLOUD_SDK_AK"]
    # sk = os.environ["CLOUD_SDK_SK"]
    ak = "NNFHWFR8ZEO6WVW8305R"
    sk = "onYcaMeGoVYrkQwtNADV1fJIA1Zpk6PWLJFGx103"

    credentials = BasicCredentials(ak, sk)

    client = DdsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(DdsRegion.value_of("cn-north-1")) \
        .build()

    try:
        request = ListAz2MigrateRequest()
        request.instance_id = "cd571954015947d8b346809a5ff22b80in02"
        response = client.list_az2_migrate(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)