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
from openapi_client.models.apps_image_info import AppsImageInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestAppsImageInfo(unittest.TestCase):
    """AppsImageInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AppsImageInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.apps_image_info.AppsImageInfo()  # noqa: E501
        if include_optional :
            return AppsImageInfo(
                hub_password = '0', 
                hub_url = '0', 
                hub_user = '0', 
                is_trust = True, 
                namespace = '0'
            )
        else :
            return AppsImageInfo(
                hub_password = '0',
                hub_url = '0',
                hub_user = '0',
                is_trust = True,
                namespace = '0',
        )

    def testAppsImageInfo(self):
        """Test AppsImageInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
