from ..models import Employee
from odoo import api, fields, models

class AddCommentWiz(models.TransientModel):
    _name = "add.comment.wizard"
    _description = "Add Comment Wizard"

    update_comment = fields.Text(string="Comment", required=True)

    def update_employee_comment(self):
        print("კომენტარი დამატებულია")

        self.env['swisscapital_employee'].browse(self._context.get("active_ids")).update({'comment': self.update_comment})