from odoo import models, fields,api
from odoo.exceptions import UserError
import re

class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    industry_id = fields.Many2one('zoho_crm.industry', string='Industry', default=lambda self: self.env.ref('zoho_crm_extend.ind_none'))
    lead_source = fields.Many2one('zoho_crm.source', string='Source', default=lambda self: self.env.ref('zoho_crm_extend.source_none'))
    lead_status = fields.Many2one('zoho_crm.status', string='Status', default=lambda self: self.env.ref('zoho_crm_extend.status_none'))
    rating = fields.Many2one('zoho_crm.rating', string='Rating', default=lambda self: self.env.ref('zoho_crm_extend.rating_none'))
    
    # Change to Float field with compute method
    annual_revenue_input = fields.Char(
        string='Annual Revenue',
        help='Enter a number or simple mathematical expression (e.g., 1000+500, 2000-500)'
    )
    annual_revenue = fields.Monetary(
        string='Total Annual Revenue',
        currency_field='currency_id',
        compute='_compute_annual_revenue',
        store=True
    )

    @api.depends('annual_revenue_input')
    def _compute_annual_revenue(self):
        for record in self:
            if record.annual_revenue_input:
                try:
                    # Clean the input
                    expr = ''.join(c for c in record.annual_revenue_input if c.isdigit() or c in '+-*/.()') 
                    # Evaluate
                    result = float(eval(expr, {'__builtins__': {}}, {}))
                    record.annual_revenue = result
                except:
                    record.annual_revenue = 0.0
            else:
                record.annual_revenue = 0.0

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id.id,
        required=True
    )
    @api.onchange('annual_revenue')
    def _evaluate_annual_revenue_expression(self):
        for record in self:
            if isinstance(record.annual_revenue, str):
                # Remove all spaces from the string
                expr = record.annual_revenue.replace(' ', '')
                
                # Check if it's a valid mathematical expression
                if re.match(r'^[\d+\-*/().]+$', expr):
                    try:
                        result = eval(expr)
                        if isinstance(result, (int, float)):
                            record.annual_revenue = float(result)
                    except Exception:
                        raise UserError("Invalid mathematical expression. Please check your input.")
                else:
                    raise UserError("Only numbers and basic mathematical operators (+, -, *, /) are allowed.")
    
    no_of_employees = fields.Integer(string="Number of Employees")  # Number of Employees field
    website = fields.Char(string="Website")  # Website field

    # Email Opt-Out Field
    email_opt_out = fields.Boolean(string="Email Opt Out")
    social_lead_id=fields.Char(string="Social Lead ID")
    secondary_email=fields.Char(string="Secondary Email")
    twitter=fields.Char(string="Twitter")
    desc= fields.Text(string="Description")
