import os

from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

APP = Flask(__name__)
APP.config.from_object(Config)

from models import *

import featureRequestManager, featureRequestService,routes
