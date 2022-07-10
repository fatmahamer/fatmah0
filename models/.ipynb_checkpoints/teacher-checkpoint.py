from odoo import api, fields, models


class ScoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "School teacher"

    name = fields.Char(string='Teacher Name', required=True)
    student_name = fields.Many2one('school.student', string="student", required=True)
   
    age = fields.Integer(string=' age', tracking=True)
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    homework = fields.Text(string='Homework')
    
  