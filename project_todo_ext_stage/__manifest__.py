# -*- coding: utf-8 -*-

{
    'name': 'To-do Extension Stage',
    'category': 'To-Do',
    'summary': 'A module for managing to-do stages',
    'description': '''
        This module provides functionality for managing to-do leads stages.
    ''',
    'author': 'Amniltech Team',
    'depends': [
        'base_setup',
        'project_todo',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/project_task_custom_stage_data.xml',
        'views/project_task.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}

