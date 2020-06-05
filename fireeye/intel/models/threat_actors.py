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


class ThreatActors(object):
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
        'labels': 'list[str]',
        'name': 'str',
        'description': 'str',
        'aliases': 'list[Aliases]',
        'created': 'str',
        'modified': 'str'
    }

    attribute_map = {
        'labels': 'labels',
        'name': 'name',
        'description': 'description',
        'aliases': 'aliases',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, labels=None, name=None, description=None, aliases=None, created=None, modified=None, local_vars_configuration=None):  # noqa: E501
        """ThreatActors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._labels = None
        self._name = None
        self._description = None
        self._aliases = None
        self._created = None
        self._modified = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        self.name = name
        if description is not None:
            self.description = description
        if aliases is not None:
            self.aliases = aliases
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def labels(self):
        """Gets the labels of this ThreatActors.  # noqa: E501


        :return: The labels of this ThreatActors.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ThreatActors.


        :param labels: The labels of this ThreatActors.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this ThreatActors.  # noqa: E501


        :return: The name of this ThreatActors.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThreatActors.


        :param name: The name of this ThreatActors.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ThreatActors.  # noqa: E501


        :return: The description of this ThreatActors.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ThreatActors.


        :param description: The description of this ThreatActors.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def aliases(self):
        """Gets the aliases of this ThreatActors.  # noqa: E501


        :return: The aliases of this ThreatActors.  # noqa: E501
        :rtype: list[Aliases]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this ThreatActors.


        :param aliases: The aliases of this ThreatActors.  # noqa: E501
        :type: list[Aliases]
        """

        self._aliases = aliases

    @property
    def created(self):
        """Gets the created of this ThreatActors.  # noqa: E501


        :return: The created of this ThreatActors.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ThreatActors.


        :param created: The created of this ThreatActors.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ThreatActors.  # noqa: E501


        :return: The modified of this ThreatActors.  # noqa: E501
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ThreatActors.


        :param modified: The modified of this ThreatActors.  # noqa: E501
        :type: str
        """

        self._modified = modified

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
        if not isinstance(other, ThreatActors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThreatActors):
            return True

        return self.to_dict() != other.to_dict()