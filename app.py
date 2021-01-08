from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://louisthomasdods@localhost:5432/pd'
db = SQLAlchemy(app)

class project_divert_output(db.Model):
  __tablename__ = 'Project Divert Output'
  index = db.Column(db.Integer, primary_key=True)
  site = db.Column(db.String(), nullable=False)
  waste_stream = db.Column(db.String(), nullable=False)
  tonnage = db.Column(db.Float(), nullable=False)
  landfill_monetary = db.Column(db.Float(), nullable=False)
  landfill_transport_carbon = db.Column(db.Float(), nullable=False)
  mrf_monetary = db.Column(db.Float(), nullable=False)
  mrf_transport_carbon = db.Column(db.Float(), nullable=False)
  mrf_to_reproccesor_monetary = db.Column(db.Float(), nullable=False)
  mrf_to_reproccesor_carbon_transport = db.Column(db.Float(), nullable=False)
  divert_monetary = db.Column(db.Float(), nullable=False)
  divert_transport_carbon = db.Column(db.Float(), nullable=False)

  def __repr__(self):
    return f'<Project Divert Output {self.id} {self.description}>'

db.create_all()

@app.route('/')
def index():
  return render_template('index.html', data=project_divert_output.query.all())

 
