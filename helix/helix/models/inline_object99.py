# coding: utf-8

"""
    Helix API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from helix.configuration import Configuration


class InlineObject99(object):
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
        'name': 'str',
        'is_public': 'bool',
        'sort_by': 'list[str]',
        'page_name': 'str',
        'customer_id': 'str',
        'columns': 'list[str]',
        'is_default': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_public': 'isPublic',
        'sort_by': 'sortBy',
        'page_name': 'pageName',
        'customer_id': 'customer_id',
        'columns': 'columns',
        'is_default': 'isDefault'
    }

    def __init__(self, name=None, is_public=None, sort_by=None, page_name=None, customer_id=None, columns=None, is_default=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject99 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._is_public = None
        self._sort_by = None
        self._page_name = None
        self._customer_id = None
        self._columns = None
        self._is_default = None
        self.discriminator = None

        self.name = name
        if is_public is not None:
            self.is_public = is_public
        if sort_by is not None:
            self.sort_by = sort_by
        self.page_name = page_name
        if customer_id is not None:
            self.customer_id = customer_id
        if columns is not None:
            self.columns = columns
        if is_default is not None:
            self.is_default = is_default

    @property
    def name(self):
        """Gets the name of this InlineObject99.  # noqa: E501

          # noqa: E501

        :return: The name of this InlineObject99.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineObject99.

          # noqa: E501

        :param name: The name of this InlineObject99.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_public(self):
        """Gets the is_public of this InlineObject99.  # noqa: E501

          # noqa: E501

        :return: The is_public of this InlineObject99.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this InlineObject99.

          # noqa: E501

        :param is_public: The is_public of this InlineObject99.  # noqa: E501
        :type: bool
        """

        self._is_public = is_public

    @property
    def sort_by(self):
        """Gets the sort_by of this InlineObject99.  # noqa: E501

          # noqa: E501

        :return: The sort_by of this InlineObject99.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this InlineObject99.

          # noqa: E501

        :param sort_by: The sort_by of this InlineObject99.  # noqa: E501
        :type: list[str]
        """

        self._sort_by = sort_by

    @property
    def page_name(self):
        """Gets the page_name of this InlineObject99.  # noqa: E501

          # noqa: E501

        :return: The page_name of this InlineObject99.  # noqa: E501
        :rtype: str
        """
        return self._page_name

    @page_name.setter
    def page_name(self, page_name):
        """Sets the page_name of this InlineObject99.

          # noqa: E501

        :param page_name: The page_name of this InlineObject99.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and page_name is None:  # noqa: E501
            raise ValueError("Invalid value for `page_name`, must not be `None`")  # noqa: E501

        self._page_name = page_name

    @property
    def customer_id(self):
        """Gets the customer_id of this InlineObject99.  # noqa: E501

          # noqa: E501

        :return: The customer_id of this InlineObject99.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this InlineObject99.

          # noqa: E501

        :param customer_id: The customer_id of this InlineObject99.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def columns(self):
        """Gets the columns of this InlineObject99.  # noqa: E501

          # noqa: E501

        :return: The columns of this InlineObject99.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this InlineObject99.

          # noqa: E501

        :param columns: The columns of this InlineObject99.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

    @property
    def is_default(self):
        """Gets the is_default of this InlineObject99.  # noqa: E501

          # noqa: E501

        :return: The is_default of this InlineObject99.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this InlineObject99.

          # noqa: E501

        :param is_default: The is_default of this InlineObject99.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

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
        if not isinstance(other, InlineObject99):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject99):
            return True

        return self.to_dict() != other.to_dict()