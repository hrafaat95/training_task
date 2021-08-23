from odoo import _, api, fields, models, modules, tools

class PurchaseOrderCountPerPartner(models.Model):
    _name = 'purchase.order.count.per.partner'
    _auto = False

    partner_id = fields.Many2one('res.partner', string="Partner")
    total_purchase_order = fields.Integer("Total Purchase Order")
    total_cost = fields.Float("Total cost")


    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute('''
            CREATE OR REPLACE VIEW %s AS (
            select  partner_id as id , partner_id as partner_id, count(partner_id) as total_purchase_order , sum(amount_total) as total_cost from purchase_order GROUP BY partner_id
            )''' % (self._table,)
        )

