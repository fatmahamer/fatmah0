from odoo import api, fields, models


class ScoolStudent(models.Model):
    _name = "school.student"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "School Student"

    name = fields.Char(string=' Name', required=True)
    
    teacher_name = fields.Many2one('school.teacher', string="teacher", required=True)
#     reference = fields.Char(string='Reference', required=True, copy=False, readonly=True )
#     default=lambda self: _('New')
    image = fields.Binary(string="Student Imge")
   
    age = fields.Integer(string=' age', tracking=True)
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    
    
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status", tracking=True)
   
    responsible_id = fields.Many2one('res.partner', string="Responsible" )

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
             vals['reference'] = self.env['ir.sequence'].next_by_code('school.student', sequence_date=seq_date) or _('New')
        res = super(ScoolStudent, self).create(vals)
        return res