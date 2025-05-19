from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    record_type = fields.Selection([
        ('lead', 'Lead'),
        ('contact', 'Contact'),
    ], string="Type")

    lead_id = fields.Many2one('crm.lead', string="Lead",domain="[('type', '=', 'lead')]")
    contact_id = fields.Many2one('res.partner', string="Contact")

    contact_related_type = fields.Selection([
        # ('account', 'Account'),
        ('sale_order', 'Sale Order'),
        ('quotation', 'Quotation'),
        ('invoice', 'Invoice'),
        ('opportunity', 'Opportunity'),
    ], string="Contact Related To")

    # Related record fields
    # account_id = fields.Many2one('res.partner', string="Account")
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    quotation_id = fields.Many2one('sale.order', string="Quotation")
    invoice_id = fields.Many2one('account.move', string="Invoice")
    opportunity_id = fields.Many2one('crm.lead', string="Opportunity",domain="[('partner_id', '=', contact_id),('type', '=', 'opportunity')]")

    @api.onchange('record_type')
    def _onchange_record_type(self):
        if self.record_type == 'lead':
            self.contact_id = False
            self.contact_related_type = False
            # self.account_id = False
            self.sale_order_id = False
            self.quotation_id = False
            self.invoice_id = False
            self.opportunity_id = False
        elif self.record_type == 'contact':
            self.lead_id = False

    @api.onchange('contact_related_type', 'contact_id')
    def _onchange_contact_related_type(self):
        # self.account_id = False
        self.sale_order_id = False
        self.quotation_id = False
        self.invoice_id = False
        self.opportunity_id = False
        