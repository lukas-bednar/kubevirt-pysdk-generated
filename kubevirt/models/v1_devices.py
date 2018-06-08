# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Devices(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'disks': 'list[V1Disk]',
        'interfaces': 'list[V1Interface]',
        'watchdog': 'V1Watchdog'
    }

    attribute_map = {
        'disks': 'disks',
        'interfaces': 'interfaces',
        'watchdog': 'watchdog'
    }

    def __init__(self, disks=None, interfaces=None, watchdog=None):
        """
        V1Devices - a model defined in Swagger
        """

        self._disks = None
        self._interfaces = None
        self._watchdog = None

        if disks is not None:
          self.disks = disks
        if interfaces is not None:
          self.interfaces = interfaces
        if watchdog is not None:
          self.watchdog = watchdog

    @property
    def disks(self):
        """
        Gets the disks of this V1Devices.
        Disks describes disks, cdroms, floppy and luns which are connected to the vm

        :return: The disks of this V1Devices.
        :rtype: list[V1Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """
        Sets the disks of this V1Devices.
        Disks describes disks, cdroms, floppy and luns which are connected to the vm

        :param disks: The disks of this V1Devices.
        :type: list[V1Disk]
        """

        self._disks = disks

    @property
    def interfaces(self):
        """
        Gets the interfaces of this V1Devices.
        Interfaces describe network interfaces which are added to the vm

        :return: The interfaces of this V1Devices.
        :rtype: list[V1Interface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this V1Devices.
        Interfaces describe network interfaces which are added to the vm

        :param interfaces: The interfaces of this V1Devices.
        :type: list[V1Interface]
        """

        self._interfaces = interfaces

    @property
    def watchdog(self):
        """
        Gets the watchdog of this V1Devices.
        Watchdog describes a watchdog device which can be added to the vm

        :return: The watchdog of this V1Devices.
        :rtype: V1Watchdog
        """
        return self._watchdog

    @watchdog.setter
    def watchdog(self, watchdog):
        """
        Sets the watchdog of this V1Devices.
        Watchdog describes a watchdog device which can be added to the vm

        :param watchdog: The watchdog of this V1Devices.
        :type: V1Watchdog
        """

        self._watchdog = watchdog

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Devices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
