# fast-api-sample-app
This is a fast-api sample app to explore docker and K8s 

# Run using docker-compose 
```
docker-compose up --build
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
