**Project Overview**
This Django project serves as a portfolio website, showcasing personal information, skills, experiences, and client reviews. It dynamically renders content from a database to provide a personalized experience for visitors.

This Django project serves as a portfolio website, showcasing personal information, skills, experiences, and clients Review.

**Database Models Overview**
_Global Information_: Store global information such as name, designation, contact details, address, image, and social media links.
_Social Links:_ Add social media links with corresponding icons.
_Contact Information:_ Store email addresses and phone numbers.
_Skills:_ Organize skills into technical and professional categories with a percentage indicator.
_About Section:_ Include a description about yourself along with skills and a resume upload.
_Experiences:_ Add both educational and work experiences with titles, institutions, descriptions, and duration.
_Clients_Review:_ Display client information including images, review, names, and designations.

**Functions Overview**
The portfolio project consists of several functions to manage and display portfolio-related data. These functions are implemented in the views.py file.

_1. hi(request)_
Description: This function is the main view function responsible for rendering the portfolio homepage.
Parameters:
request: Represents the HTTP request from the client.
Functionality:
Retrieves data from the database tables including Global, About, Skills, Experiences, and Client.
Constructs a context dictionary containing the retrieved data.
Renders the index.html template with the context data.
Returns: HTTP response with the rendered HTML template.

**Usage**
Clone the repository.
Install the necessary dependencies using pip install -r requirements.txt.
Set up your database configurations in settings.py.
Run migrations using python manage.py migrate.
Create a superuser using python manage.py createsuperuser to access the admin panel.
Populate the database with your personal information, skills, experiences, and clients through the Django admin interface or programmatically.
Customize templates and stylesheets according to your preferences to personalize the portfolio website.
Run the development server using python manage.py runserver and navigate to `http://localhost:8000 `to view the website.

**Technologies Used**
Django
HTML
CSS
JavaScript 

**Contributing**
Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on the project repository.

**License**
The news website is open-source software released under the MIT License. Feel free to use, modify, and distribute the code as needed.
![Screenshot (333)](https://github.com/Avinanda2370/Myportfolio-Django/assets/102664151/5dcb36cc-58e6-47d8-8ce5-906e5d0c67b6)

