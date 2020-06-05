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


class ReportSpecificPropertiesMetadata(object):
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
        'risk_rating': 'list[str]',
        'motivation': 'list[str]',
        'report_type': 'list[str]',
        'affected_industries': 'list[str]',
        'ttp': 'list[str]',
        'intended_effect': 'list[str]',
        'targeted_information': 'list[str]'
    }

    attribute_map = {
        'risk_rating': 'risk_rating',
        'motivation': 'motivation',
        'report_type': 'report_type',
        'affected_industries': 'affected_industries',
        'ttp': 'ttp',
        'intended_effect': 'intended_effect',
        'targeted_information': 'targeted_information'
    }

    def __init__(self, risk_rating=None, motivation=None, report_type=None, affected_industries=None, ttp=None, intended_effect=None, targeted_information=None, local_vars_configuration=None):  # noqa: E501
        """ReportSpecificPropertiesMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._risk_rating = None
        self._motivation = None
        self._report_type = None
        self._affected_industries = None
        self._ttp = None
        self._intended_effect = None
        self._targeted_information = None
        self.discriminator = None

        if risk_rating is not None:
            self.risk_rating = risk_rating
        if motivation is not None:
            self.motivation = motivation
        if report_type is not None:
            self.report_type = report_type
        if affected_industries is not None:
            self.affected_industries = affected_industries
        if ttp is not None:
            self.ttp = ttp
        if intended_effect is not None:
            self.intended_effect = intended_effect
        if targeted_information is not None:
            self.targeted_information = targeted_information

    @property
    def risk_rating(self):
        """Gets the risk_rating of this ReportSpecificPropertiesMetadata.  # noqa: E501


        :return: The risk_rating of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        """Sets the risk_rating of this ReportSpecificPropertiesMetadata.


        :param risk_rating: The risk_rating of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._risk_rating = risk_rating

    @property
    def motivation(self):
        """Gets the motivation of this ReportSpecificPropertiesMetadata.  # noqa: E501


        :return: The motivation of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._motivation

    @motivation.setter
    def motivation(self, motivation):
        """Sets the motivation of this ReportSpecificPropertiesMetadata.


        :param motivation: The motivation of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._motivation = motivation

    @property
    def report_type(self):
        """Gets the report_type of this ReportSpecificPropertiesMetadata.  # noqa: E501


        :return: The report_type of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ReportSpecificPropertiesMetadata.


        :param report_type: The report_type of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._report_type = report_type

    @property
    def affected_industries(self):
        """Gets the affected_industries of this ReportSpecificPropertiesMetadata.  # noqa: E501


        :return: The affected_industries of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._affected_industries

    @affected_industries.setter
    def affected_industries(self, affected_industries):
        """Sets the affected_industries of this ReportSpecificPropertiesMetadata.


        :param affected_industries: The affected_industries of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._affected_industries = affected_industries

    @property
    def ttp(self):
        """Gets the ttp of this ReportSpecificPropertiesMetadata.  # noqa: E501


        :return: The ttp of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._ttp

    @ttp.setter
    def ttp(self, ttp):
        """Sets the ttp of this ReportSpecificPropertiesMetadata.


        :param ttp: The ttp of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._ttp = ttp

    @property
    def intended_effect(self):
        """Gets the intended_effect of this ReportSpecificPropertiesMetadata.  # noqa: E501


        :return: The intended_effect of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._intended_effect

    @intended_effect.setter
    def intended_effect(self, intended_effect):
        """Sets the intended_effect of this ReportSpecificPropertiesMetadata.


        :param intended_effect: The intended_effect of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._intended_effect = intended_effect

    @property
    def targeted_information(self):
        """Gets the targeted_information of this ReportSpecificPropertiesMetadata.  # noqa: E501


        :return: The targeted_information of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._targeted_information

    @targeted_information.setter
    def targeted_information(self, targeted_information):
        """Sets the targeted_information of this ReportSpecificPropertiesMetadata.


        :param targeted_information: The targeted_information of this ReportSpecificPropertiesMetadata.  # noqa: E501
        :type: list[str]
        """

        self._targeted_information = targeted_information

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
        if not isinstance(other, ReportSpecificPropertiesMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportSpecificPropertiesMetadata):
            return True

        return self.to_dict() != other.to_dict()