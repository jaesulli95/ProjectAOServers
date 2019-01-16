from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from timeit import default_timer as timer
from sql_connector import jae_connector as aodb
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:!aethor_josh_0987!@localhost:3306/aethor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
adb = aodb.aedb_connector("localhost", "root", "!aethor_josh_0987!", "aethor", 3306)
adb.connect()

class AethorCharacter(db.Model):
    __tablename__ = 'aethor_characters'
    aethor_character_id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    aethor_account_id = db.Column(db.Integer())
    name = db.Column(db.String(), nullable=False, unique=True)
    aethor_class = db.Column(db.Integer())
    armor = db.Column(db.String(256), nullable=False)


# account/characters'
@app.route('/account/characters', methods=['GET'])
def get_characters():
    start=timer()
    x = AethorCharacter.query.filter_by(aethor_account_id=1).all()
    db.session.commit()
    end=timer()
    print(end-start)
    return "Finished Executing Version 1 of Get Account Characters: " + str(end-start) + " seconds"

@app.route('/account/charactersV2', methods=['GET'])
def get_characters_v2():
    start=timer()
    x = adb.getAccountCharacters(1)
    end=timer()
    print(end-start)
    return jsonify({'characters':x})


if __name__ == '__main__':
    app.run(debug=True)