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


class FindingsTel(object):
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
        'type': 'str',
        'extensions': 'FindingsTelExtensions',
        'id': 'str',
        'statement': 'str'
    }

    attribute_map = {
        'type': 'type',
        'extensions': 'extensions',
        'id': 'id',
        'statement': 'statement'
    }

    def __init__(self, type=None, extensions=None, id=None, statement=None, local_vars_configuration=None):  # noqa: E501
        """FindingsTel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._extensions = None
        self._id = None
        self._statement = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if extensions is not None:
            self.extensions = extensions
        if id is not None:
            self.id = id
        if statement is not None:
            self.statement = statement

    @property
    def type(self):
        """Gets the type of this FindingsTel.  # noqa: E501


        :return: The type of this FindingsTel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FindingsTel.


        :param type: The type of this FindingsTel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def extensions(self):
        """Gets the extensions of this FindingsTel.  # noqa: E501


        :return: The extensions of this FindingsTel.  # noqa: E501
        :rtype: FindingsTelExtensions
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this FindingsTel.


        :param extensions: The extensions of this FindingsTel.  # noqa: E501
        :type: FindingsTelExtensions
        """

        self._extensions = extensions

    @property
    def id(self):
        """Gets the id of this FindingsTel.  # noqa: E501


        :return: The id of this FindingsTel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FindingsTel.


        :param id: The id of this FindingsTel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def statement(self):
        """Gets the statement of this FindingsTel.  # noqa: E501


        :return: The statement of this FindingsTel.  # noqa: E501
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this FindingsTel.


        :param statement: The statement of this FindingsTel.  # noqa: E501
        :type: str
        """

        self._statement = statement

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
        if not isinstance(other, FindingsTel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FindingsTel):
            return True

        return self.to_dict() != other.to_dict()