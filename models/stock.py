from odoo import api, fields, models, _

class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    def _action_confirm(self, merge=True, merge_into=False):
        print('_action_confirm stock_move learn')
        res = super(StockMoveInherit, self)._action_confirm(merge=merge, merge_into=merge_into)
        return res
