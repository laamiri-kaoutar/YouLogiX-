from app.controllers.ZoneController import ZoneController
from app.schemas.zone_schemas import ZoneCreate
class Test() : 
    def zone_testing(slef) :
        zone_input = ZoneCreate(name="Casablanca Centre", code_postal="20000")
        zone = ZoneController().create(zone_input)
        print(zone)

if  __name__ == "__main__" :
    Test().zone_testing()

        
