from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///album.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Figurinha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image_path = db.Column(db.String(300), nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    figurinhas = Figurinha.query.all()
    return render_template('index.html', figurinhas=figurinhas)

@app.route('/pais/<pais>')
def pais(pais):
    figurinhas_pais = Figurinha.query.filter_by(pais=pais).all()
    return render_template('pais.html', pais=pais, figurinhas=figurinhas_pais)

if __name__ == '__main__':
    app.run(debug=True)
