

import mutagenx as mg

class MetadataException(Exception):
    pass

class MetadataTypeNotSupported(MetadataException):
    pass

class Metadata:

    def __init__(self, path):
        self._meta = mg.File(path)
        if not self._meta:
            raise MetadataTypeNotSupported("Type not recognized")

    def __str__(self):
        return self._meta.pprint()
