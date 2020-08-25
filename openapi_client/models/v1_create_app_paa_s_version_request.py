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


class V1CreateAppPaaSVersionRequest(object):
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
        'description': 'str',
        'rainbond_version': 'str',
        'template': 'V1StoreAppVersionTemplate',
        'template_type': 'str',
        'version': 'str',
        'version_alias': 'str'
    }

    attribute_map = {
        'description': 'description',
        'rainbond_version': 'rainbondVersion',
        'template': 'template',
        'template_type': 'templateType',
        'version': 'version',
        'version_alias': 'versionAlias'
    }

    def __init__(self, description=None, rainbond_version=None, template=None, template_type=None, version=None, version_alias=None, local_vars_configuration=None):  # noqa: E501
        """V1CreateAppPaaSVersionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._rainbond_version = None
        self._template = None
        self._template_type = None
        self._version = None
        self._version_alias = None
        self.discriminator = None

        self.description = description
        self.rainbond_version = rainbond_version
        self.template = template
        self.template_type = template_type
        self.version = version
        self.version_alias = version_alias

    @property
    def description(self):
        """Gets the description of this V1CreateAppPaaSVersionRequest.  # noqa: E501


        :return: The description of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1CreateAppPaaSVersionRequest.


        :param description: The description of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def rainbond_version(self):
        """Gets the rainbond_version of this V1CreateAppPaaSVersionRequest.  # noqa: E501


        :return: The rainbond_version of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._rainbond_version

    @rainbond_version.setter
    def rainbond_version(self, rainbond_version):
        """Sets the rainbond_version of this V1CreateAppPaaSVersionRequest.


        :param rainbond_version: The rainbond_version of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :type rainbond_version: str
        """
        if self.local_vars_configuration.client_side_validation and rainbond_version is None:  # noqa: E501
            raise ValueError("Invalid value for `rainbond_version`, must not be `None`")  # noqa: E501

        self._rainbond_version = rainbond_version

    @property
    def template(self):
        """Gets the template of this V1CreateAppPaaSVersionRequest.  # noqa: E501


        :return: The template of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :rtype: V1StoreAppVersionTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this V1CreateAppPaaSVersionRequest.


        :param template: The template of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :type template: V1StoreAppVersionTemplate
        """
        if self.local_vars_configuration.client_side_validation and template is None:  # noqa: E501
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def template_type(self):
        """Gets the template_type of this V1CreateAppPaaSVersionRequest.  # noqa: E501


        :return: The template_type of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this V1CreateAppPaaSVersionRequest.


        :param template_type: The template_type of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :type template_type: str
        """
        if self.local_vars_configuration.client_side_validation and template_type is None:  # noqa: E501
            raise ValueError("Invalid value for `template_type`, must not be `None`")  # noqa: E501

        self._template_type = template_type

    @property
    def version(self):
        """Gets the version of this V1CreateAppPaaSVersionRequest.  # noqa: E501


        :return: The version of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1CreateAppPaaSVersionRequest.


        :param version: The version of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def version_alias(self):
        """Gets the version_alias of this V1CreateAppPaaSVersionRequest.  # noqa: E501


        :return: The version_alias of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :rtype: str
        """
        return self._version_alias

    @version_alias.setter
    def version_alias(self, version_alias):
        """Sets the version_alias of this V1CreateAppPaaSVersionRequest.


        :param version_alias: The version_alias of this V1CreateAppPaaSVersionRequest.  # noqa: E501
        :type version_alias: str
        """
        if self.local_vars_configuration.client_side_validation and version_alias is None:  # noqa: E501
            raise ValueError("Invalid value for `version_alias`, must not be `None`")  # noqa: E501

        self._version_alias = version_alias

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
        if not isinstance(other, V1CreateAppPaaSVersionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CreateAppPaaSVersionRequest):
            return True

        return self.to_dict() != other.to_dict()