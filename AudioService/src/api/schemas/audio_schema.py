from flask_marshmallow import Marshmallow

ma = Marshmallow()


class AudioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'bpm')
    _links = ma.Hyperlinks({
        'self': ma.URLFor('get_user', id='<id>'),
        'collection': ma.URLFor('get_users')
    })