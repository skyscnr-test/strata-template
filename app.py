#!/usr/bin/env python3

from StrataCore.strata_config import StratumConfig
from StrataCore.strata_cdk import StrataApp

from template.stacks.template_stack import TemplateStack

app = StrataApp()


def account_level(context: StrataApp, account_id):

    template_stack = TemplateStack(context, 'template-stack', None)
    return [template_stack]

def region_level(context: StrataApp, stratum: StratumConfig, region: str):
    template_stack = TemplateStack(context, 'template-stack', stratum, env={'region': stratum.region})
    return [template_stack]


def az_level(context: StrataApp, stratum: StratumConfig, az: str):

    template_stack = TemplateStack(context, 'template-stack', stratum, env={'region': stratum.region})
    return [template_stack]


app.per_account(account_level)

app.per_region(region_level)

app.per_az(az_level)

app.synth()
