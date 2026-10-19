# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and ReplicaSets

## Objective
Deploy two applications, Product Catalog and Shopping Cart, on a three-node Kubernetes cluster. Use multiple replicas and pod anti-affinity to distribute replicas across different nodes.

## Technologies Used
- Docker
- Kubernetes
- Minikube
- Python
- Flask
- YAML

## Applications

### 1. Product Catalog
- Replicas: 2
- Endpoint: `/products`
- Returns a list of products with their IDs, names, and prices.

### 2. Shopping Cart
- Replicas: 3
- Endpoints:
  - `GET /cart` — retrieves cart items.
  - `POST /cart` — adds an item to the cart.

## Cluster Architecture
The cluster contains one control-plane node and two worker nodes:
- `devops-multinode`
- `devops-multinode-m02`
- `devops-multinode-m03`

Pod anti-affinity ensures that replicas of the same application are scheduled on separate nodes.

## Deployment Files
- `product_catalog.py` — Product Catalog Flask application
- `shopping_cart.py` — Shopping Cart Flask application
- `Dockerfile.product` — Product Catalog image configuration
- `Dockerfile.shopping` — Shopping Cart image configuration
- `product_catalog_deployment.yaml` — Product Catalog Deployment
- `shopping_cart_deployment.yaml` — Shopping Cart Deployment
- `product_catalog_service.yaml` — Product Catalog Service
- `shopping_cart_service.yaml` — Shopping Cart Service

## Verification
- Product Catalog: 2/2 replicas available.
- Shopping Cart: 3/3 replicas available.
- All five pods were running across the three nodes.
- Product Catalog returned Laptop, Phone, and Headphones.
- Shopping Cart successfully accepted a Laptop item through a POST request.

## API Testing

Retrieve products:
```bash
curl http://<product-catalog-url>/products
```

Retrieve cart items:
```bash
curl http://<shopping-cart-url>/cart
```

Add an item to the cart:
```bash
curl -X POST http://<shopping-cart-url>/cart \
  -H "Content-Type: application/json" \
  -d '{"id":1,"name":"Laptop","quantity":1}'
```

Replace the URLs with the current Minikube service tunnel URLs.

## Conclusion
Successfully deployed and tested two Flask applications on a three-node Minikube Kubernetes cluster using Deployments, Services, multiple replicas, and pod anti-affinity.

