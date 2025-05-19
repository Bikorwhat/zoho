from odoo import models, fields,api
class CrmSource(models.Model):
    _name = 'zoho_crm.source'
    _description = 'Lead Source'

    name = fields.Char(string="Source Name", required=True)

class CrmIndustry(models.Model):
    _name = 'zoho_crm.industry'
    _description = 'Industry Type'

    name = fields.Char(string="Industry Name", required=True)

class CrmRating(models.Model):
    _name = 'zoho_crm.rating'
    _description = 'Rating Type'

    name = fields.Char(string="Rating Name", required=True)

class CrmStatus(models.Model):
    _name = 'zoho_crm.status'
    _description = 'Status Type'

    name = fields.Char(string="Status Name", required=True)
