from odoo import fields, api, tools, models, _


class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order.line"

    partner = fields.Char(string="Partner")

    @api.onchange('product_id')
    def check_partner(self):
        for purchase in self:
            self.partner = purchase.partner_id.name

        product_obj = self.env["product.product"].search([])
        res = {}
        for product in product_obj:
            if product.seller_ids.name.name == self.partner:
                domain = {'product_id': [(product.seller_ids.name.name, '=', self.partner)]}
                return {'domain': domain}
        return res

