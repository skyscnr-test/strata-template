from StrataCore.strata_cdk import StrataStack, StrataApp

from template.constructs.template_construct import TemplateConstruct


class TemplateStack(StrataStack):

    def __init__(self, scope: StrataApp, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        construct = TemplateConstruct(self, "template-construct")
