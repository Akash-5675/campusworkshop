"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr8m0rddl9mmoies60-a.oregon-postgres.render.com",
        database="betsol_fzq1",
        user="betsol_fzq1_user",
        password="oyjwnCGg7t4uPXdU8qpPOsMUFLBtmGOO")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
