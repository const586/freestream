#Embedded file name: freestream\Core\exceptions.pyo


class FreeStreamException(Exception):

    def __init__(self, msg = None):
        Exception.__init__(self, msg)

    def __str__(self):
        return str(self.__class__) + ': ' + Exception.__str__(self)


class OperationNotPossibleAtRuntimeException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class OperationNotPossibleWhenStoppedException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class OperationNotEnabledByConfigurationException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class NotYetImplementedException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class DuplicateDownloadException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class VODNoFileSelectedInMultifileTorrentException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class LiveTorrentRequiresUsercallbackException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class TorrentDefNotFinalizedException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)


class FreeStreamLegacyException(FreeStreamException):

    def __init__(self, msg = None):
        FreeStreamException.__init__(self, msg)
