# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: huangrh@goodrain.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1StoreAppVersionTempletePluginConfigGroupOption(object):
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
        'id': 'int',
        'attr_alt_value': 'str',
        'attr_default_value': 'str',
        'attr_info': 'str',
        'attr_name': 'str',
        'attr_type': 'str',
        'build_version': 'str',
        'is_change': 'bool',
        'plugin_id': 'str',
        'protocol': 'str',
        'service_meta_type': 'str'
    }

    attribute_map = {
        'id': 'ID',
        'attr_alt_value': 'attr_alt_value',
        'attr_default_value': 'attr_default_value',
        'attr_info': 'attr_info',
        'attr_name': 'attr_name',
        'attr_type': 'attr_type',
        'build_version': 'build_version',
        'is_change': 'is_change',
        'plugin_id': 'plugin_id',
        'protocol': 'protocol',
        'service_meta_type': 'service_meta_type'
    }

    def __init__(self, id=None, attr_alt_value=None, attr_default_value=None, attr_info=None, attr_name=None, attr_type=None, build_version=None, is_change=None, plugin_id=None, protocol=None, service_meta_type=None, local_vars_configuration=None):  # noqa: E501
        """V1StoreAppVersionTempletePluginConfigGroupOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._attr_alt_value = None
        self._attr_default_value = None
        self._attr_info = None
        self._attr_name = None
        self._attr_type = None
        self._build_version = None
        self._is_change = None
        self._plugin_id = None
        self._protocol = None
        self._service_meta_type = None
        self.discriminator = None

        self.id = id
        self.attr_alt_value = attr_alt_value
        self.attr_default_value = attr_default_value
        self.attr_info = attr_info
        self.attr_name = attr_name
        self.attr_type = attr_type
        self.build_version = build_version
        self.is_change = is_change
        self.plugin_id = plugin_id
        self.protocol = protocol
        self.service_meta_type = service_meta_type

    @property
    def id(self):
        """Gets the id of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The id of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param id: The id of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def attr_alt_value(self):
        """Gets the attr_alt_value of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The attr_alt_value of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._attr_alt_value

    @attr_alt_value.setter
    def attr_alt_value(self, attr_alt_value):
        """Sets the attr_alt_value of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param attr_alt_value: The attr_alt_value of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attr_alt_value is None:  # noqa: E501
            raise ValueError("Invalid value for `attr_alt_value`, must not be `None`")  # noqa: E501

        self._attr_alt_value = attr_alt_value

    @property
    def attr_default_value(self):
        """Gets the attr_default_value of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The attr_default_value of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._attr_default_value

    @attr_default_value.setter
    def attr_default_value(self, attr_default_value):
        """Sets the attr_default_value of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param attr_default_value: The attr_default_value of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attr_default_value is None:  # noqa: E501
            raise ValueError("Invalid value for `attr_default_value`, must not be `None`")  # noqa: E501

        self._attr_default_value = attr_default_value

    @property
    def attr_info(self):
        """Gets the attr_info of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The attr_info of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._attr_info

    @attr_info.setter
    def attr_info(self, attr_info):
        """Sets the attr_info of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param attr_info: The attr_info of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attr_info is None:  # noqa: E501
            raise ValueError("Invalid value for `attr_info`, must not be `None`")  # noqa: E501

        self._attr_info = attr_info

    @property
    def attr_name(self):
        """Gets the attr_name of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The attr_name of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._attr_name

    @attr_name.setter
    def attr_name(self, attr_name):
        """Sets the attr_name of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param attr_name: The attr_name of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attr_name is None:  # noqa: E501
            raise ValueError("Invalid value for `attr_name`, must not be `None`")  # noqa: E501

        self._attr_name = attr_name

    @property
    def attr_type(self):
        """Gets the attr_type of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The attr_type of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._attr_type

    @attr_type.setter
    def attr_type(self, attr_type):
        """Sets the attr_type of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param attr_type: The attr_type of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and attr_type is None:  # noqa: E501
            raise ValueError("Invalid value for `attr_type`, must not be `None`")  # noqa: E501

        self._attr_type = attr_type

    @property
    def build_version(self):
        """Gets the build_version of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The build_version of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param build_version: The build_version of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and build_version is None:  # noqa: E501
            raise ValueError("Invalid value for `build_version`, must not be `None`")  # noqa: E501

        self._build_version = build_version

    @property
    def is_change(self):
        """Gets the is_change of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The is_change of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: bool
        """
        return self._is_change

    @is_change.setter
    def is_change(self, is_change):
        """Sets the is_change of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param is_change: The is_change of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_change is None:  # noqa: E501
            raise ValueError("Invalid value for `is_change`, must not be `None`")  # noqa: E501

        self._is_change = is_change

    @property
    def plugin_id(self):
        """Gets the plugin_id of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The plugin_id of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, plugin_id):
        """Sets the plugin_id of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param plugin_id: The plugin_id of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_id`, must not be `None`")  # noqa: E501

        self._plugin_id = plugin_id

    @property
    def protocol(self):
        """Gets the protocol of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The protocol of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param protocol: The protocol of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def service_meta_type(self):
        """Gets the service_meta_type of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501


        :return: The service_meta_type of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :rtype: str
        """
        return self._service_meta_type

    @service_meta_type.setter
    def service_meta_type(self, service_meta_type):
        """Sets the service_meta_type of this V1StoreAppVersionTempletePluginConfigGroupOption.


        :param service_meta_type: The service_meta_type of this V1StoreAppVersionTempletePluginConfigGroupOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_meta_type is None:  # noqa: E501
            raise ValueError("Invalid value for `service_meta_type`, must not be `None`")  # noqa: E501

        self._service_meta_type = service_meta_type

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
        if not isinstance(other, V1StoreAppVersionTempletePluginConfigGroupOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1StoreAppVersionTempletePluginConfigGroupOption):
            return True

        return self.to_dict() != other.to_dict()
