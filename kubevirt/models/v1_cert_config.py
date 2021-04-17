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


class V1CertConfig(object):
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
        'duration': 'K8sIoApimachineryPkgApisMetaV1Duration',
        'renew_before': 'K8sIoApimachineryPkgApisMetaV1Duration'
    }

    attribute_map = {
        'duration': 'duration',
        'renew_before': 'renewBefore'
    }

    def __init__(self, duration=None, renew_before=None):
        """
        V1CertConfig - a model defined in Swagger
        """

        self._duration = None
        self._renew_before = None

        if duration is not None:
          self.duration = duration
        if renew_before is not None:
          self.renew_before = renew_before

    @property
    def duration(self):
        """
        Gets the duration of this V1CertConfig.
        The requested 'duration' (i.e. lifetime) of the Certificate.

        :return: The duration of this V1CertConfig.
        :rtype: K8sIoApimachineryPkgApisMetaV1Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this V1CertConfig.
        The requested 'duration' (i.e. lifetime) of the Certificate.

        :param duration: The duration of this V1CertConfig.
        :type: K8sIoApimachineryPkgApisMetaV1Duration
        """

        self._duration = duration

    @property
    def renew_before(self):
        """
        Gets the renew_before of this V1CertConfig.
        The amount of time before the currently issued certificate's \"notAfter\" time that we will begin to attempt to renew the certificate.

        :return: The renew_before of this V1CertConfig.
        :rtype: K8sIoApimachineryPkgApisMetaV1Duration
        """
        return self._renew_before

    @renew_before.setter
    def renew_before(self, renew_before):
        """
        Sets the renew_before of this V1CertConfig.
        The amount of time before the currently issued certificate's \"notAfter\" time that we will begin to attempt to renew the certificate.

        :param renew_before: The renew_before of this V1CertConfig.
        :type: K8sIoApimachineryPkgApisMetaV1Duration
        """

        self._renew_before = renew_before

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
        if not isinstance(other, V1CertConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
