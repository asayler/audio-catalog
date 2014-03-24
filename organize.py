#! /usr/bin/env python3

import os
import sys
import shutil

import metadata as md

def process(path):

    for root, subdirs, subfiles in os.walk(path):

        for f in subfiles:

            f_path = os.path.join(root, f)
            try:
                f_meta = md.Metadata(f_path)
            except md.MetadataTypeNotSupported:
                continue
            print("{}: {}".format(f_path, f_meta.filetype()))


def _main(argv=None):

    if not argv:
        argv = sys.argv[1:]

    process(argv[0])

    return 0


if __name__ == "__main__":
    sys.exit(_main())
