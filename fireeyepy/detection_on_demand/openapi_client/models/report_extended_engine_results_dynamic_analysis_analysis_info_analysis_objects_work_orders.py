# coding: utf-8

"""
    Detection On Demand

    FireEye offers a best-in-class virtual execution engine in many of its core products, including our Network Security, Email Security, and File Analysis solutions. Now our customers can interact with and consume those capabilities directly via a scalable and performant web service. Use the new RESTful API to submit files for malware analysis, search hash values for past analysis results, get full reports for your file submissions, and integrate into your existing toolsets and workflows.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: developers@fireeye.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders(object):
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
        'signature': 'str',
        'os_changes': 'ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrdersOsChanges',
        'total_weight': 'int',
        'anomaly_types': 'int',
        'network_anomaly': 'ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrdersNetworkAnomaly'
    }

    attribute_map = {
        'signature': 'signature',
        'os_changes': 'os_changes',
        'total_weight': 'total_weight',
        'anomaly_types': 'anomaly_types',
        'network_anomaly': 'network_anomaly'
    }

    def __init__(self, signature=None, os_changes=None, total_weight=None, anomaly_types=None, network_anomaly=None, local_vars_configuration=None):  # noqa: E501
        """ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signature = None
        self._os_changes = None
        self._total_weight = None
        self._anomaly_types = None
        self._network_anomaly = None
        self.discriminator = None

        if signature is not None:
            self.signature = signature
        if os_changes is not None:
            self.os_changes = os_changes
        if total_weight is not None:
            self.total_weight = total_weight
        if anomaly_types is not None:
            self.anomaly_types = anomaly_types
        if network_anomaly is not None:
            self.network_anomaly = network_anomaly

    @property
    def signature(self):
        """Gets the signature of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501


        :return: The signature of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.


        :param signature: The signature of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def os_changes(self):
        """Gets the os_changes of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501


        :return: The os_changes of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :rtype: ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrdersOsChanges
        """
        return self._os_changes

    @os_changes.setter
    def os_changes(self, os_changes):
        """Sets the os_changes of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.


        :param os_changes: The os_changes of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :type: ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrdersOsChanges
        """

        self._os_changes = os_changes

    @property
    def total_weight(self):
        """Gets the total_weight of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501

        Total weight of multiple jobs.  # noqa: E501

        :return: The total_weight of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :rtype: int
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """Sets the total_weight of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.

        Total weight of multiple jobs.  # noqa: E501

        :param total_weight: The total_weight of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :type: int
        """

        self._total_weight = total_weight

    @property
    def anomaly_types(self):
        """Gets the anomaly_types of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501


        :return: The anomaly_types of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :rtype: int
        """
        return self._anomaly_types

    @anomaly_types.setter
    def anomaly_types(self, anomaly_types):
        """Sets the anomaly_types of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.


        :param anomaly_types: The anomaly_types of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :type: int
        """

        self._anomaly_types = anomaly_types

    @property
    def network_anomaly(self):
        """Gets the network_anomaly of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501


        :return: The network_anomaly of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :rtype: ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrdersNetworkAnomaly
        """
        return self._network_anomaly

    @network_anomaly.setter
    def network_anomaly(self, network_anomaly):
        """Sets the network_anomaly of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.


        :param network_anomaly: The network_anomaly of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders.  # noqa: E501
        :type: ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrdersNetworkAnomaly
        """

        self._network_anomaly = network_anomaly

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
        if not isinstance(other, ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoAnalysisObjectsWorkOrders):
            return True

        return self.to_dict() != other.to_dict()
