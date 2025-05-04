from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient', string="Related Patient")
    website = fields.Char()
    vat = fields.Char(required=True)

    @api.constrains('email', 'related_patient_id')
    def _check_unique_email(self):
        for record in self:
            if record.email and record.related_patient_id:
                existing = self.env['res.partner'].search([
                    ('email', '=', record.email),
                    ('id', '!=', record.id)
                ])
                if existing:
                    raise ValidationError("This email is already assigned to another customer. Please use a unique email.")

    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise ValidationError("You cannot delete a customer linked to a patient.")
        return super(ResPartner, self).unlink()
