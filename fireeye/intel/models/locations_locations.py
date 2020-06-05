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


class LocationsLocations(object):
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
        'source': 'list[Location]',
        'target': 'list[Location]',
        'unknown': 'list[Location]'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target',
        'unknown': 'unknown'
    }

    def __init__(self, source=None, target=None, unknown=None, local_vars_configuration=None):  # noqa: E501
        """LocationsLocations - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._target = None
        self._unknown = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if unknown is not None:
            self.unknown = unknown

    @property
    def source(self):
        """Gets the source of this LocationsLocations.  # noqa: E501


        :return: The source of this LocationsLocations.  # noqa: E501
        :rtype: list[Location]
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this LocationsLocations.


        :param source: The source of this LocationsLocations.  # noqa: E501
        :type: list[Location]
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this LocationsLocations.  # noqa: E501


        :return: The target of this LocationsLocations.  # noqa: E501
        :rtype: list[Location]
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this LocationsLocations.


        :param target: The target of this LocationsLocations.  # noqa: E501
        :type: list[Location]
        """

        self._target = target

    @property
    def unknown(self):
        """Gets the unknown of this LocationsLocations.  # noqa: E501


        :return: The unknown of this LocationsLocations.  # noqa: E501
        :rtype: list[Location]
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """Sets the unknown of this LocationsLocations.


        :param unknown: The unknown of this LocationsLocations.  # noqa: E501
        :type: list[Location]
        """

        self._unknown = unknown

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
        if not isinstance(other, LocationsLocations):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocationsLocations):
            return True

        return self.to_dict() != other.to_dict()