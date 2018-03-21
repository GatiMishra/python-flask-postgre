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

## TODO:
* Building Project and Deploying In Cloud

## Installation:
1.Download the project folder from the github.
2.Open cmd in project folder “InsuranceLabSolutionsRepo\FeatureRequestApplication\venv\Scripts” and execute the activate

**.. \InsuranceLabSolutionsRepo\FeatureRequestApplication\venv\Scripts>activate
**(venv)..\InsuranceLabSolutionsRepo\FeatureRequestApplication\venv\Scripts>
	
3.Then install required packages present in readme file 

**(venv)..InsuranceLabSolutionsRepo\FeatureRequestApplication\venv\Scripts> pip install –r where r is the package name

4.Set Flask_APP variable by using command ‘set FLASK_APP=FeatureRequestApp.py’

**(venv)..InsuranceLabSolutionsRepo\FeatureRequestApplication\venv\Scripts>set FLASK_APP=FeatureRequestApp.py
    
5.Type ‘flask run’ and navigate to ‘http://127.0.0.1:5000/’ you can see Feature Request App form

**(venv)..\FeatureRequestApplication\venv>flask run
						* Serving Flask app "FeatureRequestApplication"
						* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

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
