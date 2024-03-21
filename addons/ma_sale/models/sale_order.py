from odoo import api, fields, models



class saleManagement(models.Model):
  _inherit = 'sale.order'
  _description = 'Sale Management'

  test_1 = fields.Char(string='test_1')
  test_2 = fields.Date(string='test_2')
  test_3 = fields.Integer(string='test_3')