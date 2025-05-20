# -*- coding: utf-8 -*-

from odoo import models, fields


class ProjectTaskCustomStage(models.Model):
    _name = 'project.task.custom.stage'
    _description = 'Project Task Custom Stage'
    _order = 'sequence asc'

    sequence = fields.Integer('Sequence')
    name = fields.Char('Stage Name', required=True)
