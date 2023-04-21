{
    'name': "Visitas",
    'version': '1.0',
    'depends': ['base'],
    'author': "sie",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/visitas_views.xml',
        'views/habitaciones_views.xml',
        'views/visitas_menus.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        
    ],
    'application':True
}