from marshmallow import Schema, fields

class AssetSchema(Schema):
    id = fields.Int()
    symbol = fields.Str()