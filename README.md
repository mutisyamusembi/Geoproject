# Geoproject

The project assumes you already have docker installed on your machine. 

1. Clone the repository 
2. Create a docker machine and connect to it ```docker-machine create -d virtualbox dev`` && ```eval $(docker-machine env dev)```
3. From the root folder of the project, you can run ```docker-compose up --build -d``` to build and run the containers. 
4. If the build is successful, it should be running on the docker-machine IP. You can run ```docker-machine ls``` to check this.

The first page you are greeted with is the redox API documentation. It defines the API by the OpenAPI standard.

To make actual calls you are going to need to be authenticated. You can visit ```api/v1/dj-rest-auth/registration/``` to create a user. Only username and passord are required

On user createion, the endoint returns a token. Login with your credentials and lets have some fun!

The redox documentation lists all available urls. Alternatively you can use Swagger to interact with the urls, which can be found on the url ```swagger```. 




NB: 
The implemenation consists of four models, Order, OrderItems, Product and Category. Considering the relationships betweens the models,
You should create a Category first, then a Product, then and Order followed by Order items. 


