from StrataCore.strata_config import StratumConfig
from StrataCore.strata_cdk import StrataConstruct
from aws_cdk import (
    aws_cloudformation as cfn,
    aws_ssm as ssm,
    core,
)


class TemplateConstruct(StrataConstruct):

    def __init__(self, scope: core.Construct, id: str, stratum: StratumConfig, account_name, **kwargs) -> None:
        super().__init__(scope, id, stratum)

        # Make resources here
