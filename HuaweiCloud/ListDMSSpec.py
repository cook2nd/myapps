# coding: utf-8

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkkafka.v2.region.kafka_region import KafkaRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkkafka.v2 import *

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    # ak = __import__('os').getenv("CLOUD_SDK_AK")
    # sk = __import__('os').getenv("CLOUD_SDK_SK")
    ak = "VEUNRVRJOHSKIPSETEZK"
    sk = "mph6ZnSeRxAfj477QOBQs8BrqnkdV8e7zwdksaR8"
    projectId = "0a5fff52d000257a2fd0c0090f6e9f4c"

    credentials = BasicCredentials(ak, sk, projectId) \

    client = KafkaClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(KafkaRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = CreateInstanceByEngineRequest()
        request.engine = "kafka"
        listAvailableZonesbody = [
            
        ]
        request.body = CreateInstanceByEngineReq(
            available_zones=listAvailableZonesbody,
            subnet_id="7ea0932a-fff0-496a-aa3f-4577b31aeff5",
            security_group_id="2e53c2ce-6208-4a01-8dee-23b1b2965202",
            vpc_id="17ee7aa2-30d4-4885-b0e1-d14e2dd5026b",
            storage_space=1000,
            broker_num=0,
            engine_version="2.7",
            engine="kafka",
            name="dms-test-05"
        )
        response = client.create_instance_by_engine(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)