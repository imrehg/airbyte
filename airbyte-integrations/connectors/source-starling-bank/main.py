#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_starling_bank import SourceStarlingBank

if __name__ == "__main__":
    source = SourceStarlingBank()
    launch(source, sys.argv[1:])
