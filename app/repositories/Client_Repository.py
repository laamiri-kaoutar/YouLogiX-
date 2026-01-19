from app.models.colis_models import Client
class Client_Repository():
    
    def cereate(self , client :Client) :
        self.db.commit(client)
        self.db.refresh(client)
        return client