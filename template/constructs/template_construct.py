from StrataCore.strata_cdk import StrataConstruct, StrataStack


class TemplateConstruct(StrataConstruct):

    def __init__(self, scope: StrataStack, id: str) -> None:
        super().__init__(scope, id)

        # access config via self.config
        self.config

        # Make resources here
