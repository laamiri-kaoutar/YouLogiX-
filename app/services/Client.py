from app.repositories.Client_Repositroy import Client_Repositroy
from app.models.colis_models import Client
class Client_Service() :
    def __init__(self):
         self.Client_Reposiory = Client_Repositroy()
    def create(self, client:Client) : 
        self.Client_Reposiory.create(client)