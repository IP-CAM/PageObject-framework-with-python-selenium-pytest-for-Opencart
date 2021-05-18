# OpenCartPetProject
PageObject framework on python\selenium for opencart online store
__________________________________________________________________________________________________________________
Allure

python -m pytest --alluredir results       # test run with allure data generation
allure serve results                       # launch local server with allure reports
__________________________________________________________________________________________________________________
Jenkins
java -jar jenkins.war --httpPort=9090      # start jenkins from his folder



__________________________________________________________________________________________________________________
Docker

docker-compose.yml                     # configuration fail
docker-compose up                      # launch conteiner
docker-compose up -d                   # detached launch
docker ps                              # info for running containers
docker kill 'container id'             # kill container №
docker-compose stop 'container name'   # soft stop
__________________________________________________________________________________________________________________
version: '2'
services:
  phpadmin:
    image: 'phpmyadmin/phpmyadmin:5.0.0'
    environment:
      - PMA_HOST=mariadb
      - PMA_PORT=3306
      - PMA_USER=bn_opencart
    ports:
      - '8080:80'
  mariadb:
    image: docker.io/bitnami/mariadb:10.3
    environment:
      - ALLOW_EMPTY_PASSWORD=yes
      - MARIADB_USER=bn_opencart
      - MARIADB_DATABASE=bitnami_opencart
    ports:
      - '3306:3306'
    volumes:
      - 'mariadb_data:/bitnami/mariadb'
  opencart:
    image: docker.io/bitnami/opencart:3
    ports:
      - '80:8080'
      - '443:8443'
    environment:
      - OPENCART_HOST=localhost
      - OPENCART_DATABASE_HOST=mariadb
      - OPENCART_DATABASE_PORT_NUMBER=3306
      - OPENCART_DATABASE_USER=bn_opencart
      - OPENCART_DATABASE_NAME=bitnami_opencart
      - ALLOW_EMPTY_PASSWORD=yes
    volumes:
      - 'opencart_data:/bitnami/opencart'
      - 'opencart_storage_data:/bitnami/opencart_storage/'
    depends_on:
      - mariadb
      - phpadmin
volumes:
  mariadb_data:
    driver: local
  opencart_data:
    driver: local
  opencart_storage_data:
    driver: local
 ______________________________________________________________________________________________________________________
