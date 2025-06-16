# tests/test_full_flow.py

import pytest
from fastapi.testclient import TestClient
from faker import Faker
from main import app  # Make sure this points to your FastAPI app
import random
months = ["January", "February", "March", "April", "May", "June", "July"]
client = TestClient(app)
fake = Faker()

# Create fake user
def generate_user():
    return {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": "TestPass123"  # Static password to reuse for login
    }

def register_user(user):
    return client.post("/register", json=user)

def login_user(user):
    res = client.post("/login", data={
        "username": user["username"],
        "password": user["password"]
    })
    token = res.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}

def test_user_flow():
    user = generate_user()
    print(f"🔧 Registering user: {user['username']}")

    # 1. Register
    res = register_user(user)
    assert res.status_code == 200 or res.status_code == 409

    # 2. Login
    headers = login_user(user)
    assert headers["Authorization"].startswith("Bearer")

    # 3. Create Budget
    used_month_year = set()

    while True:
        month = random.choice(months)
        year = random.randint(2024, 2026)
        if (month, year) not in used_month_year:
            used_month_year.add((month, year))
            break
    budget_payload = {
        "month": month,
        "year": year,
        "amount": random.randint(10000, 100000)
    }
    res = client.post("/budget", json=budget_payload, headers=headers)
    assert res.status_code == 200
    budget_id = res.json()["id"]
    print(f"✅ Budget created: ID {budget_id}")

    # 4. Create Expense

    expense_payload = {
        "amount": 3500,
        "category": "Food",
        "description": "Dinner at a restaurant",
        "date": "2025-05-01T18:30:00"
    }
    res = client.post("/expense/", json=expense_payload, headers=headers)
    assert res.status_code == 200
    expense_id = res.json()["id"]
    print(f"✅ Expense created: ID {expense_id}")

    # 5. Get Expenses
    res = client.get("/expenses", headers=headers)
    assert res.status_code == 200
    assert any(exp["id"] == expense_id for exp in res.json())
    print(f"📦 Retrieved expenses: {len(res.json())}")

    # 6. Update Expense
    updated_payload = {
        "amount": 3000,
        "category": "Groceries",
        "description": "Changed description",
        "date": "2025-05-06T10:00:00"
    }
    res = client.put(f"/expense/{expense_id}", json=updated_payload, headers=headers)
    assert res.status_code == 200
    print("🔄 Expense updated successfully")

    # 7. Delete Expense
    # res = client.delete(f"/expense/{expense_id}", headers=headers)
    # assert res.status_code == 200
    # print("❌ Expense deleted")

    # 8. Create earnings
    earnings_payload = {
        "amount": 7000,
        "source": "Internship Stipend",
        "date": "2025-05-10T12:00:00"
    }
    res = client.post("/earnings/", json=earnings_payload, headers=headers)
    assert res.status_code == 200
    earnings_id = res.json()["id"]
    print(f"💰 earnings created: ID {earnings_id}")

    # 9. Get earningss
    res = client.get("/earnings", headers=headers)
    assert res.status_code == 200
    assert any(e["id"] == earnings_id for e in res.json())
    print(f"📥 Retrieved earningss: {len(res.json())}")

    # 10. Update earnings
    updated_earnings = {
        "amount": 8000,
        "source": "Updated Stipend",
        "date": "2025-05-11T14:00:00"
    }
    res = client.put(f"/earnings/{earnings_id}", json=updated_earnings, headers=headers)
    assert res.status_code == 200
    print("🔁 earnings updated")

    # 11. Delete earnings
    #res = client.delete(f"/earnings/{earnings_id}", headers=headers)
    #assert res.status_code == 200
    #print("❌ earnings deleted")

    # 12. Optional: Delete Budget
    #res = client.delete(f"/budget/{budget_id}", headers=headers)
    #if res.status_code == 200:
        #print("❌ Budget deleted")

