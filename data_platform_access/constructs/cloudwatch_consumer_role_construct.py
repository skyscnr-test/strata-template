from StrataCore.strata_config import StratumConfig
from StrataCore.strata_cdk import StrataConstruct
from aws_cdk import (
    aws_iam as iam,
    core,
)


class CloudwatchConsumerRoleConstruct(StrataConstruct):

    def __init__(self, scope: core.Construct, id: str, stratum: StratumConfig, account_name, **kwargs) -> None:
        super().__init__(scope, id, stratum)

        principal = iam.CompositePrincipal(
            iam.ArnPrincipal('arn:aws:iam::295180981731:user/svc_grafana_cloudwatch_access'),
            iam.ArnPrincipal('arn:aws:iam::325714046698:user/SVC_Grafana_CW_Production')
        )

        role = iam.Role(
            self,
            f'cloudwatch-consumer-role',
            assumed_by=principal,
            role_name='CloudWatchConsumerRole',
            path="/"
        )

        cloudwatch_policy = self.generate_cloudwatch_policy()
        role.attach_inline_policy(cloudwatch_policy)

    def generate_cloudwatch_policy(self):
        policy = iam.Policy(self, id='cloudwatch-metrics-policy')
        metrics_statement = iam.PolicyStatement()
        metrics_statement.add_all_resources()
        metrics_statement.add_actions(
            'cloudwatch:DescribeAlarmsForMetric',
            'cloudwatch:ListMetrics',
            'cloudwatch:GetMetricStatistics',
            'cloudwatch:GetMetricData'
        )

        ec2_statement = iam.PolicyStatement()
        ec2_statement.add_all_resources()
        ec2_statement.add_actions(
            'ec2:DescribeTags',
            'ec2:DescribeInstances',
            'ec2:DescribeRegions'
        )

        tags_statement = iam.PolicyStatement()
        tags_statement.add_all_resources()
        tags_statement.add_actions(
            'tag:GetResources'
        )

        policy.add_statements(metrics_statement)
        policy.add_statements(ec2_statement)
        policy.add_statements(tags_statement)
        return policy
