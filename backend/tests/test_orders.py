from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
client = TestClient(app)

Order1 = {
  "order_id": 1,
  "customer_id": 1,
  "date": "2022-05-17T16:10:11"
}

testOrder = {
    "customer_id": 5,
    "date": "2022-07-21T12:40:11"
}

testUpdate = {
    "customer_id": 1,
    "date": "2021-01-01T00:00:00"
}

NotFound = '{"code":404,"reason":"This order id does not exist"}'

def test_orders():
    response = client.get("/orders")
    assert response.status_code == 200

def test_ExistingOrderById():
    response = client.get("/order/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == Order1
    assert data["order_id"] == 1
    assert data["customer_id"] == 1
    assert data["date"] == "2022-05-17T16:10:11"

#non-existing order (order_id=0)
def test_NonExistingOrderById():
    response = client.get("/order/0")
    assert response.status_code == 404, response.text  
    data = response.content
    #type(data)
    assert  data.decode("utf-8") == NotFound

def test_insertOrder():
    response = client.post("/order", json=testOrder)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["date"] == "2022-07-21T12:40:11"
    assert data["customer_id"] == 5
    assert "order_id" in data
    order_id = data["order_id"]

    response = client.get(f"/order/{order_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["order_id"] == order_id
    assert data["date"] == "2022-07-21T12:40:11"
    assert data["customer_id"] == 5

    #clean database-delete test order
    response = client.delete(f"/order/{order_id}")
    assert response.status_code == 200

#Non-existing customer (customer_id=0)
def test_insertOrder_NoCustomer():
    response = client.post("/order", json={
        "customer_id": 0,
        "date": "2021-01-01T00:00:00"
    })
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == '{"code":404,"reason":"This customer does not exist"}'

def test_updateExistingOrder():
    #create test order
    response = client.post("/order", json=testOrder)
    assert response.status_code == 200, response.text
    data = response.json()
    order_id= data["order_id"]

    #testing update
    response = client.put(f"/order/{order_id}", json=testUpdate)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["order_id"] == order_id
    assert data["customer_id"] == 1
    assert data["date"] == "2021-01-01T00:00:00"

    #clean database-delete test order
    response = client.delete(f"/order/{order_id}")
    assert response.status_code == 200

#non-existing order (order_id=0)
def test_updateNonExistingOrder():
    response = client.put("/order/0", json=testUpdate)
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == NotFound

def test_updateExistingOrder_NoCustomer():
    #create test order
    response = client.post("/order", json=testOrder)
    assert response.status_code == 200, response.text
    data = response.json()
    order_id= data["order_id"]

    #testing update
    response = client.put(f"/order/{order_id}", json={
        "customer_id": 0,
        "date": "2021-01-01T00:00:00"
    })
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == '{"code":404,"reason":"This customer does not exist"}'

    #clean database-delete test order
    response = client.delete(f"/order/{order_id}")
    assert response.status_code == 200

def test_deleteOrder():
    #create test order
    response = client.post("/order", json=testOrder)
    assert response.status_code == 200, response.text
    data = response.json()
    order_id= data["order_id"]

    #clean database-delete test order
    response = client.delete(f"/order/{order_id}")
    assert response.text == '"Order deleted successfully."'
    response = client.get(f"/order/{order_id}")
    assert response.status_code == 404

def test_deleteNonExistingOrder():
    response = client.delete("/order/0")
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == NotFound