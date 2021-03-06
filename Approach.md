#Donation Promise System


####Repository/Source

    https://github.com/olaseni/donation-promise-system

####Libraries/Tools

+ [Django][] (Web Framework, Tests, Forms, etc)
+ [Django Rest Framework][drf] (Rest APIs)
+ [PostgreSQL][] (RDBMS)
+ [Redis][] (Key-value Caching Server)
+ [Docker/Docker-Compose][]  (Images, Containers, Definition & Execution, etc)
+ [CircleCI][] (Continuous Integration Pipeline, Tests on PR, etc)  
+ [Trello][] (Project/Task Management)
  
    [circleci]: https://circleci.com/
    [docker/docker-compose]: https://hub.docker.com/
    [redis]: http://redis.io
    [PostgreSQL]: https://postgresql.org
    [django]: https://www.djangoproject.com/
    [drf]: https://www.django-rest-framework.org/
    [trello]: https://trello.com
    [vue.js]: https://vuejs.org/

####Approach

######Task Management/Status

_Trello_ will be used to map out the high-level sub-tasks that make up manageable units of the project, and to give
additional feedback where the need arises. The actual board will be communicated as soon as this is setup

######Containers

The application comprises multiple units and tools and servers. Docker and _docker-compose_ will be used to define the
containers that will host the disparate units for proper separation of concerns and to ease testing in the CI/CD 
pipeline.

######Persistence

The RDBMS, **PostgreSQL** in this case would be the persistent data store  and the source of truth for data. 
Redis will be employed as an in-memory cache that sits in between the DB and the logic that retrieves data. To reduce 
latency, data will be cached in Redis with an appropriate expiry on initial retrieval, so that subsequent requests will
take significantly less time and require less calculations. Requests will be initially made to Redis, and then to the 
DB on cache miss.

    
Django's data, ORM and migrations interfaces will be highly used to model causes data. Django's existing user 
architecture will be used to hold user profiles, roles and priviledges. This also covers registration and login.

To accommodate causes and promises, two entities/tables will be added:

 + **Contact**
    - Id
    - First Name
    - Last Name
    - Address
    - Phone
    - Email
    - Created

 + **Causes**
    - Id
    - Title
    - Description
    - Illustration
    - Contact Id (One to one relationship to contact)
    - Address
    - Phone
    - Email
    - Expiration Date
    - Target Amount
    - Created
    - Creator
    - Modified
    - Enabled
 
 + **Promises**
    - Id
    - Cause Id (Foreign key to `Causes`)  # note: unique index exists here to restrict promises per user per cause to 1
    - User Id (Foreign key to Django `Users`)
    - Amount Promised (i.e. all amounts will be in Naira - NGN)
    - Target Date
    - Created
    - Modified
    

######Actions

The core business logic will consist of actions that interact with the persistence/caching layer and exposing generic
functions:

 + Create cause (admin)
 + List causes
 + List available causes _i.e. causes which the user has no promise attached_
 + Read cause
 + Update cause (admin) _i.e. disable cause, change target, or extend expiration_
 + Delete cause (admin)
 + Add promise _i.e. associates unique promise to a cause_
 + List promises (admin all, user own)
 + Read promise (admin, own)
 + Update own promise _i.e. change amount pledged etc_
 + Delete own promise
 + List promises by cause (admin)
 + Get promise associated with a cause (user if own promise, admin can see any)
 + Get all causes promised
 
######Reports

 + Top 5 causes by amount (admin) _i.e. uses `Q()`_
 + Top 5 causes by promises (admin) _i.e. uses `Q()`_


######API

Uses DRF to expose the core actions via REST endpoints.
API Root is `/api/v1/`, with support for versioning.

 + **POST** `/cause/`  - _creates a cause_
 + **GET** `/cause/`  - _gets all active causes_
 + **GET** `/cause/available/`  - _gets all active causes_
 + **GET** `/cause/<int:id>/`  - _gets single cause_
 + **PUT** `/cause/<int:id>/`  - _updates single cause_
 + **DELETE** `/cause/<int:id>/`  - _deletes single cause_
 + **POST** `/promise/<int:cause_id>/make/`  - _make a promise to a cause_
 + **GET** `/promise/`  - _gets all promises_
 + **GET** `/promise/<int:id>/`  - _gets single promise_
 + **PUT** `/promise/<int:id>/`  - _updates single promise_
 + **DELETE** `/promise/<int:id>/`  - _deletes single promise_
 + **GET** `/cause/<int:id>/promises/` - _admin only, all promises by cause_
 + **GET** `/cause/<int:id>/promise/` - _promise associated with a cause_
 + **GET** `/cause/promised/` - _all causes which user has promised_
 + **GET** `/cause/top/amount/` - _top grossing causes by amount promised_
 + **GET** `/cause/top/promises/` - _top grossing causes by number of promises made_
 
######Views
 
The project will use forms and class based views to write the UI.

######Sub-Tasks 

The sub-tasks are domiciled on [Trello][trello-task] for easy management. [Go][trello-task] ->.

   [trello-task]: https://trello.com/b/rslpLFZE/donation-promise-system
   
######Notes

Once each task is completed. An appropriate PR with details will be created.