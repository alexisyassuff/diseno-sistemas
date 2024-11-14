from flask import Blueprint, request, jsonify
from services.mutant_service import Mutante
from repositories.dna_repository import DNARepository

mutant_bp = Blueprint('mutant', __name__)


@mutant_bp.route('/mutant/', methods=['POST'])
def detect_mutant():
    data = request.get_json()
    dna = data.get("dna", [])

    response = process_dna(dna)

    if isinstance(response, tuple):
        return response
    return jsonify({"error": "An unexpected issue occurred"}), 500


def process_dna(dna):
    if not isinstance(dna, list):
        return jsonify({"error": "DNA data must be provided as a list"}), 400

    if len(dna) != 6:
        return jsonify({"error": "DNA data must have exactly 6 sequences"}), 400

    for row in dna:
        if not isinstance(row, str):
            return jsonify({"error": "Each DNA sequence should be a string"}), 400
        if len(row) != 6:
            return jsonify({"error": "Each DNA sequence must be 6 characters long"}), 400

    dna_repository = DNARepository()

    if dna_repository.obtener_adn(dna):
        return jsonify({"message": "This DNA has already been analyzed"}), 200

    mutante_checker = Mutante(dna)
    is_mutant = mutante_checker.isMutante()

    dna_repository.save_result(dna, is_mutant)

    if is_mutant:
        return jsonify({"message": "Mutant DNA detected"}), 200
    else:
        return jsonify({"message": "Human DNA detected"}), 403
