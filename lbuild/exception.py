#!/usr/bin/env python3
#
# Copyright (c) 2015, Fabian Greif
# All Rights Reserved.
#
# The file is part of the lbuild project and is released under the
# 2-clause BSD license. See the file `LICENSE.txt` for the full license
# governing this code.


class BlobException(Exception):
    """
    Base class for exception thrown by lbuild.
    """
    pass

class OptionFormatException(BlobException):
    """
    Exception for all invalid option names.
    """
    def __init__(self, name):
        BlobException.__init__(self,
            "Invalid option format for '{}'. Option must contain "
            "one (repository option) or two (module option) "
            "colons.".format(name))