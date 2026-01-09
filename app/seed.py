# seed.py
from app.core.database import SessionLocal, engine, Base
from app.models import colis_models, user_models 

# Ensure tables exist
Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    print("🌱 Seeding database (Auto-IDs)...")

    # 1. Create Objects WITHOUT specifying 'id'
    zone = colis_models.Zone(name="Centre Ville", code_postal="10000")
    
    client = user_models.ClientExpediteur(
        nom="Dupont",
        prenom="Jean",
        email="jean.dupont@example.com",
        telephone="0600000001",
        adresse="123 Rue Principale"
    )

    destinataire = user_models.Destinataire(
        nom="Martin",
        prenom="Sophie",
        email="sophie.martin@example.com",
        telephone="0600000002",
        adresse="456 Avenue de la Liberté"
    )

    livreur = user_models.Livreur(
        nom="Speedy",
        prenom="Gonzales",
        telephone="0600000003",
        vehicule="Scooter"
    )

    try:
        # 2. Add to session and flush
        # flushing sends data to DB and gets the IDs back, but doesn't finalize the transaction yet
        db.add(zone)
        db.add(client)
        db.add(destinataire)
        db.add(livreur)
        
        db.flush() # <--- This prompts the DB to generate the IDs and assign them to our python objects

        # 3. Commit to save permanently
        db.commit()

        print("✅ Database populated successfully!")
        print("👇 USE THESE IDs FOR YOUR TEST JSON 👇")
        print(f"  -> id_client: {client.id}")
        print(f"  -> id_destinataire: {destinataire.id}")
        print(f"  -> id_zone: {zone.id}")
        print(f"  -> id_livreur: {livreur.id}")
        
    except Exception as e:
        print(f" Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()