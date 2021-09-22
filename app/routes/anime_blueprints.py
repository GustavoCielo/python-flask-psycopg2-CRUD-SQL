from flask import Flask, Blueprint
from app.controllers.animes_controller import get_animes, get_animes_by_id, create_animes, delete, update



bp_animes = Blueprint('animes', __name__, url_prefix='/animes')


bp_animes.post('')(create_animes)
bp_animes.get('')(get_animes)
bp_animes.get('/<int:anime_id>')(get_animes_by_id)
bp_animes.patch('/<int:anime_id>')(update)
bp_animes.delete('/<int:anime_id>')(delete)