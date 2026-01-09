from fastapi.testclient import TestClient
from app.main import app 
from app.models.user_models import User, Role
from app.models.colis_models import StatutColis
from app.api.deps import get_current_user, get_current_active_livreur

client = TestClient(app)

# --- SETUP: Fake User (So we don't get 401 Errors) ---
fake_user = User(id=1, email="test@test.com", role=Role.LIVREUR)

# We tell FastAPI: "Whenever you need a user, use this fake one"
app.dependency_overrides[get_current_user] = lambda: fake_user
app.dependency_overrides[get_current_active_livreur] = lambda: fake_user


def test_colis_lifecycle():
    # 1. CREATE (POST)
    nouveau_colis = {
        "description": "Test Simple",
        "poids": 10.5,
        "adresse_depart": "Casa",
        "adresse_destination": "Rabat",
        "ville_destination": "Rabat",
        "destinataire_nom": "Omar",
        "destinataire_telephone": "0600000000",
        "destinataire_email": "omar@test.com",
        "id_zone": 1 ,
        "id_client": 3 
    }
    
    response_create = client.post("/api/v1/colis/", json=nouveau_colis)
    
    assert response_create.status_code == 200 
    
    colis_id = response_create.json()["id"]
    print(f"Created Colis ID: {colis_id}")

    # 2. UPDATE STATUS (PATCH)
    update_data = {
        "statut": StatutColis.EN_COURS.value, 
        "id_livreur": 1
    }
    
    response_update = client.patch(f"/api/v1/colis/{colis_id}/status", json=update_data)
    
    assert response_update.status_code == 200
    assert response_update.json()["statut"] == "en_cours"

    # 3. READ (GET)
    response_get = client.get(f"/api/v1/colis/{colis_id}")
    
    assert response_get.status_code == 200
    assert response_get.json()["destinataire_nom"] == "Omar"

    # 4. DELETE (DELETE)
    response_delete = client.delete(f"/api/v1/colis/{colis_id}")
    
    # Your delete controller usually returns 204 (No Content) or 200
    assert response_delete.status_code in [200, 204]

    # 5. VERIFY DELETE (GET should fail)
    response_check = client.get(f"/api/v1/colis/{colis_id}")
    assert response_check.status_code == 404