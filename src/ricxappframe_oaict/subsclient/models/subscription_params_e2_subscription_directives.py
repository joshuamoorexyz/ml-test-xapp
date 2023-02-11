# coding: utf-8

"""
    RIC subscription

    This is the initial REST API for RIC subscription  # noqa: E501

    OpenAPI spec version: 0.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ricxappframe_oaict.subsclient.configuration import Configuration


class SubscriptionParamsE2SubscriptionDirectives(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'e2_timeout_timer_value': 'int',
        'e2_retry_count': 'int',
        'rmr_routing_needed': 'bool'
    }

    attribute_map = {
        'e2_timeout_timer_value': 'E2TimeoutTimerValue',
        'e2_retry_count': 'E2RetryCount',
        'rmr_routing_needed': 'RMRRoutingNeeded'
    }

    def __init__(self, e2_timeout_timer_value=None, e2_retry_count=None, rmr_routing_needed=None, _configuration=None):  # noqa: E501
        """SubscriptionParamsE2SubscriptionDirectives - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._e2_timeout_timer_value = None
        self._e2_retry_count = None
        self._rmr_routing_needed = None
        self.discriminator = None

        if e2_timeout_timer_value is not None:
            self.e2_timeout_timer_value = e2_timeout_timer_value
        if e2_retry_count is not None:
            self.e2_retry_count = e2_retry_count
        if rmr_routing_needed is not None:
            self.rmr_routing_needed = rmr_routing_needed

    @property
    def e2_timeout_timer_value(self):
        """Gets the e2_timeout_timer_value of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501

        How long time response is waited from E2 node  # noqa: E501

        :return: The e2_timeout_timer_value of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501
        :rtype: int
        """
        return self._e2_timeout_timer_value

    @e2_timeout_timer_value.setter
    def e2_timeout_timer_value(self, e2_timeout_timer_value):
        """Sets the e2_timeout_timer_value of this SubscriptionParamsE2SubscriptionDirectives.

        How long time response is waited from E2 node  # noqa: E501

        :param e2_timeout_timer_value: The e2_timeout_timer_value of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                e2_timeout_timer_value is not None and e2_timeout_timer_value > 10):  # noqa: E501
            raise ValueError("Invalid value for `e2_timeout_timer_value`, must be a value less than or equal to `10`")  # noqa: E501
        if (self._configuration.client_side_validation and
                e2_timeout_timer_value is not None and e2_timeout_timer_value < 1):  # noqa: E501
            raise ValueError("Invalid value for `e2_timeout_timer_value`, must be a value greater than or equal to `1`")  # noqa: E501

        self._e2_timeout_timer_value = e2_timeout_timer_value

    @property
    def e2_retry_count(self):
        """Gets the e2_retry_count of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501

        How many times E2 subscription request is retried  # noqa: E501

        :return: The e2_retry_count of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501
        :rtype: int
        """
        return self._e2_retry_count

    @e2_retry_count.setter
    def e2_retry_count(self, e2_retry_count):
        """Sets the e2_retry_count of this SubscriptionParamsE2SubscriptionDirectives.

        How many times E2 subscription request is retried  # noqa: E501

        :param e2_retry_count: The e2_retry_count of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                e2_retry_count is not None and e2_retry_count > 10):  # noqa: E501
            raise ValueError("Invalid value for `e2_retry_count`, must be a value less than or equal to `10`")  # noqa: E501
        if (self._configuration.client_side_validation and
                e2_retry_count is not None and e2_retry_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `e2_retry_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._e2_retry_count = e2_retry_count

    @property
    def rmr_routing_needed(self):
        """Gets the rmr_routing_needed of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501

        Subscription needs RMR route from E2Term to xApp  # noqa: E501

        :return: The rmr_routing_needed of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501
        :rtype: bool
        """
        return self._rmr_routing_needed

    @rmr_routing_needed.setter
    def rmr_routing_needed(self, rmr_routing_needed):
        """Sets the rmr_routing_needed of this SubscriptionParamsE2SubscriptionDirectives.

        Subscription needs RMR route from E2Term to xApp  # noqa: E501

        :param rmr_routing_needed: The rmr_routing_needed of this SubscriptionParamsE2SubscriptionDirectives.  # noqa: E501
        :type: bool
        """

        self._rmr_routing_needed = rmr_routing_needed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SubscriptionParamsE2SubscriptionDirectives, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubscriptionParamsE2SubscriptionDirectives):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionParamsE2SubscriptionDirectives):
            return True

        return self.to_dict() != other.to_dict()
