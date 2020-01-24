from StrataCore.strata_config import StratumConfig
from StrataCore.strata_cdk import StrataStack

from aws_cdk import (
    core,
    aws_route53 as route53
)

from data_platform_access.constructs.cloudwatch_consumer_role_construct import CloudwatchConsumerRoleConstruct


class CloudwatchAccessStack(StrataStack):

    def __init__(self, scope: core.Construct, id: str, account_name, stratum: StratumConfig, **kwargs) -> None:
        super().__init__(scope, id, stratum, **kwargs)

        CloudwatchConsumerRoleConstruct(self, "data-platform-access-construct", stratum, account_name)
