# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mpijob
from mpijob.models.v1_delete_options import V1DeleteOptions  # noqa: E501
from mpijob.rest import ApiException

class TestV1DeleteOptions(unittest.TestCase):
    """V1DeleteOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1DeleteOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mpijob.models.v1_delete_options.V1DeleteOptions()  # noqa: E501
        if include_optional :
            return V1DeleteOptions(
                api_version = '', 
                dry_run = [
                    ''
                    ], 
                grace_period_seconds = 56, 
                kind = '', 
                orphan_dependents = True, 
                preconditions = mpijob.models.v1/preconditions.v1.Preconditions(
                    resource_version = '', 
                    uid = '', ), 
                propagation_policy = ''
            )
        else :
            return V1DeleteOptions(
        )

    def testV1DeleteOptions(self):
        """Test V1DeleteOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()