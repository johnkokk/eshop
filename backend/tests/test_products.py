from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
client = TestClient(app)

testProduct= {
    "name": "Test Product",
    "brand": "PyTest",
    "description": "This is an integration test for routes.product",
    "price": "101",
    "cost":  "21",
    "stock": "100",
    "size": "N/A",
    "category": "Hats" #sql enum restriction
}

Product1= {
  "product_id": 1,
  "name": "Nike Jockey Hat",
  "brand": "Nike",
  "description": "Sportswear H86 Nk Metal Swoosh",
  "price": 20,
  "cost": 8,
  "stock": 50,
  "size": "N/A",
  "category": "Hats"
}

testUpdate= {
    "name": "Updated Test Product",
    "brand": "New",
    "description": "wow I am so updated",
    "price": 5000,
    "cost":  5000,
    "stock": 20,
    "size": "Small",
    "category": "Equipment" #sql enum restriction
}

def test_products():
    response = client.get("/products")
    assert response.status_code == 200

def test_insertProduct():
    response = client.post("/product", json=testProduct)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test Product"
    assert "product_id" in data
    product_id = data["product_id"]

    response = client.get(f"/product/{product_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["description"] == "This is an integration test for routes.product"
    assert data["product_id"] == product_id

    response = client.delete(f"/product/{product_id}")
    assert response.status_code == 200

#testing with known-existing product 
def test_ExistingProductByID():
    response = client.get("/product/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data == Product1
    assert data["description"] =="Sportswear H86 Nk Metal Swoosh"
    assert data["size"] == "N/A"

NotFound = '{"code":404,"reason":"This product does not exist"}'

#testing for non-existing product (product_id=0)
def test_NonExistingProductByID():
    response = client.get("/product/0")
    assert response.status_code == 404, response.text  
    data = response.content
    #type(data)
    assert  data.decode("utf-8") == NotFound 


def test_updateExistingProduct():

    #creating a test product
    response = client.post("/product", json=testProduct)
    assert response.status_code == 200, response.text
    data = response.json()
    product_id= data["product_id"]

    #testing update
    response = client.put(f"/product/{product_id}", json=testUpdate)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["product_id"] == product_id
    assert data["name"] == "Updated Test Product"
    assert data["brand"] == "New"
    assert data["description"] == "wow I am so updated"
    assert data["price"] == 5000
    assert data["cost"] == 5000
    assert data["stock"] == 20
    assert data["size"] == "Small"
    assert data["category"] == "Equipment"

    #delete new inserted test-product
    response = client.delete(f"/product/{product_id}")
    assert response.status_code == 200

#No product with id=0
def test_updateNonExistingProduct():
    response = client.put("/product/0", json=testUpdate)
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == NotFound

def test_deleteExistingProduct():
    #creating a test-product
    response = client.post("/product", json=testProduct)
    assert response.status_code == 200, response.text
    data = response.json()
    product_id= data["product_id"]

    #delete test-product
    response = client.delete(f"/product/{product_id}")
    assert response.status_code == 200
    assert response.text == '"Product deleted successfully"'
    response = client.get(f"/product/{product_id}")
    assert response.status_code == 404


#No product with id=0
def test_deleteNonExistingProduct():
    response = client.delete(f"/product/0")
    assert response.status_code == 404, response.text
    data = response.content
    assert  data.decode("utf-8") == NotFound