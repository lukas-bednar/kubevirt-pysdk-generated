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


class V1RegistryDiskSource(object):
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
        'image': 'str',
        'image_pull_secret': 'str'
    }

    attribute_map = {
        'image': 'image',
        'image_pull_secret': 'imagePullSecret'
    }

    def __init__(self, image=None, image_pull_secret=None):
        """
        V1RegistryDiskSource - a model defined in Swagger
        """

        self._image = None
        self._image_pull_secret = None

        self.image = image
        if image_pull_secret is not None:
          self.image_pull_secret = image_pull_secret

    @property
    def image(self):
        """
        Gets the image of this V1RegistryDiskSource.
        Image is the name of the image with the embedded disk

        :return: The image of this V1RegistryDiskSource.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1RegistryDiskSource.
        Image is the name of the image with the embedded disk

        :param image: The image of this V1RegistryDiskSource.
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")

        self._image = image

    @property
    def image_pull_secret(self):
        """
        Gets the image_pull_secret of this V1RegistryDiskSource.
        ImagePullSecret is the name of the Docker registry secret required to pull the image. The secret must already exist.

        :return: The image_pull_secret of this V1RegistryDiskSource.
        :rtype: str
        """
        return self._image_pull_secret

    @image_pull_secret.setter
    def image_pull_secret(self, image_pull_secret):
        """
        Sets the image_pull_secret of this V1RegistryDiskSource.
        ImagePullSecret is the name of the Docker registry secret required to pull the image. The secret must already exist.

        :param image_pull_secret: The image_pull_secret of this V1RegistryDiskSource.
        :type: str
        """

        self._image_pull_secret = image_pull_secret

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
        if not isinstance(other, V1RegistryDiskSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
