# coding: utf-8

"""
    app-server

    Resource for managing app-server  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class V1alpha1RainbondApplicationConfig(object):
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
        'app_config_groups': 'list[V1alpha1AppConfigGroup]',
        'apps': 'list[V1alpha1Component]',
        'group_key': 'str',
        'group_name': 'str',
        'group_version': 'str',
        'plugins': 'list[V1alpha1Plugin]',
        'template_version': 'str'
    }

    attribute_map = {
        'app_config_groups': 'app_config_groups',
        'apps': 'apps',
        'group_key': 'group_key',
        'group_name': 'group_name',
        'group_version': 'group_version',
        'plugins': 'plugins',
        'template_version': 'template_version'
    }

    def __init__(self, app_config_groups=None, apps=None, group_key=None, group_name=None, group_version=None, plugins=None, template_version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1RainbondApplicationConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_config_groups = None
        self._apps = None
        self._group_key = None
        self._group_name = None
        self._group_version = None
        self._plugins = None
        self._template_version = None
        self.discriminator = None

        self.app_config_groups = app_config_groups
        self.apps = apps
        self.group_key = group_key
        self.group_name = group_name
        self.group_version = group_version
        if plugins is not None:
            self.plugins = plugins
        self.template_version = template_version

    @property
    def app_config_groups(self):
        """Gets the app_config_groups of this V1alpha1RainbondApplicationConfig.  # noqa: E501


        :return: The app_config_groups of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :rtype: list[V1alpha1AppConfigGroup]
        """
        return self._app_config_groups

    @app_config_groups.setter
    def app_config_groups(self, app_config_groups):
        """Sets the app_config_groups of this V1alpha1RainbondApplicationConfig.


        :param app_config_groups: The app_config_groups of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :type: list[V1alpha1AppConfigGroup]
        """
        if self.local_vars_configuration.client_side_validation and app_config_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `app_config_groups`, must not be `None`")  # noqa: E501

        self._app_config_groups = app_config_groups

    @property
    def apps(self):
        """Gets the apps of this V1alpha1RainbondApplicationConfig.  # noqa: E501


        :return: The apps of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :rtype: list[V1alpha1Component]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this V1alpha1RainbondApplicationConfig.


        :param apps: The apps of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :type: list[V1alpha1Component]
        """
        if self.local_vars_configuration.client_side_validation and apps is None:  # noqa: E501
            raise ValueError("Invalid value for `apps`, must not be `None`")  # noqa: E501

        self._apps = apps

    @property
    def group_key(self):
        """Gets the group_key of this V1alpha1RainbondApplicationConfig.  # noqa: E501


        :return: The group_key of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :rtype: str
        """
        return self._group_key

    @group_key.setter
    def group_key(self, group_key):
        """Sets the group_key of this V1alpha1RainbondApplicationConfig.


        :param group_key: The group_key of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_key is None:  # noqa: E501
            raise ValueError("Invalid value for `group_key`, must not be `None`")  # noqa: E501

        self._group_key = group_key

    @property
    def group_name(self):
        """Gets the group_name of this V1alpha1RainbondApplicationConfig.  # noqa: E501


        :return: The group_name of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this V1alpha1RainbondApplicationConfig.


        :param group_name: The group_name of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def group_version(self):
        """Gets the group_version of this V1alpha1RainbondApplicationConfig.  # noqa: E501


        :return: The group_version of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """Sets the group_version of this V1alpha1RainbondApplicationConfig.


        :param group_version: The group_version of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and group_version is None:  # noqa: E501
            raise ValueError("Invalid value for `group_version`, must not be `None`")  # noqa: E501

        self._group_version = group_version

    @property
    def plugins(self):
        """Gets the plugins of this V1alpha1RainbondApplicationConfig.  # noqa: E501


        :return: The plugins of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :rtype: list[V1alpha1Plugin]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this V1alpha1RainbondApplicationConfig.


        :param plugins: The plugins of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :type: list[V1alpha1Plugin]
        """

        self._plugins = plugins

    @property
    def template_version(self):
        """Gets the template_version of this V1alpha1RainbondApplicationConfig.  # noqa: E501


        :return: The template_version of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :rtype: str
        """
        return self._template_version

    @template_version.setter
    def template_version(self, template_version):
        """Sets the template_version of this V1alpha1RainbondApplicationConfig.


        :param template_version: The template_version of this V1alpha1RainbondApplicationConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template_version is None:  # noqa: E501
            raise ValueError("Invalid value for `template_version`, must not be `None`")  # noqa: E501

        self._template_version = template_version

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
        if not isinstance(other, V1alpha1RainbondApplicationConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1RainbondApplicationConfig):
            return True

        return self.to_dict() != other.to_dict()
