# Travel With Friends

Thank you for taking the time to review this new code.

This is an attempt at creating a web application (mobile device option); an interactive platform that will allow users to connect annonymously with other users while traveling, in the hopes of meeting new people and experiencing new places.

If you would like to contribute to this code, I'm making this application open source, free to the public.

### Product Overview

The web application allows users to check their geo-location, surrounding landmarks, businesses, and events on their phone. Allowing the user to check-into a Journey or Trip that others have in the past or present, providing feedback and advice about the Journey. Users can also anonymously communicate with others users inside the app to ask questions and give further advice in real time. 

### Specific Functionality

Users can create, view, edit Profile, create or view Journey, create or view Events, send messages to other users, give feedback and rate other Users advice about Journey or Events.

Current Scope of Work:
* Landing Page
* User Account Creation
* Login with OAuth

Here is a mockup using [draw.io](https://draw.io/) showing some basic ideas.

Here is the [link](docs/twf_mockups.pdf) to the PDF image of the vision I have for this project. 


### Data Model

Nouns:
* USER
* JOURNEY
* LOCATION
* EVENT (Future Build)

Verbs:
* Register
* Login
* Create Profile
* Edit Profile
* Search Users, Journey, and Event
* Checking-In on Journey
* Traversing Location (List)
* Viewing Location  (Map)
* Create Event 
* Edit Event


USER {
    userID, userName, firstName, lastName, homeLocation, userImage, userNumber} 
    
  
JOURNEY {
    journeyID, locationID, eventID, journeyDetails, userID_tag}
    
LOCATION {
    geoTag, locationID, mapArea, radius, userID_tag,}
    
    

We'll be using a relational database which models things like a spreadsheet.
There are fixed fields and every instance

Since Postgres will be used, querying data by specific ID's that will link each User, Journey, and Place with a locationID.

### Technical Components

There will be 3 main Modules for this project:

* user
* journey
* location

Using these technologies:

* Browser Geolocation
* [Google Maps API JS/REST](https://developers.google.com/maps/documentation/javascript/?hl=en_US)
* SQLITE3 for database backend
* pytest

* HTML, CSS, JS, jQuery, BS4
* Django REST Framework
* [Cordova](https://cordova.apache.org/)
* [Twilio](https://www.twilio.com/?mkwid=s5YsI2dSk&pdv=c&pcrid=166298610378&pmt=e&pkw=twilio&campaign=G_S_Brand_Alpha_NA&utm_source=google&utm_medium=cpc&utm_term=twilio&utm_campaign=G_S_Brand_Alpha_NA&utm_content=Brand&gclid=Cj0KEQiA0L_FBRDMmaCTw5nxm-ABEiQABn-VqWpOgOYR24O93xODtHaATUJcdyqFQYtvQJxYBoguPdQaAhpj8P8HAQ) (User Device Auth)

The front-end will be a light weight framework with a robust back-end framework using Django and REST API to communicate data to and from the web application.

### Schedule

1. Create pages for the front end, designing specifically for mobile device usage.
2. Create JS modules that can communicate AJAX calls to the back-end DB.
3. Using Python, BS4, and Django REST Framework, allow for incomming requests and responses. 

### Further Work

Features to be rolled out in the future product releases:

1. Event creation
2. Business information and reviews
3. Communication between users, first annonymously, then allowed for user data to be shared.
4. Reviews and feedback, ratings that give weight to users good advice and info.
5. Upload images to Journey libraries.
6. Image text tranlation and comments using [Tesseract](http://tesseract.projectnaptha.com/)

## Submission

Capstone "Travel With Friends" available to review files and README.md via BitBucket in PDX Code Repo - File named "Capstone"