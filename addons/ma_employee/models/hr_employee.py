from odoo import api, fields, models



class employeeManagement(models.Model):
  _inherit = 'hr.employee'
  _description = 'Employee Management'

  test_1 = fields.Char(string='Test_1')
  test_2 = fields.Float(string='Test_2')
  test_3 = fields.Date(string='Test_3')
  test_4 = fields.Datetime(string='Test_4')
  test_5 = fields.Integer(string='Test_5')
  test_6 = fields.Selection([('new','New'),('done','Done'),('cancel','Canceld'),('reject','Rejected'),],string='Test_')
