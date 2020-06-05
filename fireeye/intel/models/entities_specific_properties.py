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


class EntitiesSpecificProperties(object):
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
        'threat_actor': 'list[str]',
        'malware': 'list[str]',
        'cve': 'list[str]',
        'location': 'list[str]'
    }

    attribute_map = {
        'threat_actor': 'threat-actor',
        'malware': 'malware',
        'cve': 'cve',
        'location': 'location'
    }

    def __init__(self, threat_actor=None, malware=None, cve=None, location=None, local_vars_configuration=None):  # noqa: E501
        """EntitiesSpecificProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._threat_actor = None
        self._malware = None
        self._cve = None
        self._location = None
        self.discriminator = None

        if threat_actor is not None:
            self.threat_actor = threat_actor
        if malware is not None:
            self.malware = malware
        if cve is not None:
            self.cve = cve
        if location is not None:
            self.location = location

    @property
    def threat_actor(self):
        """Gets the threat_actor of this EntitiesSpecificProperties.  # noqa: E501


        :return: The threat_actor of this EntitiesSpecificProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._threat_actor

    @threat_actor.setter
    def threat_actor(self, threat_actor):
        """Sets the threat_actor of this EntitiesSpecificProperties.


        :param threat_actor: The threat_actor of this EntitiesSpecificProperties.  # noqa: E501
        :type: list[str]
        """

        self._threat_actor = threat_actor

    @property
    def malware(self):
        """Gets the malware of this EntitiesSpecificProperties.  # noqa: E501


        :return: The malware of this EntitiesSpecificProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._malware

    @malware.setter
    def malware(self, malware):
        """Sets the malware of this EntitiesSpecificProperties.


        :param malware: The malware of this EntitiesSpecificProperties.  # noqa: E501
        :type: list[str]
        """

        self._malware = malware

    @property
    def cve(self):
        """Gets the cve of this EntitiesSpecificProperties.  # noqa: E501


        :return: The cve of this EntitiesSpecificProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._cve

    @cve.setter
    def cve(self, cve):
        """Sets the cve of this EntitiesSpecificProperties.


        :param cve: The cve of this EntitiesSpecificProperties.  # noqa: E501
        :type: list[str]
        """

        self._cve = cve

    @property
    def location(self):
        """Gets the location of this EntitiesSpecificProperties.  # noqa: E501


        :return: The location of this EntitiesSpecificProperties.  # noqa: E501
        :rtype: list[str]
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EntitiesSpecificProperties.


        :param location: The location of this EntitiesSpecificProperties.  # noqa: E501
        :type: list[str]
        """

        self._location = location

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
        if not isinstance(other, EntitiesSpecificProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EntitiesSpecificProperties):
            return True

        return self.to_dict() != other.to_dict()