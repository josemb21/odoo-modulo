{
    'name': "MegaMarket",
    'summary': "Gestión de electrodomésticos y clientes",
    'description': """
        Módulo para gestionar la venta de electrodomésticos y artículos de electrónica.
        Incluye gestión de clientes y productos.
    """,
    'author': "Tu Nombre o Empresa",
    'website': "https://www.yourcompany.com",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
      
    ],
    'installable': True,
    'application': True,
}
