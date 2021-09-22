from flask import Flask, jsonify, request
from app.models.anime_model import Anime
from psycopg2.errors import UniqueViolation

def create_animes():
    data = request.get_json()
    try:
        anime = Anime(**data)
        new_anime = anime.create_animes()

        return new_anime, 201
    except TypeError as e:
        return {"available keys": [
            "anime",
            "released_date",
            "seasons"
        ],
            "Wrong keys sent": str(e)
        }, 422
    except UniqueViolation as e:
        return {
            "error": "anime already exists"
        }, 422    


def get_animes():
    animes = Anime.get_animes()
    return jsonify(animes), 200


def get_animes_by_id(anime_id):
    try:
        anime = Anime.get_animes_by_id(anime_id)
        return anime, 200
    except TypeError as e:
        return {}, 404


def update(anime_id):
    data = request.get_json()
    try:
        updated_anime = Anime.update(anime_id, data)
        
        return updated_anime, 200
    except TypeError as e:
        return {"available keys": [
            "anime",
            "released_date",
            "seasons"
        ],
            "Wrong keys sent": str(e)
        }, 422


def delete(anime_id):
    try:
        deleted_anime = Anime.delete(anime_id)
        return 204
    except TypeError:
        {"error": "Not Found"}, 404
