from flask import Flask
from controllers.mutant_controller import mutant_bp
from repositories.dna_repository import DNARepository
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(mutant_bp)
    init_db()

    return app


def init_db():
    dna_repository = DNARepository()
    dna_repository.create_table()


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
