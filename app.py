#!/usr/bin/env python3

from StrataCore.strata_config import StrataConfig
from stratum import get_app

app = get_app(StrataConfig())

app.synth()
