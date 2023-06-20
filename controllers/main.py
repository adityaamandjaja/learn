from odoo import http
from odoo.http import request


class OdooProvider(http.Controller):

    # masih belom jalan
    @http.route('/learn/get_stock', type='json', auth='user')
    def get_stock(self, **kwargs):
        res = request.env['stock.quant'].get_quant_data()
        return {
            'return': res,
        }
