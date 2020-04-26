from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname((__file__)))

app = Flask(__name__)
os_path_join = os.path.join(basedir, 'data.sqlite')
app_config_1 = app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite://' + os_path_join
app_config_2 = app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app_config_3 = app.config['SQLALCHEMY_COMMIT_TRACK_MODIFICATIONS'] = True

database = SQLAlchemy(app)

@app.route("/home")
@app.route(":id/inventory")
def greetings():
  return "Welcome to the dungeon, we have dust and flames!"

if __name__ == "__main__":
  app.run()