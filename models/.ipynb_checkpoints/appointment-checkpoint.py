from odoo import api, fields, models


class SchoolAppointment(models.Model):
    _name = "school.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "school appointment"

    name = fields.Char(string=' Order Reference', required=False, copy=False, readonly=True )
#     default=lambda self: _('New')

    age = fields.Integer(string='Age', related='student_id.age', tracking=True)

    student_id = fields.Many2one('school.student', string="Student",  required=True)  
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status", tracking=True)
   

    note = fields.Text(string='Description')
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check up Time")
    

    def action_confirm(self):
        self.state = 'confirm'
        
    def action_done(self):
        self.state = 'done' 
        
        
    def action_draft(self):
        self.state = 'draft'
    
    def action_cancel(self):
        self.state = 'cancel'
        
    @api.model
    def create(self, vals):
        if not vals.get('note'):
             vals['note'] = 'New Student'
#              vals['reference'] = self.env['ir.sequence'].next_by_code('school.appointment') or _('New')
        res = super(SchoolAppointment, self).create(vals)
        return res
    
    
    @api.onchange('student_id')
    def onchange_student_id(self):
        if self.student_id:
            if self.student_id.gender:
                self.gender = self.student_id.gender