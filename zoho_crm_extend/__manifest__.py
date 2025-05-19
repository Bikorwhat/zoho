# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'zoho_crm_extend',
    'version': '1.3',
    'summary': 'Zoho crm extend',
    'sequence': 10,
    'description': """
    Zoho CRM Extend""",
    'category': 'Accounting/Accounting',
    'depends': ['base_setup', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/field_data.xml',
        'views/crm_zoho.xml',
        'views/field_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
