from constructs import Construct
from pst_foundation_service.foundation import Service
from pst_foundation_service.gateway import Gateway


class DoughnutService(Service):
    def __init__(self, scope: Construct, construct_id: str, gateway: Gateway):
        super().__init__(scope, construct_id, "doughnut-service", gateway)
        # TODO - add actual service resources
