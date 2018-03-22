#import sys
#sys.path.append('E://Gati_Software//projects//example2//venv//')

# Import Unittest to create test cases, requests to post 
import unittest, requests, json
from unittest.mock import MagicMock
from config import Config
from app import featureRequestService, FeatureRequestApp

# TestCasesApp class inherits unittest.TestCase class and consists of different testcases to unittest featureapp
class UnitTestCases(unittest.TestCase):    

    # test_app_featureHomePage function tests routing url 'http://127.0.0.1:5000/' in routes.py
    def test_app_featureHomePage(self):
        """Tests for the Loading of Home Page URL"""
        self.assertEqual((requests.get(Config.featureHomePageURL)).status_code,200)
		
    # test_app_featureListPagePage function checks routing url 'http://127.0.0.1:5000/FeatureRequestDetails' in routes.py  
    def test_app_featureListPagePage(self):
        """Tests for the Loading of Details Page URL"""
        self.assertEqual((requests.get(Config.featureListPageURL)).status_code,200) 

    # test_app_featureRequestService_createFeatureRequestService tests createFeatureRequestService present in FeatureRequestService class in featureRequestService module using a mock session
    def test_app_featureRequestService_createFeatureRequestService(self):
        """Test for Successful insertion of values in the Feature Requests Form Page"""         
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        print("inside Mock test Feature request service", mock)
        # Creating an instance of FeatureRequestService class
        servicerequest= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class 
        servicerequest.setSession(mock)
        print("mock set",servicerequest.getSession())
        # Creating an instance of FeatureRequestApp model class with all required values
        insertrequestdata = FeatureRequestApp('Titl5', 'descr','Client B', 1, 'Billing', '2018-02-01')
        result= servicerequest.createFeatureRequestService(insertrequestdata)
        self.assertEqual(result,'success')

    # test_app_featureRequestService_retrieveFeatureRequestService tests createFeatureRequestService present in FeatureRequestService class in featureRequestService module using a mock session
    def test_app_featureRequestService_retrieveFeatureRequestService(self):
        """Tests successful retrieval of values from database for Feature Request Details"""        
        mock= MagicMock(Config.Session())
        print("inside Mock test Feature request service", mock)
        # Creating an instance of FeatureRequestService class
        servicerequest= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class 
        servicerequest.setSession(mock)
        print("mock set",servicerequest.getSession())
        # Creating an instance of FeatureRequestApp model class with all required values
        result= servicerequest.retrieveFeatureRequestService()
        # Checking result of retrieveFeatureRequestService
        self.assertIsNotNone(result)

    # test_app_featureRequestService_createFeatureRequestService tests createFeatureRequestService present in FeatureRequestService class in featureRequestService module using a mock session
    def test_app_featureRequestService_createFeatureRequestService_failure(self):
        """Tests successful submission of values in Feature Requests Form Page"""
        # Create an instance of MagicMock class with specification Session Class which gives a 'mock'Session instance
        mock= MagicMock(Config.Session())
        print("inside Mock test Feature request service", mock)
        # Creating an instance of FeatureRequestService class
        servicerequest= featureRequestService.FeatureRequestService()
        # setting a mock session using setSession function in FeatureRequestService class
        servicerequest.setSession(mock)
        print("mock set",servicerequest.getSession())
        # Creating an instance of FeatureRequestApp model class with invalidvalues
        insertrequestdata = FeatureRequestApp('TestTitle1', 'TestDesc1','Client A', 'invalidvalue' , 'Policies', '2018-03-02')
        result= servicerequest.createFeatureRequestService(insertrequestdata)
        self.assertEqual(result,'Error Occured')