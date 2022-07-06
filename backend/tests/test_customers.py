from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
client = TestClient(app)

testCustomer= {
  "first_name": "Mr Test",
  "last_name": "Testing",
  "email": "TT@gmail.com",
  "address": "Test Street 123",
  "city": "Testiny",
  "telephone": "691234567"
}

Customer1= {
  "customer_id": 1,
  "first_name": "Giorgos",
  "last_name": "Dimitriadis",
  "email": "dimitriadisg@gmail.com",
  "address": "Michalakopoulou 123",
  "city": "Athens",
  "telephone": "6913141567"
}

testUpdate= {
  "first_name": "Giannis",
  "last_name": "Kokki",
  "email": "kokki@gmail.com",
  "address": "Patreon 3",
  "city": "Patras",
  "telephone": "698529634"
}

NotFound = '{"code":404,"reason":"This customer id does not exist"}'

def test_customers():
    response = client.get("/customers")
    assert response.status_code == 200

def test_ExistingCustomerById():
    response = client.get("/customer/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == Customer1
    assert data["email"] == "dimitriadisg@gmail.com"

#non-existing customer (customer_id=0)
def test_NonExistingCustomerById():
    response = client.get("/customer/0")
    assert response.status_code == 404, response.text  
    data = response.content
    assert  data.decode("utf-8") == NotFound

def test_insertCustomer():
    response = client.post("/customer", json=testCustomer)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["first_name"] == "Mr Test"
    assert "customer_id" in data
    customer_id = data["customer_id"]

    response = client.get(f"/customer/{customer_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["customer_id"] == customer_id
    assert data["first_name"] == "Mr Test"
    assert data["last_name"] == "Testing"
    assert data["email"] == "TT@gmail.com"
    assert data["address"] == "Test Street 123"
    assert data["city"] == "Testiny"
    assert data["telephone"] == "691234567"

    #clean database-delete test costumer
    response = client.delete(f"/customer/{customer_id}")
    assert response.status_code == 200

def test_insertCustomerWithExistingEmail():
    #creating test costumer
    response = client.post("/customer", json=testCustomer)
    assert response.status_code == 200, response.text
    data = response.json()
    assert "customer_id" in data
    customer_id = data["customer_id"]
    
    #insert customer with same email
    response = client.post("/customer", json={
        "first_name": "Totally Different",
        "last_name": "Name",
        "email": "TT@gmail.com",
        "address": "Who knows",
        "city": "Faaaar Away",
        "telephone": "690000000"
        })
    assert response.status_code == 409, response.text
    data = response.content
    assert  data.decode("utf-8") == '{"code":409,"reason":"This email already exists"}'

    #clean database-delete test costumer
    response = client.delete(f"/customer/{customer_id}")
    assert response.status_code == 200

def test_updateExistingCustomer():

    #creating a test customer
    response = client.post("/customer", json=testUpdate)
    assert response.status_code == 200, response.text
    data = response.json()
    customer_id= data["customer_id"]

    #testing update
    response = client.put(f"/customer/{customer_id}", json=testCustomer)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["customer_id"] == customer_id
    assert data["first_name"] == "Mr Test"
    assert data["last_name"] == "Testing"
    assert data["email"] == "TT@gmail.com"
    assert data["address"] == "Test Street 123"
    assert data["city"] == "Testiny"
    assert data["telephone"] == "691234567"

    #clean database-delete test costumer
    response = client.delete(f"/customer/{customer_id}")
    assert response.status_code == 200

#non-existing customer (customer_id=0)
def test_updateNonExistingCustomer():
    response = client.put("/customer/0", json=testUpdate)
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == NotFound

def test_deleteExistingCustomer():
    #creating a test customer
    response = client.post("/customer", json=testUpdate)
    assert response.status_code == 200, response.text
    data = response.json()
    customer_id= data["customer_id"]

    #testing delete
    response = client.delete(f"/customer/{customer_id}")
    assert response.status_code == 200
    assert response.text == '"Customer deleted successfully."'
    response = client.get(f"/customer/{customer_id}")
    assert response.status_code == 404

def test_deleteExistingCustomer():
    response = client.delete("/customer/0")
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == NotFound
    