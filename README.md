# fast-api-sample-app
This is a fast-api sample app to explore docker and K8s 

# Run using docker-compose 
```
docker-compose up --build
```

# curl request to add new user in docker
```
  curl -H 'Content-Type: application/json' \
      -d '{ "name": "Sam", "ph_no": "1232123123"}' \
      -X POST \
      http://0.0.0.0:8000/users
```

# Run using K8s in local
```
kubectl apply -f=database-persistent-volume-claim.yaml
kubectl apply -f=ping_deployment.yaml
kubectl apply -f=ping_service.yaml
kubectl apply -f=postgres_deployment.yaml
kubectl apply -f=postgres_service.yaml
kubectl apply -f=user_service.yaml
kubectl apply -f=user_deployment.yaml
```

# Delete K8s resources
```
kubectl delete deployment ping-server
kubectl delete deployment postgres-deployment
kubectl delete deployment user-server
kubectl delete service ping-service 
kubectl delete service postgres-cluster-ip-service
kubectl delete service user-service
kubectl delete PersistentVolumeClaim database-persistent-volume-claim
```

# curl request to add new user in K8s
```
  curl -H 'Content-Type: application/json' \
      -d '{ "name": "Sam", "ph_no": "1232123123"}' \
      -X POST \
      http://0.0.0.0:30036/users
```
