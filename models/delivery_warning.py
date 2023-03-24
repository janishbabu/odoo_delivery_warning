from odoo import models, fields


class DeliveryWarning(models.Model):
    _inherit = "sale.order"

    delivery = fields.Boolean(help="Deliver Order at Sale Order")


class Delivery(models.Model):
    _inherit = "stock.picking"

    delivery_warning = fields.Boolean(related="sale_id.delivery")
