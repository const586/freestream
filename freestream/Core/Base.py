#Embedded file name: freestream\Core\Base.pyo
from freestream.Core.exceptions import *
DEBUG = False

class Serializable:

    def __init__(self):
        pass


class Copyable:

    def copy(self):
        raise NotYetImplementedException()
