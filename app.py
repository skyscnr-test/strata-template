#!/usr/bin/env python3

from StrataCore.strata_config import StratumConfig
from StrataCore.strata_cdk import StrataApp

from data_platform_access.stacks.cloudwatch_access_stack import CloudwatchAccessStack

app = StrataApp()


def account_level(context: StrataApp, stratum: StratumConfig):
    account_name = stratum.name

    cloudwatch_access_stack = CloudwatchAccessStack(context.app, 'data-platform-access-stack', account_name, stratum, env={'region': stratum.region})
    return [cloudwatch_access_stack]


app.per_account(account_level)
app.synth()
