# OnlineTicket 🎫

**a web app for buy tickets and select cinemas and etc with fastapi based on cinematicket.org** 

this apps is contain some diffrent endpoints and apis for handelling requests and return proper response 

this project has two side as backend and frontend which in bavkend its used diffrent technologies 
to have a well  result in developing and quality and performances in this side .

this project is monolithics (till now ) and based on python and fastapi web framework to develop 

!! this project not finished yet !! 

you can run this project by 3 ways :

___________________________________________________
1 : docker-compose 🥇
-----------------------------------------------------

if you have docker-compose installed on your systems you can change your directory to `` docker-compose.yml ``

file and run containers by this command :

``docker-compose up -d --build `` 

this command will execute containers as detach mode and if you dont wanna to run as detach you can run command without ``-d `` 
_____________________________________________
2 : run with docker file 🥈
-------------------------------------------------------------------

if you have docker service installed on your systems you can change your cirectory to ``dockerfile`` and then

``docker build -t <image-name:tag> . ``

and then for run image you have to run this command :

``docker run  -p <your port : 8000> --name <favourite-dontainer name > <image-name:tag>``

!! MAKE SURE THAT YOU HAVE INSTALLED `mongodb` ON YOUR SYSTEM OR ITS CONTAINER  !!

if you wanna to run mongo image you can run this command :

`` docker pull mongo ``

and for run that container  :

`` docker run -d -p 27017:27017 --name my-mongodb mongo ``

_________________________________________________
3 : run with `start.sh `file on /backend  🥉
----------------------------------------
if you dont wanna to run any other before you can run by `start.sh` file that is on /backend directory by run this command :

first be sure that file can run and have permissions to run 

to give permission you can run this command :

`sudo chmod +x start.sh`

and then write :

`./start.sh`

!! MAKE SURE THAT YOU HAVE INSTALLED `mongodb` ON YOUR SYSTEM OR ITS CONTAINER  !!


-------------------------------------------------------------


CONNECT ELASTIC SEARCH TO PROJECT 

 
```docker run -d -p 9200:9200 -p 9300:9300 --name elasticsearch_1 -e "discovery.type=single-node" -e "ELASTIC_PASSWORD=elastic" docker.elastic.co/elasticsearch/elasticsearch:8.11.3```


```docker run -d -p 5601:5601  --name kibana kibana:8.11.3```


```docker exec -it <token>```


```docker exec -it <verificant code>```


```docker cp elasticsearch_1:/usr/share/elasticsearch/config/certs/http_ca.crt .```


-------------------------------------------------------------

 ❗ this project is not completed as well and not recommend to use on real products but its features and properties can run properly and work without problen ❗


❗❗ NOTE ME IF THERE IS ANY BUG OR ISSUE OR ENHERITANCEMENT YOU NEED BY ISSUES ON GITHUB ❗❗


--------------------------------------------------------------

