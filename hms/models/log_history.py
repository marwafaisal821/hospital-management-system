from odoo import models, fields

class LogHistory(models.Model):
    _name = 'hms.log.history'
    _description = 'Log History'

    patient_id = fields.Many2one('hms.patient', string="Patient", required=True)
    create_date = fields.Datetime(string="Creation Date", readonly=True)
    created_by = fields.Many2one('res.users', string="Created By", default=lambda self: self.env.user, readonly=True)
    description = fields.Text(string="Description")


