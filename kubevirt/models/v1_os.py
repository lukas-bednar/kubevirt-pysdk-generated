# coding: utf-8

"""
    KubeVirt API, 

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1OS(object):
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
        'bios': 'V1BIOS',
        'boot_menu': 'V1BootMenu',
        'boot_order': 'list[V1Boot]',
        'sm_bios': 'V1SMBios',
        'type': 'V1OSType'
    }

    attribute_map = {
        'bios': 'bios',
        'boot_menu': 'bootMenu',
        'boot_order': 'bootOrder',
        'sm_bios': 'smBIOS',
        'type': 'type'
    }

    def __init__(self, bios=None, boot_menu=None, boot_order=None, sm_bios=None, type=None):
        """
        V1OS - a model defined in Swagger
        """

        self._bios = None
        self._boot_menu = None
        self._boot_order = None
        self._sm_bios = None
        self._type = None

        if bios is not None:
          self.bios = bios
        if boot_menu is not None:
          self.boot_menu = boot_menu
        if boot_order is not None:
          self.boot_order = boot_order
        if sm_bios is not None:
          self.sm_bios = sm_bios
        self.type = type

    @property
    def bios(self):
        """
        Gets the bios of this V1OS.

        :return: The bios of this V1OS.
        :rtype: V1BIOS
        """
        return self._bios

    @bios.setter
    def bios(self, bios):
        """
        Sets the bios of this V1OS.

        :param bios: The bios of this V1OS.
        :type: V1BIOS
        """

        self._bios = bios

    @property
    def boot_menu(self):
        """
        Gets the boot_menu of this V1OS.

        :return: The boot_menu of this V1OS.
        :rtype: V1BootMenu
        """
        return self._boot_menu

    @boot_menu.setter
    def boot_menu(self, boot_menu):
        """
        Sets the boot_menu of this V1OS.

        :param boot_menu: The boot_menu of this V1OS.
        :type: V1BootMenu
        """

        self._boot_menu = boot_menu

    @property
    def boot_order(self):
        """
        Gets the boot_order of this V1OS.

        :return: The boot_order of this V1OS.
        :rtype: list[V1Boot]
        """
        return self._boot_order

    @boot_order.setter
    def boot_order(self, boot_order):
        """
        Sets the boot_order of this V1OS.

        :param boot_order: The boot_order of this V1OS.
        :type: list[V1Boot]
        """

        self._boot_order = boot_order

    @property
    def sm_bios(self):
        """
        Gets the sm_bios of this V1OS.

        :return: The sm_bios of this V1OS.
        :rtype: V1SMBios
        """
        return self._sm_bios

    @sm_bios.setter
    def sm_bios(self, sm_bios):
        """
        Sets the sm_bios of this V1OS.

        :param sm_bios: The sm_bios of this V1OS.
        :type: V1SMBios
        """

        self._sm_bios = sm_bios

    @property
    def type(self):
        """
        Gets the type of this V1OS.

        :return: The type of this V1OS.
        :rtype: V1OSType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1OS.

        :param type: The type of this V1OS.
        :type: V1OSType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, V1OS):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
