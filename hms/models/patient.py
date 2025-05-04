
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import logging
_logger = logging.getLogger(__name__)

class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'
    _rec_name = 'first_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birthdate = fields.Date()
    age = fields.Integer(compute='_compute_age_and_pcr', store=True, readonly=True)
    email = fields.Char()
    image = fields.Binary("Image", attachment=True)
    address = fields.Text()
    blood_type = fields.Selection([
        ('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')
    ])
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=True)
    department_id = fields.Many2one('hms.department')
    doctor_ids = fields.Many2many('hms.doctor')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')
    ], default='undetermined')
    pcr = fields.Boolean()
    cr_ratio = fields.Float()
    history = fields.Text()
    log_history_ids = fields.One2many('hms.log.history', 'patient_id')
    related_patient_id = fields.Many2one('hms.patient', string='Related Patient')



    def print_patient_report(self):
        return self.env.ref('hms.action_report_patient').report_action(self)

    @api.model
    def get_patient_data(self):
        _logger.info(f"Patient Image Data: {self.image}")



    @api.depends('birthdate')
    def _compute_age_and_pcr(self):
        for record in self:
            if record.birthdate:
                today = date.today()
                record.age = today.year - record.birthdate.year - (
                    (today.month, today.day) < (record.birthdate.month, record.birthdate.day)
                )
                record.pcr = record.age > 50
            else:
                record.age = 0
                record.pcr = False

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and self.search_count([('email', '=', record.email), ('id', '!=', record.id)]):
                raise ValidationError("Email must be unique.")

    @property
    def health_logs(self):
        return self.log_history_ids


    