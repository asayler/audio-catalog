

import mutagenx as mg


_mime_extensions = {
    'audio/x-flac': 'flac',
    'application/x-flac': 'flac'
}

class MetadataException(Exception):
    pass

class MetadataTypeNotSupported(MetadataException):
    pass

class Metadata:

    # Internal Methods

    def __init__(self, path):
        self._meta = mg.File(path)
        if not self._meta:
            raise MetadataTypeNotSupported("Type not recognized")

    def __str__(self):
        return self._meta.pprint()

    # Metadata Access

    def filetype(self):
        return _mime_extensions[self._meta.mime[0]]

    def mimetypes(self):
        return self._meta.mime

    def mimetype(self):
        return self.mimetypes()[0]
