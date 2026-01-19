from app.services.Client import Client_Service
from app.schemas.client_schemas import Client_Create
from app.models.colis_models import Client
class Client() :
    def __init__(self):
        self.client_service = Client_Service()
    def cerate(self,client : Client_Service) :
        client = Client(**client.model_dump(mode="orm"))
        self.client_service.cerate(client)