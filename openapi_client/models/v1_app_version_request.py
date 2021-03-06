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


class V1AppVersionRequest(object):
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
        'app_version': 'str',
        'app_version_alias': 'str',
        'desc': 'str',
        'rainbond_version': 'str',
        'templete': 'str',
        'update_version': 'int'
    }

    attribute_map = {
        'app_version': 'appVersion',
        'app_version_alias': 'appVersionAlias',
        'desc': 'desc',
        'rainbond_version': 'rainbondVersion',
        'templete': 'templete',
        'update_version': 'updateVersion'
    }

    def __init__(self, app_version=None, app_version_alias=None, desc=None, rainbond_version=None, templete=None, update_version=None, local_vars_configuration=None):  # noqa: E501
        """V1AppVersionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_version = None
        self._app_version_alias = None
        self._desc = None
        self._rainbond_version = None
        self._templete = None
        self._update_version = None
        self.discriminator = None

        self.app_version = app_version
        self.app_version_alias = app_version_alias
        self.desc = desc
        self.rainbond_version = rainbond_version
        self.templete = templete
        self.update_version = update_version

    @property
    def app_version(self):
        """Gets the app_version of this V1AppVersionRequest.  # noqa: E501


        :return: The app_version of this V1AppVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this V1AppVersionRequest.


        :param app_version: The app_version of this V1AppVersionRequest.  # noqa: E501
        :type app_version: str
        """
        if self.local_vars_configuration.client_side_validation and app_version is None:  # noqa: E501
            raise ValueError("Invalid value for `app_version`, must not be `None`")  # noqa: E501

        self._app_version = app_version

    @property
    def app_version_alias(self):
        """Gets the app_version_alias of this V1AppVersionRequest.  # noqa: E501


        :return: The app_version_alias of this V1AppVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_version_alias

    @app_version_alias.setter
    def app_version_alias(self, app_version_alias):
        """Sets the app_version_alias of this V1AppVersionRequest.


        :param app_version_alias: The app_version_alias of this V1AppVersionRequest.  # noqa: E501
        :type app_version_alias: str
        """
        if self.local_vars_configuration.client_side_validation and app_version_alias is None:  # noqa: E501
            raise ValueError("Invalid value for `app_version_alias`, must not be `None`")  # noqa: E501

        self._app_version_alias = app_version_alias

    @property
    def desc(self):
        """Gets the desc of this V1AppVersionRequest.  # noqa: E501


        :return: The desc of this V1AppVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this V1AppVersionRequest.


        :param desc: The desc of this V1AppVersionRequest.  # noqa: E501
        :type desc: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def rainbond_version(self):
        """Gets the rainbond_version of this V1AppVersionRequest.  # noqa: E501


        :return: The rainbond_version of this V1AppVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._rainbond_version

    @rainbond_version.setter
    def rainbond_version(self, rainbond_version):
        """Sets the rainbond_version of this V1AppVersionRequest.


        :param rainbond_version: The rainbond_version of this V1AppVersionRequest.  # noqa: E501
        :type rainbond_version: str
        """
        if self.local_vars_configuration.client_side_validation and rainbond_version is None:  # noqa: E501
            raise ValueError("Invalid value for `rainbond_version`, must not be `None`")  # noqa: E501

        self._rainbond_version = rainbond_version

    @property
    def templete(self):
        """Gets the templete of this V1AppVersionRequest.  # noqa: E501


        :return: The templete of this V1AppVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._templete

    @templete.setter
    def templete(self, templete):
        """Sets the templete of this V1AppVersionRequest.


        :param templete: The templete of this V1AppVersionRequest.  # noqa: E501
        :type templete: str
        """
        if self.local_vars_configuration.client_side_validation and templete is None:  # noqa: E501
            raise ValueError("Invalid value for `templete`, must not be `None`")  # noqa: E501

        self._templete = templete

    @property
    def update_version(self):
        """Gets the update_version of this V1AppVersionRequest.  # noqa: E501


        :return: The update_version of this V1AppVersionRequest.  # noqa: E501
        :rtype: int
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this V1AppVersionRequest.


        :param update_version: The update_version of this V1AppVersionRequest.  # noqa: E501
        :type update_version: int
        """
        if self.local_vars_configuration.client_side_validation and update_version is None:  # noqa: E501
            raise ValueError("Invalid value for `update_version`, must not be `None`")  # noqa: E501

        self._update_version = update_version

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
        if not isinstance(other, V1AppVersionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AppVersionRequest):
            return True

        return self.to_dict() != other.to_dict()
