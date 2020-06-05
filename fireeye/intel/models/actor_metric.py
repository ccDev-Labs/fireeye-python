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


class ActorMetric(object):
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
        'confidence': 'str',
        'description': 'str',
        'end_date': 'str',
        'value': 'int',
        'metric_type': 'str',
        'start_date': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'confidence': 'confidence',
        'description': 'description',
        'end_date': 'end_date',
        'value': 'value',
        'metric_type': 'metric_type',
        'start_date': 'start_date',
        'unit': 'unit'
    }

    def __init__(self, confidence=None, description=None, end_date=None, value=None, metric_type=None, start_date=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """ActorMetric - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._confidence = None
        self._description = None
        self._end_date = None
        self._value = None
        self._metric_type = None
        self._start_date = None
        self._unit = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if description is not None:
            self.description = description
        if end_date is not None:
            self.end_date = end_date
        if value is not None:
            self.value = value
        if metric_type is not None:
            self.metric_type = metric_type
        if start_date is not None:
            self.start_date = start_date
        if unit is not None:
            self.unit = unit

    @property
    def confidence(self):
        """Gets the confidence of this ActorMetric.  # noqa: E501


        :return: The confidence of this ActorMetric.  # noqa: E501
        :rtype: str
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ActorMetric.


        :param confidence: The confidence of this ActorMetric.  # noqa: E501
        :type: str
        """

        self._confidence = confidence

    @property
    def description(self):
        """Gets the description of this ActorMetric.  # noqa: E501


        :return: The description of this ActorMetric.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ActorMetric.


        :param description: The description of this ActorMetric.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this ActorMetric.  # noqa: E501


        :return: The end_date of this ActorMetric.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ActorMetric.


        :param end_date: The end_date of this ActorMetric.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def value(self):
        """Gets the value of this ActorMetric.  # noqa: E501


        :return: The value of this ActorMetric.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ActorMetric.


        :param value: The value of this ActorMetric.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def metric_type(self):
        """Gets the metric_type of this ActorMetric.  # noqa: E501


        :return: The metric_type of this ActorMetric.  # noqa: E501
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this ActorMetric.


        :param metric_type: The metric_type of this ActorMetric.  # noqa: E501
        :type: str
        """

        self._metric_type = metric_type

    @property
    def start_date(self):
        """Gets the start_date of this ActorMetric.  # noqa: E501


        :return: The start_date of this ActorMetric.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ActorMetric.


        :param start_date: The start_date of this ActorMetric.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def unit(self):
        """Gets the unit of this ActorMetric.  # noqa: E501


        :return: The unit of this ActorMetric.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ActorMetric.


        :param unit: The unit of this ActorMetric.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, ActorMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActorMetric):
            return True

        return self.to_dict() != other.to_dict()