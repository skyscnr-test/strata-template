from StrataCore.strata_cdk import StrataConstruct, StrataStack
from aws_cdk import aws_lambda_python as _lmbda, aws_logs as logs


class TemplateConstruct(StrataConstruct):

    def __init__(self, scope: StrataStack, id: str) -> None:
        super().__init__(scope, id)

        # access config via self.config
        _lmbda.PythonFunction(self, id="template-lambda",
                              entry="template/lambdas/template-lambda",
                              handler="handle_event",
                              index="main.py",
                              log_retention=logs.RetentionDays.ONE_MONTH)
        # Make resources here
