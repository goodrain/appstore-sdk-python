# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.v1alpha1_component_extend_method_rule import V1alpha1ComponentExtendMethodRule  # noqa: E501
from openapi_client.rest import ApiException

class TestV1alpha1ComponentExtendMethodRule(unittest.TestCase):
    """V1alpha1ComponentExtendMethodRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ComponentExtendMethodRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.v1alpha1_component_extend_method_rule.V1alpha1ComponentExtendMethodRule()  # noqa: E501
        if include_optional :
            return V1alpha1ComponentExtendMethodRule(
                is_restart = 56, 
                max_memory = 56, 
                max_node = 56, 
                min_memory = 56, 
                min_node = 56, 
                step_memory = 56, 
                step_node = 56
            )
        else :
            return V1alpha1ComponentExtendMethodRule(
                is_restart = 56,
                max_memory = 56,
                max_node = 56,
                min_memory = 56,
                min_node = 56,
                step_memory = 56,
                step_node = 56,
        )

    def testV1alpha1ComponentExtendMethodRule(self):
        """Test V1alpha1ComponentExtendMethodRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
