from StrataCore.strata_cdk import StrataStack, StrataApp
from StrataCore.strata_config import StratumConfig

from template.constructs.template_construct import TemplateConstruct


class TemplateStack(StrataStack):

    def __init__(self, scope: StrataApp, id: str, stratum: StratumConfig, **kwargs) -> None:
        super().__init__(scope, id, stratum, **kwargs)

        construct = TemplateConstruct(self, "template-construct",)
