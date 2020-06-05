# coding: utf-8

"""
    Intel API v3 - Simplified Intel API

    FireEye Intel API - Simplified Intelligence  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@fireeye.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fireeye.intel.configuration import Configuration


class FileSpecificPropertiesHashes(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'sha_256': 'str',
        'sha_1': 'str',
        'md5': 'str'
    }

    attribute_map = {
        'sha_256': 'SHA-256',
        'sha_1': 'SHA-1',
        'md5': 'MD5'
    }

    def __init__(self, sha_256=None, sha_1=None, md5=None, local_vars_configuration=None):  # noqa: E501
        """FileSpecificPropertiesHashes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sha_256 = None
        self._sha_1 = None
        self._md5 = None
        self.discriminator = None

        if sha_256 is not None:
            self.sha_256 = sha_256
        if sha_1 is not None:
            self.sha_1 = sha_1
        if md5 is not None:
            self.md5 = md5

    @property
    def sha_256(self):
        """Gets the sha_256 of this FileSpecificPropertiesHashes.  # noqa: E501


        :return: The sha_256 of this FileSpecificPropertiesHashes.  # noqa: E501
        :rtype: str
        """
        return self._sha_256

    @sha_256.setter
    def sha_256(self, sha_256):
        """Sets the sha_256 of this FileSpecificPropertiesHashes.


        :param sha_256: The sha_256 of this FileSpecificPropertiesHashes.  # noqa: E501
        :type: str
        """

        self._sha_256 = sha_256

    @property
    def sha_1(self):
        """Gets the sha_1 of this FileSpecificPropertiesHashes.  # noqa: E501


        :return: The sha_1 of this FileSpecificPropertiesHashes.  # noqa: E501
        :rtype: str
        """
        return self._sha_1

    @sha_1.setter
    def sha_1(self, sha_1):
        """Sets the sha_1 of this FileSpecificPropertiesHashes.


        :param sha_1: The sha_1 of this FileSpecificPropertiesHashes.  # noqa: E501
        :type: str
        """

        self._sha_1 = sha_1

    @property
    def md5(self):
        """Gets the md5 of this FileSpecificPropertiesHashes.  # noqa: E501


        :return: The md5 of this FileSpecificPropertiesHashes.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this FileSpecificPropertiesHashes.


        :param md5: The md5 of this FileSpecificPropertiesHashes.  # noqa: E501
        :type: str
        """

        self._md5 = md5

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FileSpecificPropertiesHashes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileSpecificPropertiesHashes):
            return True

        return self.to_dict() != other.to_dict()