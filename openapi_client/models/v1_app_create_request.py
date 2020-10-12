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


class V1AppCreateRequest(object):
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
        'app_classification_id': 'str',
        'desc': 'str',
        'introduction': 'str',
        'logo': 'str',
        'name': 'str',
        'org_id': 'str',
        'publish_type': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'app_classification_id': 'appClassificationID',
        'desc': 'desc',
        'introduction': 'introduction',
        'logo': 'logo',
        'name': 'name',
        'org_id': 'orgID',
        'publish_type': 'publishType',
        'tags': 'tags'
    }

    def __init__(self, app_classification_id=None, desc=None, introduction=None, logo=None, name=None, org_id=None, publish_type=None, tags=None, local_vars_configuration=None):  # noqa: E501
        """V1AppCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_classification_id = None
        self._desc = None
        self._introduction = None
        self._logo = None
        self._name = None
        self._org_id = None
        self._publish_type = None
        self._tags = None
        self.discriminator = None

        self.app_classification_id = app_classification_id
        self.desc = desc
        self.introduction = introduction
        self.logo = logo
        self.name = name
        self.org_id = org_id
        self.publish_type = publish_type
        self.tags = tags

    @property
    def app_classification_id(self):
        """Gets the app_classification_id of this V1AppCreateRequest.  # noqa: E501


        :return: The app_classification_id of this V1AppCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_classification_id

    @app_classification_id.setter
    def app_classification_id(self, app_classification_id):
        """Sets the app_classification_id of this V1AppCreateRequest.


        :param app_classification_id: The app_classification_id of this V1AppCreateRequest.  # noqa: E501
        :type app_classification_id: str
        """
        if self.local_vars_configuration.client_side_validation and app_classification_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_classification_id`, must not be `None`")  # noqa: E501

        self._app_classification_id = app_classification_id

    @property
    def desc(self):
        """Gets the desc of this V1AppCreateRequest.  # noqa: E501


        :return: The desc of this V1AppCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this V1AppCreateRequest.


        :param desc: The desc of this V1AppCreateRequest.  # noqa: E501
        :type desc: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def introduction(self):
        """Gets the introduction of this V1AppCreateRequest.  # noqa: E501


        :return: The introduction of this V1AppCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._introduction

    @introduction.setter
    def introduction(self, introduction):
        """Sets the introduction of this V1AppCreateRequest.


        :param introduction: The introduction of this V1AppCreateRequest.  # noqa: E501
        :type introduction: str
        """
        if self.local_vars_configuration.client_side_validation and introduction is None:  # noqa: E501
            raise ValueError("Invalid value for `introduction`, must not be `None`")  # noqa: E501

        self._introduction = introduction

    @property
    def logo(self):
        """Gets the logo of this V1AppCreateRequest.  # noqa: E501


        :return: The logo of this V1AppCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this V1AppCreateRequest.


        :param logo: The logo of this V1AppCreateRequest.  # noqa: E501
        :type logo: str
        """
        if self.local_vars_configuration.client_side_validation and logo is None:  # noqa: E501
            raise ValueError("Invalid value for `logo`, must not be `None`")  # noqa: E501

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this V1AppCreateRequest.  # noqa: E501


        :return: The name of this V1AppCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1AppCreateRequest.


        :param name: The name of this V1AppCreateRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def org_id(self):
        """Gets the org_id of this V1AppCreateRequest.  # noqa: E501

        组织机构 ID  # noqa: E501

        :return: The org_id of this V1AppCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this V1AppCreateRequest.

        组织机构 ID  # noqa: E501

        :param org_id: The org_id of this V1AppCreateRequest.  # noqa: E501
        :type org_id: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def publish_type(self):
        """Gets the publish_type of this V1AppCreateRequest.  # noqa: E501


        :return: The publish_type of this V1AppCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._publish_type

    @publish_type.setter
    def publish_type(self, publish_type):
        """Sets the publish_type of this V1AppCreateRequest.


        :param publish_type: The publish_type of this V1AppCreateRequest.  # noqa: E501
        :type publish_type: str
        """
        if self.local_vars_configuration.client_side_validation and publish_type is None:  # noqa: E501
            raise ValueError("Invalid value for `publish_type`, must not be `None`")  # noqa: E501

        self._publish_type = publish_type

    @property
    def tags(self):
        """Gets the tags of this V1AppCreateRequest.  # noqa: E501


        :return: The tags of this V1AppCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1AppCreateRequest.


        :param tags: The tags of this V1AppCreateRequest.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if not isinstance(other, V1AppCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AppCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
