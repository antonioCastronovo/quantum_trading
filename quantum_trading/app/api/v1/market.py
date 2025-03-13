from flask_restx import Resource, Namespace

market_ns = Namespace('market')

@market_ns.route('/data')
class MarketData(Resource):
    def get(self):
        return {"data": [100, 101, 99]}