# -*- coding: utf-8 -*-
{
    'name': 'Plant Nursery',
    'version': '1.0',
    'summary': 'Take Care Of Plants',
    'sequence': -101,
    'description': """Take Care Of Plants""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/nursery_views.xml',
        'views/nursery_order_views.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
