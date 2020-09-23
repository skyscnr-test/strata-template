from typing import Optional

from StrataCore.strata_config import StratumConfig, StrataConfig
from StrataCore.strata_cdk import StrataApp

from template.stacks.template_stack import TemplateStack

def account_level(context: StrataApp, account_id):
    template_stack = TemplateStack(context, 'template-stack')
    return [template_stack]


def region_level(context: StrataApp, stratum: StratumConfig, region: str):
    template_stack = TemplateStack(context, 'template-stack', stratum, env={'region': stratum.region})
    return [template_stack]


def az_level(context: StrataApp, stratum: StratumConfig, az: str):
    template_stack = TemplateStack(context, 'template-stack', stratum, env={'region': stratum.region})
    return [template_stack]


def run(config: Optional[StratumConfig]):
    app = StrataApp(config=config)
    app.per_account(account_level)
    app.per_region(region_level)
    app.per_az(az_level)
    return app
