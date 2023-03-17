#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_aws_cost_explorer import SourceAwsCostExplorer

if __name__ == "__main__":
    source = SourceAwsCostExplorer()
    launch(source, sys.argv[1:])
