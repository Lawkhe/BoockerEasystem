# BoockerEasystem
Current and future market trends force entities to be increasingly competitive. Every entity that wishes to compete in the current market must consider the information and accessibility of it; as one of the most important assets. For this reason, it is necessary for the entity to have the appropriate Information Systems to quickly and efficiently supply information with additional value in a reservation and service system within the reach of its users. In most cases, entities distribute all their information systems in various applications, with the inefficiency and repetition of data that this entails. For this reason, a suitable option may be the acquisition of a Boocker Easystem system.

## Requirements for local deployment:
- MySQL instance running on the system
- Python 3 installed (versión 3.7 > )
- Virtual environment (optional, but its use is recommended)

### Book and appointemnt for a  locker to used it in that period of reservation. 
### Order food directly from the restaurant within the application
### Access all kind of information regarding the university, such as: Bathroom maintnance times and the availability of the library. 

**Universidad Manuela Beltrán** _Software Architecture_
1. Diego Torres
2. Andres Escovar
3. Juan Hernandez

# ARC MODEL
### 1.-Introduction and goals 
Current and future market trends force entities to be increasingly competitive. Every entity that wishes to compete in the current market must consider the information and accessibility of it; as one of the most important assets. For this reason, it is necessary for the entity to have the appropriate Information Systems to quickly and efficiently supply information with additional value in a reservation and service system within the reach of its users. In most cases, entities distribute all their information systems in various applications, with the inefficiency and repetition of data that this entails. For this reason, a suitable option may be the acquisition of a Boocker Easystem system.

### 2.-Constraints
•	Apply said software in the infrastructure of the university.
•	That both the user and managers use the software in the intended way.
•	Software can only be made for a specific university or organization.

### 3.-Context & scope 
Booker Easystem offers an alternative solution to the permanent need of the different infrastructures presented in public and private entities, to maintain updated information about places of interest, reservation of services in execution and that at the same time it can be managed in an agile and timely, according to the needs of the entities that request it.
The origin of this approach lies in the large number of recurring users in the facilities, a number that is continuously increasing over time, which in some way makes it difficult to consult information, access reserved spaces, access services provided, location of points of interest. This leads to a relational increase of time in the users, this refers to a higher cost in the approach of an internal service

### 4.-Solution strategy
Based on the information previously provided, it is intended to develop an Intranet module with the capacity to generate the necessary information for the different entities, their places of interest, reservations and infrastructure information

### 5.-Building block view
![image](https://user-images.githubusercontent.com/50247627/168958515-d9007e63-d7a0-4b68-a22a-6052be23c4c9.png)

### 6.-Runtime view
![image](https://user-images.githubusercontent.com/50247627/168958562-363ff0d0-b042-4999-92fe-67efcf351edb.png)

### 7.-Deployment view
![image](https://user-images.githubusercontent.com/50247627/168958583-de9fa29d-f1b0-497c-9bb4-4a636d975967.png)

### 8.-Crosscutting concepts
•	Logging
•	Memory management
•	Privacy
•	Computer security

### 9.-Architectural decisions
![image](https://user-images.githubusercontent.com/50247627/168958647-ca6e3a67-eb7e-4a34-917f-f5970d568253.png)
![image](https://user-images.githubusercontent.com/50247627/168958658-38474a20-f026-4eeb-9f47-f483e582e61b.png)
![image](https://user-images.githubusercontent.com/50247627/168958666-a204ec90-022b-45b5-89d6-4325b90b2ffe.png)

![image](https://user-images.githubusercontent.com/50247627/168958684-6c5cd325-ec9c-41ff-ad58-12bd0ffc0314.png)

![image](https://user-images.githubusercontent.com/50247627/168958697-8f2010e2-266e-4cad-80ba-5785f148c5a7.png)

### 10.- Quality requirements
![image](https://user-images.githubusercontent.com/50247627/168958714-3c170475-05b5-41a6-a2ff-ab4664e3374e.png)

![image](https://user-images.githubusercontent.com/50247627/168958721-129f0e30-e9f4-4b6f-82c1-5dea77adc111.png)

![image](https://user-images.githubusercontent.com/50247627/168958731-fd4dc275-258b-42d4-a222-52efec1a3054.png)

![image](https://user-images.githubusercontent.com/50247627/168958735-400cbf02-86e6-4a97-9676-f68971a7c15d.png)

### 11.- Risks and technical debt  
● Notify the user when registering.
● Add a button to go back to login in the registry.
● Validate a single schedule per day per site of interest.

### 12.-Glossary
Lockers
