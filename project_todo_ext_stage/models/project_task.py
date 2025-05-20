# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _inherit = 'project.task'

    custom_stage_id = fields.Many2one('project.task.custom.stage', string='Stages')

    @api.model
    def _read_group_custom_stage_id(self, records, domain, order=None):
        return records.search([])
