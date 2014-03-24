#! /usr/bin/env python3

import os
import sys
import shutil

import mutagenx as mg

def process(path):

    for root, subdirs, subfiles in os.walk(path):

        print("{}".format(root))

        for f in subfiles:

            f_path = os.path.join(root, f)
            af_meta = mg.File(f_path)
            if not af_meta:
                continue

            print("{}:\n{}".format(f_path, af_meta.pprint()))


def _main(argv=None):

    if not argv:
        argv = sys.argv[1:]

    process(argv[0])

    return 0


if __name__ == "__main__":
    sys.exit(_main())
