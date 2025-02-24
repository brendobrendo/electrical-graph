from neo4j import GraphDatabase

URI = "bolt://localhost:7687"  # Change if needed
AUTH = ("neo4j", "neo4jneo4j")  # Change credentials as needed

driver = GraphDatabase.driver(URI, auth=AUTH)

def get_db_session():
    return driver.session()

def add_device(device_id, power_rating_watts):
    with get_db_session() as session:
        session.run(
            "MERGE (d:Device {device_id: $device_id, power_rating_watts: $power_rating_watts})",
            device_id=device_id,
            power_rating_watts=power_rating_watts
        )
    
def get_device(device_id):
    with get_db_session() as session:
        result = session.run(
            "MATCH (d:Device {device_id: $device_id}) RETURN d LIMIT 1",
            device_id=device_id
        )
        return result.single()  # Ensures only one result is returned
