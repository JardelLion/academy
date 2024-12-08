from odoo import models, fields

class AcademyProfessor(models.Model):
    _name = 'academy.professor'
    _description = 'Professor da Academia'

    name = fields.Char(string='Nome', required=True)
    expertise = fields.Char(string='Especialidade')
    course_ids = fields.One2many(
        'academy.course',
        'professor_id',
        string='Cursos Ministrados'
    )