from odoo import fields, models, api

class Characteristics(models.Model):
    _name = "swisscapital.characteristics"
    _description = "Characteristics"

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
