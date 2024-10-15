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
from mpijob.models.v1_internal_event import V1InternalEvent  # noqa: E501
from mpijob.rest import ApiException

class TestV1InternalEvent(unittest.TestCase):
    """V1InternalEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1InternalEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mpijob.models.v1_internal_event.V1InternalEvent()  # noqa: E501
        if include_optional :
            return V1InternalEvent(
                object = None, 
                type = ''
            )
        else :
            return V1InternalEvent(
                object = None,
                type = '',
        )

    def testV1InternalEvent(self):
        """Test V1InternalEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()