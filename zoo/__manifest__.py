# -*- coding: utf-8 -*-
{
    'name': "Zoo",
    'summary': "Gestión de zoológico",
    'description': """
Módulo para gestionar un zoológico con los modelos Animal, Cuidador y Espacio.
""",
    'author': "Tu Nombre / Empresa",
    'website': "https://www.tuweb.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'installable': True,
    'application': True,
}
