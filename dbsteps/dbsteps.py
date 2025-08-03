from dbclient.dbclient import PgClient


class DbSteps:
    def __init__(self, client: PgClient):
        self.client = client

    def get_id(self, registration_type=1):
        return self.client.fetchone(query=f"SELECT id FROM active_long WHERE registration_type_id = {registration_type} AND deleted_at IS NULL ")

    def get_tour_id(self):
        return self.client.fetchone(query="SELECT id FROM tours")

    def get_lead_id(self):
        return self.client.fetchone(query="SELECT id FROM leads WHERE id = (SELECT MAX(id) FROM leads)")

    def delete_id(self, id):
        return self.client.delete(query=f"DELETE FROM leads_history WHERE lead_id = {id}; DELETE FROM leads WHERE id = {id}")