# Revenue Technology Software Engineer Code Test

The test covers the following:
* General Python/Django/Django Rest Framework Web Development Proficiency
* API design
* General JavaScript Web Development Proficiency (A nice to have, OPTIONAL, you can use the DRF web interface)
* Comfort with working in a docker environment
* Ability to write tests!!! and document code

__Note:__ Feel free to use any 3rd party libraries for any portion of this. In some cases, it is encouraged. Part of the follow-up is a discussion of why you chose certain libraries. Some of this test is intentionally open-ended, so treat it as if it would go into production (after a many more hours of work) and be a long-lasting application (Remember to test)

Best of luck and have fun!


## Assignment

There are four database tables represented in models in `core/models.py`. Currently there is no API on top of those models. Building out some of that API is your task as well as a potentially a client app using react on top of those endpoints. Styling is not a requirement but if you have time go for it.

This assignment should not take more than 2-3 hours. The goal of the assignment is not to tease out the test taker's deep knowledge of the DRF API, rather to see how well one can work in a web environment with consideration of how that work will interact with other parts of the stack. If you are running out of time feel free to write some form of psuedocode to show how you would have done it. 

### Cards:

#### Card/Ticket 1: Feature

A list view of the campaigns that has the campaign information as well as the product name.

_API:_
Create an API endpoint that allows a user to GET multiple campaigns. The URL via query params should also be able to filter on:
1. Product Name
2. Name
3. Start Date (greater than, less than or equal to)
4. End Date (greater than, less than or equal to)

Note: Feel free to use a third party API library or a Django Rest Framework Extension for this. The end goal is user functionality.

_Client:_
If you have time add the filtering and styling to the client although that is outside the scope of the assignment

#### Card 2: Feature

Create an API endpoint that allows a user to POST a new campaign to a preexisting product through a form in a modal in the frontend that is accessible on the campaign list view. 

The one piece of validation required is that a campaign for a certain product cannot a have date overlap with another
 campaign for the same product. If a user attempts this, they should see some type of validation error in the modal
 
## Set up

### Docker
Make sure you have docker installed: https://www.docker.com/products/docker-desktop

### nodejs

Install if it isn't already installed https://nodejs.org/en/download/

#### Commands

In the project directory run the follow to build/setup your local environment

```bash
docker-compose build
```

To start your containers
```bash
docker-compose up
```

To run django migrations 
```bash
docker-compose exec web python manage.py migrate
```

To create superuser in order to access admin

```bash
docker-compose exec web python manage.py createsuperuser
```

Navigate to http://localhost:8000/admin to login

Build Frontend
```bash
cd frontend
npm install
```

Run Frontend
```bash
cd frontend
npm start
```

To see the logs
```bash
docker-compose logs -f  
```
