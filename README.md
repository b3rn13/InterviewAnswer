# InterviewAnswer
Medical Concierge Group Assignment

The solution presented here demonstrates how a web application is structured using the Model-View-Controller pattern (or MVC) 
and how it works in practice:

__The methodoly behind an MVC concept is:__
    -A user requests to view a page by entering a URL.
    -The Controller receives that request.
    -It uses the Models to retrieve all of the necessary data, organizes it, and sends it off to the...
    -The View, which then uses that data to render the final webpage presented to the the user in their browser.
    
__From a more technical standpoint__
  There are really four major components in play: routes, models, views, and controllers.
      
      Routes:Each route is associated with a controller - more specifically, a certain function within a controller, 
             known as a controller action. So when you enter a URL, the application attempts to find a matching route, 
             and, if it’s successful, it calls that route’s associated controller action.
             In the web application, the config.py has the #server fucntion that handles routing.
             
      Models:Within the web application, the model.py file was used to retrieve all of the necessary data 
             from the csv files-which acted as data stores; 
             
      Controllers: The folder controller contains the controller.py module that handles the data retrieved from the models,
                   this data will be passed into the views files to be rendered when the requested page is typed 
                   i.e localhost/8080.
                   The data retrieved via the models is generally added to a data structure (like a list or dictionary), 
                   and that structure is what’s sent to the view.
              
       Views:The view accesses the structure of data and uses it to render the requested page, 
             which is then presented to the user in their browser. In the web app, the views package is the templates
             package/folder and usually files such as index.html or layout.html which usually serve as templates 
             are stored in there to render the desired view
             
The technical summary of the MVC request process is as follows:
            -A user requests to view a page by entering a URL.
            -The application matches the URL to a predefined route.
            -The controller action associated with the route is called.
            -The controller action uses the models to retrieve all of the necessary data from a database,
                places the data in an array, and loads a view, passing along the data structure.
            -The view accesses the structure of data and uses it to render the requested page,
                which is then presented to the user in their browser.

  
I used Modular Programming inorder to implement my solution to the assignment.
  
    ***Modular programming***: refers to the process of breaking a large, unwieldy programming task into separate, smaller, 
    more manageable subtasks or modules. Individual modules can then be cobbled together like building blocks 
    to create a larger application.
    
    There are several advantages to modularizing code:
    
        -Simplicity: A module typically focuses on one relatively small portion of the problem. Working on a single module,
                      meant that I had a smaller problem domain to wrap my head around. 
                      This made the development easier and less error-prone.
                      
        -Maintainability: Modules are typically designed so that they enforce logical boundaries between different problem
                          domains. If modules are written in a way that minimizes interdependency, there is decreased 
                          likelihood that modifications to a single module will have an impact on other parts of the program.
                          (This can make it possible for other developers to make changes to a given module without having any
                          knowledge of the application outside that module which makes it more viable for a team of many
                          programmers to work collaboratively on a large application.

        -Reusability: Functionality defined in a single module can be easily reused (through an appropriately defined
                      interface) by other parts of the application. This eliminates the need to recreate duplicate code.

        -Scoping: Modules typically define a separate namespace, which helps avoid collisions between identifiers in 
                 different areas of a program. 
                 (One of the tenets in the Zen of Python is Namespaces are one honking great idea—let’s do more of those!)
                 
***Note***:Functions, modules and packages are all constructs in Python that promote code modularization.

In developing this web application, 
  I created my own modules and packages which helped me organize and modularize my code, which made the coding, maintenance, 
  and debugging easier.
  
  The ***MODULES/PACKAGES*** in this Web Application are: models.py/models, controller.py/controller, index.py/templates.
  Remember I mentioned that I followed the MVC pattern so
  
The application is set-up as shown below:

  InterviewAnswer
    │   .gitignore
    │   characters.csv
    │   config.py
    │   episode_per_season.csv
    │   LICENSE
    │   README.md│   
    │   
    ├───controller
    │       controller.py
    │       __init__.py
    │       
    ├───models
    │       models.py
    │       __init__.py
    │       
    └───templates
            index.html
            index.py
            __init__.py
            

   From the above tree structure: the models, controller, and templates are Packages.
   while models.py is the MODELS module; controller.py is the CONTROLLERS module; index.py is the VIEW module; 
   and config.py contains the ROUTES module.
   
     **Note: The templates package was not imported into the controller package in order to serve the template-index.html,
     no 3rd party library was imported.
     However Please note that inorder to render the template, there is a requirement to download JINJA2 
     and more configurations have to be made to the index.html file inorder to exploit the use of the JINJA2 library
   
   In order to run the web application, type `python config.py`
   The application will be accessed from [localhost:8080](http://localhost:8080) in your browser
