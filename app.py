#!/usr/bin/env python3

from StrataCore.strata_config import StratumConfig
from StrataCore.strata_cdk import StrataApp

from template.stacks.template_stack import TemplateStack

app = StrataApp()


def account_level(context: StrataApp, stratum: StratumConfig):
    account_name = stratum.name

    template_stack = TemplateStack(context.app, 'template-stack', account_name, stratum, env={'region': stratum.region})
    return [template_stack]


app.per_account(account_level)
app.synth()
