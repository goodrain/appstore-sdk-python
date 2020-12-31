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


class V1StoreAppVersionTempleteAppProbe(object):
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
        'cmd': 'str',
        'failure_threshold': 'int',
        'http_header': 'str',
        'initial_delay_second': 'int',
        'is_used': 'bool',
        'mode': 'str',
        'path': 'str',
        'period_second': 'int',
        'port': 'int',
        'probe_id': 'str',
        'scheme': 'str',
        'service_id': 'str',
        'success_threshold': 'int',
        'timeout_second': 'int'
    }

    attribute_map = {
        'id': 'ID',
        'cmd': 'cmd',
        'failure_threshold': 'failure_threshold',
        'http_header': 'http_header',
        'initial_delay_second': 'initial_delay_second',
        'is_used': 'is_used',
        'mode': 'mode',
        'path': 'path',
        'period_second': 'period_second',
        'port': 'port',
        'probe_id': 'probe_id',
        'scheme': 'scheme',
        'service_id': 'service_id',
        'success_threshold': 'success_threshold',
        'timeout_second': 'timeout_second'
    }

    def __init__(self, id=None, cmd=None, failure_threshold=None, http_header=None, initial_delay_second=None, is_used=None, mode=None, path=None, period_second=None, port=None, probe_id=None, scheme=None, service_id=None, success_threshold=None, timeout_second=None, local_vars_configuration=None):  # noqa: E501
        """V1StoreAppVersionTempleteAppProbe - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._cmd = None
        self._failure_threshold = None
        self._http_header = None
        self._initial_delay_second = None
        self._is_used = None
        self._mode = None
        self._path = None
        self._period_second = None
        self._port = None
        self._probe_id = None
        self._scheme = None
        self._service_id = None
        self._success_threshold = None
        self._timeout_second = None
        self.discriminator = None

        self.id = id
        self.cmd = cmd
        self.failure_threshold = failure_threshold
        self.http_header = http_header
        self.initial_delay_second = initial_delay_second
        self.is_used = is_used
        self.mode = mode
        self.path = path
        self.period_second = period_second
        self.port = port
        self.probe_id = probe_id
        self.scheme = scheme
        self.service_id = service_id
        self.success_threshold = success_threshold
        self.timeout_second = timeout_second

    @property
    def id(self):
        """Gets the id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1StoreAppVersionTempleteAppProbe.


        :param id: The id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def cmd(self):
        """Gets the cmd of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The cmd of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        """Sets the cmd of this V1StoreAppVersionTempleteAppProbe.


        :param cmd: The cmd of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cmd is None:  # noqa: E501
            raise ValueError("Invalid value for `cmd`, must not be `None`")  # noqa: E501

        self._cmd = cmd

    @property
    def failure_threshold(self):
        """Gets the failure_threshold of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The failure_threshold of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: int
        """
        return self._failure_threshold

    @failure_threshold.setter
    def failure_threshold(self, failure_threshold):
        """Sets the failure_threshold of this V1StoreAppVersionTempleteAppProbe.


        :param failure_threshold: The failure_threshold of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and failure_threshold is None:  # noqa: E501
            raise ValueError("Invalid value for `failure_threshold`, must not be `None`")  # noqa: E501

        self._failure_threshold = failure_threshold

    @property
    def http_header(self):
        """Gets the http_header of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The http_header of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: str
        """
        return self._http_header

    @http_header.setter
    def http_header(self, http_header):
        """Sets the http_header of this V1StoreAppVersionTempleteAppProbe.


        :param http_header: The http_header of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and http_header is None:  # noqa: E501
            raise ValueError("Invalid value for `http_header`, must not be `None`")  # noqa: E501

        self._http_header = http_header

    @property
    def initial_delay_second(self):
        """Gets the initial_delay_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The initial_delay_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: int
        """
        return self._initial_delay_second

    @initial_delay_second.setter
    def initial_delay_second(self, initial_delay_second):
        """Sets the initial_delay_second of this V1StoreAppVersionTempleteAppProbe.


        :param initial_delay_second: The initial_delay_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and initial_delay_second is None:  # noqa: E501
            raise ValueError("Invalid value for `initial_delay_second`, must not be `None`")  # noqa: E501

        self._initial_delay_second = initial_delay_second

    @property
    def is_used(self):
        """Gets the is_used of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The is_used of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: bool
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        """Sets the is_used of this V1StoreAppVersionTempleteAppProbe.


        :param is_used: The is_used of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_used is None:  # noqa: E501
            raise ValueError("Invalid value for `is_used`, must not be `None`")  # noqa: E501

        self._is_used = is_used

    @property
    def mode(self):
        """Gets the mode of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The mode of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this V1StoreAppVersionTempleteAppProbe.


        :param mode: The mode of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mode is None:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def path(self):
        """Gets the path of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The path of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1StoreAppVersionTempleteAppProbe.


        :param path: The path of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and path is None:  # noqa: E501
            raise ValueError("Invalid value for `path`, must not be `None`")  # noqa: E501

        self._path = path

    @property
    def period_second(self):
        """Gets the period_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The period_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: int
        """
        return self._period_second

    @period_second.setter
    def period_second(self, period_second):
        """Sets the period_second of this V1StoreAppVersionTempleteAppProbe.


        :param period_second: The period_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and period_second is None:  # noqa: E501
            raise ValueError("Invalid value for `period_second`, must not be `None`")  # noqa: E501

        self._period_second = period_second

    @property
    def port(self):
        """Gets the port of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The port of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this V1StoreAppVersionTempleteAppProbe.


        :param port: The port of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def probe_id(self):
        """Gets the probe_id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The probe_id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: str
        """
        return self._probe_id

    @probe_id.setter
    def probe_id(self, probe_id):
        """Sets the probe_id of this V1StoreAppVersionTempleteAppProbe.


        :param probe_id: The probe_id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and probe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `probe_id`, must not be `None`")  # noqa: E501

        self._probe_id = probe_id

    @property
    def scheme(self):
        """Gets the scheme of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The scheme of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this V1StoreAppVersionTempleteAppProbe.


        :param scheme: The scheme of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and scheme is None:  # noqa: E501
            raise ValueError("Invalid value for `scheme`, must not be `None`")  # noqa: E501

        self._scheme = scheme

    @property
    def service_id(self):
        """Gets the service_id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The service_id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this V1StoreAppVersionTempleteAppProbe.


        :param service_id: The service_id of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service_id is None:  # noqa: E501
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

    @property
    def success_threshold(self):
        """Gets the success_threshold of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The success_threshold of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: int
        """
        return self._success_threshold

    @success_threshold.setter
    def success_threshold(self, success_threshold):
        """Sets the success_threshold of this V1StoreAppVersionTempleteAppProbe.


        :param success_threshold: The success_threshold of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and success_threshold is None:  # noqa: E501
            raise ValueError("Invalid value for `success_threshold`, must not be `None`")  # noqa: E501

        self._success_threshold = success_threshold

    @property
    def timeout_second(self):
        """Gets the timeout_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501


        :return: The timeout_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :rtype: int
        """
        return self._timeout_second

    @timeout_second.setter
    def timeout_second(self, timeout_second):
        """Sets the timeout_second of this V1StoreAppVersionTempleteAppProbe.


        :param timeout_second: The timeout_second of this V1StoreAppVersionTempleteAppProbe.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timeout_second is None:  # noqa: E501
            raise ValueError("Invalid value for `timeout_second`, must not be `None`")  # noqa: E501

        self._timeout_second = timeout_second

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
        if not isinstance(other, V1StoreAppVersionTempleteAppProbe):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1StoreAppVersionTempleteAppProbe):
            return True

        return self.to_dict() != other.to_dict()
