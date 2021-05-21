from odoo import api, fields, models
from odoo.exceptions import UserError


class Plants(models.Model):
    _name = 'nursery.plant'

    name = fields.Char("Plant Name")
    price = fields.Float()
    order_ids = fields.One2many("nursery.order", "plant_id", string="Orders")
    order_count = fields.Integer(compute='_compute_order_count',
                                 store=True,
                                 string="Total Sold")
    number_in_stock = fields.Integer()
    image = fields.Binary("Plant Image", attachment=True)

    @api.constrains('order_count', 'number_in_stock')
    def _check_available_in_stock(self):
        for plant in self:
            if plant.number_in_stock and plant.order_count > plant.number_in_stock:
                raise UserError("There is only %s %s in stock but %s were sold" % (plant.number_in_stock, plant.name,
                                                                                   plant.order_count))

    @api.depends('order_ids')
    def _compute_order_count(self):
        for plant in self:
            plant.order_count = len(plant.order_ids)


class Customer(models.Model):
    _name = "nursery.customer"

    name = fields.Char("Customer Name", required=True)
    email = fields.Char(help="to receive the newsletter")


class Order(models.Model):
    _name = "nursery.order"

    name = fields.Datetime(default=fields.Datetime.now())
    plant_id = fields.Many2one("nursery.plant", required=True)
    customer_id = fields.Many2one("nursery.customer")
    state = fields.Selection([
        ("draft", "Draft"),
        ("confirm", "Confirm"),
        ("cancel", "Cancel")
    ], default="draft")
    last_modification = fields.Datetime(readonly=True)

    def write(self, values):
        # helper to "YYYY-MM-DD"
        values["last_modification"] = fields.Datetime.now()

        return super(Order, self).write(values)

    def unlink(self):
        # self is a record set
        for order in self:
            if order.state == 'confirm':
                raise UserError("You Cannot Delete Confirmed Orders!")

        return super(Order, self).unlink()
