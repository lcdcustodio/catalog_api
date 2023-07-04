Catalog API
===========


Flask application implementing a REST API in order to provide a Catalog API


------------

Setup Database
===========================

For this demo it was used Firestore from Google Firebase as database solution following DBaaS approach: 

1 - First of all a Firebase account must be created through the following link https://console.firebase.google.com/ and then create a project.
2 - Next step is to switch on Firestore resources in your project
3 - Generate a private key file for your service account. In the Firebase console, open Settings > Service Accounts.
4 - Click Generate New Private Key, then confirm by clicking Generate Key.
5 - Rename the JSON file to credentials.json and save at ./src/app folder
5 - Inside ./src/app folder enter the below code to your console:

- npx -p node-firestore-import-export firestore-import -a credentials.json -b backup.json

The line command above will import data from backup.json towards Firestore Database 


------------

Installation Flask App (Container approach using docker)
===========================

Deployment and running in a containerized environment, using docker

```
    git clone https://github.com/lcdcustodio/catalog_api.git
    cd catalog_api
    docker build -t catalog_api .
    docker run -p 5000:5000 catalog_api
``` 

Swagger doc will be available at http://localhost:5000/

<kbd>![Alt text](/picture/01.png "Flask application")</kbd>