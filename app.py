from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content
        }

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "GET":
        notes = Note.query.all()
        return jsonify([note.to_dict() for note in notes])

    if request.method == "POST":
        content = request.json.get("content")
        if not content:
            return jsonify({"error": "Content is required"}), 400

        note = Note(content=content)
        db.session.add(note)
        db.session.commit()

        return jsonify(note.to_dict()), 201

@app.route("/notes/<int:note_id>", methods=["GET", "PUT", "DELETE"])
def note_detail(note_id):
    note = Note.query.get_or_404(note_id)

    if request.method == "GET":
        return jsonify(note.to_dict())

    if request.method == "PUT":
        content = request.json.get("content")
        if not content:
            return jsonify({"error": "Content is required"}), 400

        note.content = content
        db.session.commit()

        return jsonify(note.to_dict())

    if request.method == "DELETE":
        db.session.delete(note)
        db.session.commit()

        return jsonify({"message": "Note deleted"}), 200

def main():
    app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    main()

