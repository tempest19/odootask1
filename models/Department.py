from odoo import fields, models, api

class Department(models.Model):
    _name = "swisscapital.department"
    _description = "Department"

    name = fields.Char(string='Name')
    description = fields.Text(string='Description
