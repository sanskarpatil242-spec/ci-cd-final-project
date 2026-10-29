"""
Test Cases for Account Service Routes
"""
import unittest
from service import app
from service.models import Account


class TestAccountRoutes(unittest.TestCase):
    """Test suite for Account routes"""

    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True

    def setUp(self):
        Account.data = {}
        self.client = app.test_client()

    def test_health(self):
        """Test the health check endpoint"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["status"], "OK")

    def test_create_account(self):
        """Test creating an account"""
        new_account = {"name": "Alice", "email": "alice@example.com", "address": "123 Main St"}
        resp = self.client.post("/accounts", json=new_account)
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertEqual(data["name"], "Alice")
        self.assertEqual(data["email"], "alice@example.com")

    def test_get_account(self):
        """Test getting an account by ID"""
        account = Account(name="Bob", email="bob@example.com").create()
        resp = self.client.get(f"/accounts/{account.id}")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["name"], "Bob")

    def test_get_account_not_found(self):
        """Test getting a non-existent account"""
        resp = self.client.get("/accounts/999")
        self.assertEqual(resp.status_code, 404)

    def test_list_accounts(self):
        """Test listing all accounts"""
        Account(name="Charlie", email="charlie@example.com").create()
        resp = self.client.get("/accounts")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(len(data), 1)

    def test_update_account(self):
        """Test updating an account"""
        account = Account(name="Dave", email="dave@example.com").create()
        resp = self.client.put(f"/accounts/{account.id}", json={"name": "David", "email": "dave@example.com"})
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["name"], "David")

    def test_delete_account(self):
        """Test deleting an account"""
        account = Account(name="Eve", email="eve@example.com").create()
        resp = self.client.delete(f"/accounts/{account.id}")
        self.assertEqual(resp.status_code, 204)
        resp = self.client.get(f"/accounts/{account.id}")
        self.assertEqual(resp.status_code, 404)


if __name__ == "__main__":
    unittest.main()
