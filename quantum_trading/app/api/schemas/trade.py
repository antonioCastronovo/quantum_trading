from marshmallow import Schema, fields

class TradeSchema(Schema):
    amount = fields.Float()
    symbol = fields.Str()