from StrataCore.strata_config import StratumConfig
from StrataCore.strata_cdk import StrataStack
from StrataCore.utils import save_parameter, as_list

from aws_cdk import (
    core,
    aws_route53 as route53
)


class AccountHostedZoneStack(StrataStack):

    def __init__(self, scope: core.Construct, id: str, account_name, stratum: StratumConfig, **kwargs) -> None:
        super().__init__(scope, id, stratum, **kwargs)

        construct = TemplateConstruct(self, "template-construct", stratum, account_name)
