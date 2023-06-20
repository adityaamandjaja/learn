from odoo import api, fields, models, _


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    x_check_x = fields.Boolean(string='Check X')
    x_check_y = fields.Boolean(string='Check Y')
    # x_check_z = fields.Boolean(string='Check Z')


class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    def _action_confirm(self, merge=True, merge_into=False):
        print('_action_confirm stock_move learn')
        res = super(StockMoveInherit, self)._action_confirm(merge=merge, merge_into=merge_into)
        return res


class StockQuantInherit(models.Model):
    _inherit = 'stock.quant'

    def get_quant_data(self):
        print('masuk get_data stock_quant')
        return True
