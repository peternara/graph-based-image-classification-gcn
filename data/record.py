import tensorflow as tf


class Record(object):

    def __init__(self, height, width, depth, label, data):
        """
        Args:
            height: Number of rows in the record.
            width: Number of columns in the record.
            depth: Number of color channels in the record.
            label: An int64 tensor with the label of the record.
            data: A [height, width, depth] float32 tensor with the data of the
              record.
        """

        # TODO Assertions for label and data

        self._height = height
        self._width = width
        self._depth = depth

        self._label = label
        self._label.set_shape([1])
        self._data = data
        self._data.set_shape([height, width, depth])

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @property
    def depth(self):
        return self._depth

    @property
    def label(self):
        return self._label

    @property
    def data(self):
        return self._data
