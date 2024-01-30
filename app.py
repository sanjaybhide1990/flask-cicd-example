from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid,pytz


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/cars"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

IST = pytz.timezone('Asia/Kolkata')
# migrate = Migrate(app,db)

def generate_uuid(): 
    return str(uuid.uuid4())

class ridersModel(db.Model): 
    __tablename__ = 'riders'

    id = db.Column(db.String(36),primary_key=True,default=generate_uuid,nullable=False)
    name = db.Column(db.Text(30),nullable=False)
    team = db.Column(db.Text(30),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False)

    def __init__(self,name,team,created_at,updated_at):
        self.name = name
        self.team = team
        self.created_at = created_at
        self.updated_at = updated_at
    
@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/addRider')
def add_rider():
    return 'Test statement!!'


@app.route('/test-route')
def test_route():
    return "Route is working!!"

@app.route('/testing-jenkins')
def check_pipeline():
    return 'Let us hope the pipeline is triggered via Jenkinsfile'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)