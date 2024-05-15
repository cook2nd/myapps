# coding: utf-8
import json
import re
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkvpc.v2.region.vpc_region import VpcRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkvpc.v2 import *

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    # ak = __import__('os').getenv("CLOUD_SDK_AK")
    # sk = __import__('os').getenv("CLOUD_SDK_SK")
    ak = 'RKF6SNZMEAGEZCFGQ5HD'
    sk = 'keutBUXLAksv3TrudUHArOU2sQS4YWnqI6kNpZ6J'

    credentials = BasicCredentials(ak, sk) \

    client = VpcClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(VpcRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = ListVpcsRequest()
        response = client.list_vpcs(request)
        # print(response)
        print("#############")
        # print(type(response))
        jj = {}
        # print(jj)
        # print(type(jj))
        jj = json.loads(str(response))
        # print(jj)
        # print(type(jj))
        for vpc in jj.get('vpcs'):
            if re.search(r'.*-dp-.*', vpc.get('name')):
                route = vpc.get('routes')
                # print(type(route))
                print(route[0].get('nexthop'))
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)