# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: huangrh@goodrain.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.v1_store_app_version_templete_app_probe import V1StoreAppVersionTempleteAppProbe  # noqa: E501
from openapi_client.rest import ApiException

class TestV1StoreAppVersionTempleteAppProbe(unittest.TestCase):
    """V1StoreAppVersionTempleteAppProbe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1StoreAppVersionTempleteAppProbe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1_store_app_version_templete_app_probe.V1StoreAppVersionTempleteAppProbe()  # noqa: E501
        if include_optional :
            return V1StoreAppVersionTempleteAppProbe(
                id = 56, 
                cmd = '0', 
                failure_threshold = 56, 
                http_header = '0', 
                initial_delay_second = 56, 
                is_used = True, 
                mode = '0', 
                path = '0', 
                period_second = 56, 
                port = 56, 
                probe_id = '0', 
                scheme = '0', 
                service_id = '0', 
                success_threshold = 56, 
                timeout_second = 56
            )
        else :
            return V1StoreAppVersionTempleteAppProbe(
                id = 56,
                cmd = '0',
                failure_threshold = 56,
                http_header = '0',
                initial_delay_second = 56,
                is_used = True,
                mode = '0',
                path = '0',
                period_second = 56,
                port = 56,
                probe_id = '0',
                scheme = '0',
                service_id = '0',
                success_threshold = 56,
                timeout_second = 56,
        )

    def testV1StoreAppVersionTempleteAppProbe(self):
        """Test V1StoreAppVersionTempleteAppProbe"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
