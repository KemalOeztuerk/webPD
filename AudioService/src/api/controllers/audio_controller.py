from flask import Flask ,request
from src.api.models.audio import Audio, db
from src.api.schemas.audio_schema import AudioSchema

app = Flask(__name__ )
URI = "/api/v1.0/audios"

audio_schema = AudioSchema()


class AudioController:

    @staticmethod
    @app.route(URI, methods=['GET'])
    def get_audios():
        all_audios = Audio.query.all()
        return audio_schema.dump(all_audios)# implement pagination afterward

    @staticmethod
    @app.route(URI+"/<int:id>", methods=["GET"])
    def get_audio(id):
        single_audio = Audio.query.get(id)
        return audio_schema.dump(single_audio)

    @staticmethod
    @app.route(URI, methods=['POST'])
    def post_audio():
        data = request.get_json()
        new_audio = Audio(
            name=data['name'],
            bpm=data['bpm'],
            file_path="filepath/31",
            length = 10000
        )
        db.session.add(new_audio)
        db.session.commit()
        return audio_schema.dump(new_audio)

    @staticmethod
    @app.route(URI+"/<int:id>", methods=['PUT'])
    def put_audio(id):
        pass

    @staticmethod
    @app.route(URI+"/<int:id>",methods=['DELETE'])
    def delete_audio(id):
        pass


