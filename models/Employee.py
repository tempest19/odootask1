from datetime import datetime
from datetime import date
from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Employees(models.Model):
    _name = "swisscapital_employee"
    _description = "Employee"
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    full_name = fields.Char(string="Full Name", compute="get_fullname")
    home_town = fields.Char(string="Home Town")
    date_of_birth = fields.Date(string='Date of birth')
    age = fields.Integer(string="Age", compute='_compute_age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string="Gender", default='male')
    id_number = fields.Char(string="ID Number")
    date_of_card_creation = fields.Date(string="Date of card creation")
    card_number = fields.Char(string="Card number")
    image = fields.Binary(string="Employee Photo")
    place_of_birth = fields.Char(string="Place of Birth")
    card_issuing_organization = fields.Char(string="Card issuing organization")
    signature = fields.Binary(string="Employee signature")
    good_thru = fields.Date(string="Card good thru")
    department = fields.Many2one("swisscapital.department", string="Department")
    characteristics = fields.Many2many("swisscapital.characteristics", string="Characteristics")
    comment = fields.Text(string="კომენტარი", readonly=True)
    user_id = fields.Many2one('res.users', string='Responsible')

    _sql_constraints = [
        ('unique_id_number', 'unique (id_number)', 'ID number must be unique.'),
        ('unique_card_number', 'unique (card_number)', 'Card number must be unique.')
    ]


    def get_fullname(self):
        for record in self:
            record.full_name = record.first_name + " " + record.last_name

    @api.constrains('date_of_birth')
    def _compute_age(self):
        for record in self:
            bdate = datetime.strptime(record.date_of_birth, '%Y-%m-%d').date()
            today = date.today()
            if record.date_of_birth:
                record.age = str(int((today - bdate).days / 365))
            else:
                record.age = 0

            if record.age < 18:
                raise ValidationError(("მომხმარებელი არ არის სრულწლოვანი!"))

    @api.constrains('date_of_card_creation', 'good_thru')
    def created_card_limit(self):
        for record in self:
            today = date.today()
            card_created = datetime.strptime(record.date_of_card_creation, '%Y-%m-%d').date()
            valid_thru = datetime.strptime(record.good_thru, '%Y-%m-%d').date()
            if (today - card_created).days > 3652.5:
                raise ValidationError(("ბარათს მოქმედების ვადა გაუვიდა!"))
            if (valid_thru - card_created).days > 3652.5:
                raise ValidationError(("ბარათის მოქმედების ვადასა და ბარათის შექმნის თარიღს შორის სხვაობა უნდა იყოს მაქსიმუმ 10 წელი"))

    @api.constrains('id_number')
    def check_id(self):
        for record in self:
            if len(record.id_number) != 11 :
                raise ValidationError(("ჩანაწერი არ ემთხვევა პირადი ნომრის ფორმატს(სიმბოლოების რ-ობა უნდა შეადგენდეს 11-ს)"))
            if record.id_number.isdigit():
                pass
            else:
                raise ValidationError(("ჩანაწერი არ ემთხვევა პირადი ნომრის ფორმატს(შეიყვანეთ მხოლოდ ციფრები!)"))

    def add_comment(self):

        return {'type': 'ir.actions.act_window',
                'res_model': 'add.comment.wizard',
                'view_mode': 'form',
                'target': 'new'}







