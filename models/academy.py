from odoo import models, fields, api


class Academy(models.Model):
    _name = 'academy.course'
    _description ='Academy testing'

    name = fields.Char(string='Nome')
    description = fields.Text(string='Descrisao')
    members = fields.Many2many(
        'res.partner',
        'academy_course_res_partner_rel',
        'course_id',
        'partner_id',
        string='Membros'
    )

    professor_id = fields.Many2one(
        'academy.professor',
        string='Professor',
        ondelete='set null'
    )

