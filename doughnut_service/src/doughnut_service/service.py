from constructs import Construct
from pst_foundation_service.foundation import Service
from pst_foundation_service.gateway import Gateway
from pst_foundation_service.package import name


class DoughnutService(Service):
    def __init__(self, scope: Construct, construct_id: str, gateway: Gateway):
        super().__init__(scope, construct_id, name(__package__), gateway)
        # TODO - add actual service resources
