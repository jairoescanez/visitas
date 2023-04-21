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
        'views/visitas_views.xml',
        'security\ir.model.access.csv'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        
    ],
    'application':True
}