# InsuranceLabSolutionsRepo
Sample Project built with Python , Flask ,SQL-Alchemy and KnockoutJS for 'Feature Request Application'

## Feature Request Application:
This is a web application built with Python and Flask.
The home page where a user can fill in a feature request form, KnockoutJS is used for data binding and validation,
SQl-Alchemy ORM is used for persisting data into database Postgresql is used as database.A details page is rendered where a user can see feature request list in the form of a table.

## Getting Started:
Pre-requisites: Project is developed using
* Python (v.3.6.4), 
* PostgreSql database(v.10.1)
* Browsers: Chrome(v.64.) and Firefox(v.55+)
* Flask Virtual Environment.

## TODO:
* Building Project and Deploying In Cloud

## Installation:
1.Download the project folder from the github.

2.Uncomment the line inside config.py 
db_string = "postgres://postgres:Password0@localhost:5432/featureapp".
Make changes according to your local database and comment the cloud dbstring path.

3.Uncomment the line inside run_waitress_server.py "serve(APP,host="localhost",port="5000")" to run it on the localhost.

4.Activate the Virtual Environment for Flask
	
5.Then install required packages present in requirement.txt file 

6.Set Flask_APP variable by using command ‘set FLASK_APP=run_waitress_server.py’

7.Type ‘flask run’ and navigate to ‘http://127.0.0.1:5000/’ you can see Feature Request App form

## Form Page:
Open chrome/Mozilla and navigate to url ‘http://127.0.0.1:5000/’ where list of fields are present for customer to fill
in are as follows:
Here different types of form fields are used 
* String type,Date type,Integer Type
* Data binding are done using KnockoutJS.
* HTML attributes are used for validation.

## List of Details Page:
On Submission of valid data it routes to url ‘http://127.0.0.1:5000/FeatureRequestDetails’ of details page.
It list all the feature request details in a table which will have Sorting and Searching mechanism.

## Application Technical Stack
The following are requirements on the tech stack.
* OS: Windows/Linux
* Server Side Scripting: Python (3.6.4)
* Server Framework: Flask (0.12.2)
* SqlAlchemy (1.2.2)
* JavaScript: KnockoutJS (3.4.2)
* Testing: Unittest2 (1.1.0)
* Bootstrap for css
