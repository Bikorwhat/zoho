# -*- coding: utf-8 -*-

{
    'name': 'CRM Extension Stage',
    'category': 'CRM',
    'summary': 'A module for managing leads stages',
    'description': '''
        This module provides functionality for managing crm leads stages.
    ''',
    'author': 'Amniltech Team',
    'depends': [
        'base_setup',
        'crm',
    ],
    'data': [
        'data/crm_stage_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
