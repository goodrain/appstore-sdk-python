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


class V1AppBaseInfo(object):
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
        'app_detail_url': 'str',
        'app_key_id': 'str',
        'create_time': 'datetime',
        'desc': 'str',
        'dev_status': 'str',
        'download_count': 'int',
        'install_count': 'int',
        'introduction': 'str',
        'introduction_html': 'str',
        'is_official': 'bool',
        'logo': 'str',
        'market_id': 'str',
        'market_name': 'str',
        'market_url': 'str',
        'name': 'str',
        'publish_type': 'str',
        'start_count': 'int',
        'status': 'str',
        'tags': 'list[str]',
        'update_time': 'datetime',
        'versions': 'list[V1AppVersionBase]'
    }

    attribute_map = {
        'app_detail_url': 'appDetailURL',
        'app_key_id': 'appKeyID',
        'create_time': 'createTime',
        'desc': 'desc',
        'dev_status': 'devStatus',
        'download_count': 'downloadCount',
        'install_count': 'installCount',
        'introduction': 'introduction',
        'introduction_html': 'introductionHTML',
        'is_official': 'isOfficial',
        'logo': 'logo',
        'market_id': 'marketID',
        'market_name': 'marketName',
        'market_url': 'marketURL',
        'name': 'name',
        'publish_type': 'publishType',
        'start_count': 'startCount',
        'status': 'status',
        'tags': 'tags',
        'update_time': 'updateTime',
        'versions': 'versions'
    }

    def __init__(self, app_detail_url=None, app_key_id=None, create_time=None, desc=None, dev_status=None, download_count=None, install_count=None, introduction=None, introduction_html=None, is_official=None, logo=None, market_id=None, market_name=None, market_url=None, name=None, publish_type=None, start_count=None, status=None, tags=None, update_time=None, versions=None, local_vars_configuration=None):  # noqa: E501
        """V1AppBaseInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_detail_url = None
        self._app_key_id = None
        self._create_time = None
        self._desc = None
        self._dev_status = None
        self._download_count = None
        self._install_count = None
        self._introduction = None
        self._introduction_html = None
        self._is_official = None
        self._logo = None
        self._market_id = None
        self._market_name = None
        self._market_url = None
        self._name = None
        self._publish_type = None
        self._start_count = None
        self._status = None
        self._tags = None
        self._update_time = None
        self._versions = None
        self.discriminator = None

        self.app_detail_url = app_detail_url
        self.app_key_id = app_key_id
        self.create_time = create_time
        self.desc = desc
        self.dev_status = dev_status
        self.download_count = download_count
        self.install_count = install_count
        self.introduction = introduction
        self.introduction_html = introduction_html
        self.is_official = is_official
        self.logo = logo
        self.market_id = market_id
        self.market_name = market_name
        self.market_url = market_url
        self.name = name
        self.publish_type = publish_type
        self.start_count = start_count
        self.status = status
        self.tags = tags
        self.update_time = update_time
        self.versions = versions

    @property
    def app_detail_url(self):
        """Gets the app_detail_url of this V1AppBaseInfo.  # noqa: E501


        :return: The app_detail_url of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._app_detail_url

    @app_detail_url.setter
    def app_detail_url(self, app_detail_url):
        """Sets the app_detail_url of this V1AppBaseInfo.


        :param app_detail_url: The app_detail_url of this V1AppBaseInfo.  # noqa: E501
        :type app_detail_url: str
        """
        if self.local_vars_configuration.client_side_validation and app_detail_url is None:  # noqa: E501
            raise ValueError("Invalid value for `app_detail_url`, must not be `None`")  # noqa: E501

        self._app_detail_url = app_detail_url

    @property
    def app_key_id(self):
        """Gets the app_key_id of this V1AppBaseInfo.  # noqa: E501


        :return: The app_key_id of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._app_key_id

    @app_key_id.setter
    def app_key_id(self, app_key_id):
        """Sets the app_key_id of this V1AppBaseInfo.


        :param app_key_id: The app_key_id of this V1AppBaseInfo.  # noqa: E501
        :type app_key_id: str
        """
        if self.local_vars_configuration.client_side_validation and app_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_key_id`, must not be `None`")  # noqa: E501

        self._app_key_id = app_key_id

    @property
    def create_time(self):
        """Gets the create_time of this V1AppBaseInfo.  # noqa: E501


        :return: The create_time of this V1AppBaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this V1AppBaseInfo.


        :param create_time: The create_time of this V1AppBaseInfo.  # noqa: E501
        :type create_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def desc(self):
        """Gets the desc of this V1AppBaseInfo.  # noqa: E501


        :return: The desc of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this V1AppBaseInfo.


        :param desc: The desc of this V1AppBaseInfo.  # noqa: E501
        :type desc: str
        """
        if self.local_vars_configuration.client_side_validation and desc is None:  # noqa: E501
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def dev_status(self):
        """Gets the dev_status of this V1AppBaseInfo.  # noqa: E501


        :return: The dev_status of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._dev_status

    @dev_status.setter
    def dev_status(self, dev_status):
        """Sets the dev_status of this V1AppBaseInfo.


        :param dev_status: The dev_status of this V1AppBaseInfo.  # noqa: E501
        :type dev_status: str
        """
        if self.local_vars_configuration.client_side_validation and dev_status is None:  # noqa: E501
            raise ValueError("Invalid value for `dev_status`, must not be `None`")  # noqa: E501

        self._dev_status = dev_status

    @property
    def download_count(self):
        """Gets the download_count of this V1AppBaseInfo.  # noqa: E501


        :return: The download_count of this V1AppBaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._download_count

    @download_count.setter
    def download_count(self, download_count):
        """Sets the download_count of this V1AppBaseInfo.


        :param download_count: The download_count of this V1AppBaseInfo.  # noqa: E501
        :type download_count: int
        """
        if self.local_vars_configuration.client_side_validation and download_count is None:  # noqa: E501
            raise ValueError("Invalid value for `download_count`, must not be `None`")  # noqa: E501

        self._download_count = download_count

    @property
    def install_count(self):
        """Gets the install_count of this V1AppBaseInfo.  # noqa: E501


        :return: The install_count of this V1AppBaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._install_count

    @install_count.setter
    def install_count(self, install_count):
        """Sets the install_count of this V1AppBaseInfo.


        :param install_count: The install_count of this V1AppBaseInfo.  # noqa: E501
        :type install_count: int
        """
        if self.local_vars_configuration.client_side_validation and install_count is None:  # noqa: E501
            raise ValueError("Invalid value for `install_count`, must not be `None`")  # noqa: E501

        self._install_count = install_count

    @property
    def introduction(self):
        """Gets the introduction of this V1AppBaseInfo.  # noqa: E501


        :return: The introduction of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._introduction

    @introduction.setter
    def introduction(self, introduction):
        """Sets the introduction of this V1AppBaseInfo.


        :param introduction: The introduction of this V1AppBaseInfo.  # noqa: E501
        :type introduction: str
        """
        if self.local_vars_configuration.client_side_validation and introduction is None:  # noqa: E501
            raise ValueError("Invalid value for `introduction`, must not be `None`")  # noqa: E501

        self._introduction = introduction

    @property
    def introduction_html(self):
        """Gets the introduction_html of this V1AppBaseInfo.  # noqa: E501


        :return: The introduction_html of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._introduction_html

    @introduction_html.setter
    def introduction_html(self, introduction_html):
        """Sets the introduction_html of this V1AppBaseInfo.


        :param introduction_html: The introduction_html of this V1AppBaseInfo.  # noqa: E501
        :type introduction_html: str
        """
        if self.local_vars_configuration.client_side_validation and introduction_html is None:  # noqa: E501
            raise ValueError("Invalid value for `introduction_html`, must not be `None`")  # noqa: E501

        self._introduction_html = introduction_html

    @property
    def is_official(self):
        """Gets the is_official of this V1AppBaseInfo.  # noqa: E501


        :return: The is_official of this V1AppBaseInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_official

    @is_official.setter
    def is_official(self, is_official):
        """Sets the is_official of this V1AppBaseInfo.


        :param is_official: The is_official of this V1AppBaseInfo.  # noqa: E501
        :type is_official: bool
        """
        if self.local_vars_configuration.client_side_validation and is_official is None:  # noqa: E501
            raise ValueError("Invalid value for `is_official`, must not be `None`")  # noqa: E501

        self._is_official = is_official

    @property
    def logo(self):
        """Gets the logo of this V1AppBaseInfo.  # noqa: E501


        :return: The logo of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this V1AppBaseInfo.


        :param logo: The logo of this V1AppBaseInfo.  # noqa: E501
        :type logo: str
        """
        if self.local_vars_configuration.client_side_validation and logo is None:  # noqa: E501
            raise ValueError("Invalid value for `logo`, must not be `None`")  # noqa: E501

        self._logo = logo

    @property
    def market_id(self):
        """Gets the market_id of this V1AppBaseInfo.  # noqa: E501


        :return: The market_id of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._market_id

    @market_id.setter
    def market_id(self, market_id):
        """Sets the market_id of this V1AppBaseInfo.


        :param market_id: The market_id of this V1AppBaseInfo.  # noqa: E501
        :type market_id: str
        """
        if self.local_vars_configuration.client_side_validation and market_id is None:  # noqa: E501
            raise ValueError("Invalid value for `market_id`, must not be `None`")  # noqa: E501

        self._market_id = market_id

    @property
    def market_name(self):
        """Gets the market_name of this V1AppBaseInfo.  # noqa: E501


        :return: The market_name of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._market_name

    @market_name.setter
    def market_name(self, market_name):
        """Sets the market_name of this V1AppBaseInfo.


        :param market_name: The market_name of this V1AppBaseInfo.  # noqa: E501
        :type market_name: str
        """
        if self.local_vars_configuration.client_side_validation and market_name is None:  # noqa: E501
            raise ValueError("Invalid value for `market_name`, must not be `None`")  # noqa: E501

        self._market_name = market_name

    @property
    def market_url(self):
        """Gets the market_url of this V1AppBaseInfo.  # noqa: E501


        :return: The market_url of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._market_url

    @market_url.setter
    def market_url(self, market_url):
        """Sets the market_url of this V1AppBaseInfo.


        :param market_url: The market_url of this V1AppBaseInfo.  # noqa: E501
        :type market_url: str
        """
        if self.local_vars_configuration.client_side_validation and market_url is None:  # noqa: E501
            raise ValueError("Invalid value for `market_url`, must not be `None`")  # noqa: E501

        self._market_url = market_url

    @property
    def name(self):
        """Gets the name of this V1AppBaseInfo.  # noqa: E501


        :return: The name of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1AppBaseInfo.


        :param name: The name of this V1AppBaseInfo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def publish_type(self):
        """Gets the publish_type of this V1AppBaseInfo.  # noqa: E501


        :return: The publish_type of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._publish_type

    @publish_type.setter
    def publish_type(self, publish_type):
        """Sets the publish_type of this V1AppBaseInfo.


        :param publish_type: The publish_type of this V1AppBaseInfo.  # noqa: E501
        :type publish_type: str
        """
        if self.local_vars_configuration.client_side_validation and publish_type is None:  # noqa: E501
            raise ValueError("Invalid value for `publish_type`, must not be `None`")  # noqa: E501

        self._publish_type = publish_type

    @property
    def start_count(self):
        """Gets the start_count of this V1AppBaseInfo.  # noqa: E501


        :return: The start_count of this V1AppBaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_count

    @start_count.setter
    def start_count(self, start_count):
        """Sets the start_count of this V1AppBaseInfo.


        :param start_count: The start_count of this V1AppBaseInfo.  # noqa: E501
        :type start_count: int
        """
        if self.local_vars_configuration.client_side_validation and start_count is None:  # noqa: E501
            raise ValueError("Invalid value for `start_count`, must not be `None`")  # noqa: E501

        self._start_count = start_count

    @property
    def status(self):
        """Gets the status of this V1AppBaseInfo.  # noqa: E501


        :return: The status of this V1AppBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1AppBaseInfo.


        :param status: The status of this V1AppBaseInfo.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this V1AppBaseInfo.  # noqa: E501


        :return: The tags of this V1AppBaseInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1AppBaseInfo.


        :param tags: The tags of this V1AppBaseInfo.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this V1AppBaseInfo.  # noqa: E501


        :return: The update_time of this V1AppBaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this V1AppBaseInfo.


        :param update_time: The update_time of this V1AppBaseInfo.  # noqa: E501
        :type update_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def versions(self):
        """Gets the versions of this V1AppBaseInfo.  # noqa: E501


        :return: The versions of this V1AppBaseInfo.  # noqa: E501
        :rtype: list[V1AppVersionBase]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this V1AppBaseInfo.


        :param versions: The versions of this V1AppBaseInfo.  # noqa: E501
        :type versions: list[V1AppVersionBase]
        """
        if self.local_vars_configuration.client_side_validation and versions is None:  # noqa: E501
            raise ValueError("Invalid value for `versions`, must not be `None`")  # noqa: E501

        self._versions = versions

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
        if not isinstance(other, V1AppBaseInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1AppBaseInfo):
            return True

        return self.to_dict() != other.to_dict()
