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


class Phishtank(object):
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
        'url': 'str',
        'online': 'str',
        'target': 'str',
        'details': 'list[PhishtankDetails]',
        'phish_id': 'str',
        'verified': 'str',
        'submission_time': 'str',
        'phish_detail_url': 'str',
        'verification_time': 'str'
    }

    attribute_map = {
        'url': 'url',
        'online': 'online',
        'target': 'target',
        'details': 'details',
        'phish_id': 'phish_id',
        'verified': 'verified',
        'submission_time': 'submission_time',
        'phish_detail_url': 'phish_detail_url',
        'verification_time': 'verification_time'
    }

    def __init__(self, url=None, online=None, target=None, details=None, phish_id=None, verified=None, submission_time=None, phish_detail_url=None, verification_time=None, local_vars_configuration=None):  # noqa: E501
        """Phishtank - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._online = None
        self._target = None
        self._details = None
        self._phish_id = None
        self._verified = None
        self._submission_time = None
        self._phish_detail_url = None
        self._verification_time = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if online is not None:
            self.online = online
        if target is not None:
            self.target = target
        if details is not None:
            self.details = details
        if phish_id is not None:
            self.phish_id = phish_id
        if verified is not None:
            self.verified = verified
        if submission_time is not None:
            self.submission_time = submission_time
        if phish_detail_url is not None:
            self.phish_detail_url = phish_detail_url
        if verification_time is not None:
            self.verification_time = verification_time

    @property
    def url(self):
        """Gets the url of this Phishtank.  # noqa: E501


        :return: The url of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Phishtank.


        :param url: The url of this Phishtank.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def online(self):
        """Gets the online of this Phishtank.  # noqa: E501


        :return: The online of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this Phishtank.


        :param online: The online of this Phishtank.  # noqa: E501
        :type: str
        """

        self._online = online

    @property
    def target(self):
        """Gets the target of this Phishtank.  # noqa: E501


        :return: The target of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Phishtank.


        :param target: The target of this Phishtank.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def details(self):
        """Gets the details of this Phishtank.  # noqa: E501


        :return: The details of this Phishtank.  # noqa: E501
        :rtype: list[PhishtankDetails]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Phishtank.


        :param details: The details of this Phishtank.  # noqa: E501
        :type: list[PhishtankDetails]
        """

        self._details = details

    @property
    def phish_id(self):
        """Gets the phish_id of this Phishtank.  # noqa: E501


        :return: The phish_id of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._phish_id

    @phish_id.setter
    def phish_id(self, phish_id):
        """Sets the phish_id of this Phishtank.


        :param phish_id: The phish_id of this Phishtank.  # noqa: E501
        :type: str
        """

        self._phish_id = phish_id

    @property
    def verified(self):
        """Gets the verified of this Phishtank.  # noqa: E501


        :return: The verified of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this Phishtank.


        :param verified: The verified of this Phishtank.  # noqa: E501
        :type: str
        """

        self._verified = verified

    @property
    def submission_time(self):
        """Gets the submission_time of this Phishtank.  # noqa: E501


        :return: The submission_time of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        """Sets the submission_time of this Phishtank.


        :param submission_time: The submission_time of this Phishtank.  # noqa: E501
        :type: str
        """

        self._submission_time = submission_time

    @property
    def phish_detail_url(self):
        """Gets the phish_detail_url of this Phishtank.  # noqa: E501


        :return: The phish_detail_url of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._phish_detail_url

    @phish_detail_url.setter
    def phish_detail_url(self, phish_detail_url):
        """Sets the phish_detail_url of this Phishtank.


        :param phish_detail_url: The phish_detail_url of this Phishtank.  # noqa: E501
        :type: str
        """

        self._phish_detail_url = phish_detail_url

    @property
    def verification_time(self):
        """Gets the verification_time of this Phishtank.  # noqa: E501


        :return: The verification_time of this Phishtank.  # noqa: E501
        :rtype: str
        """
        return self._verification_time

    @verification_time.setter
    def verification_time(self, verification_time):
        """Sets the verification_time of this Phishtank.


        :param verification_time: The verification_time of this Phishtank.  # noqa: E501
        :type: str
        """

        self._verification_time = verification_time

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
        if not isinstance(other, Phishtank):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Phishtank):
            return True

        return self.to_dict() != other.to_dict()