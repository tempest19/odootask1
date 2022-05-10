{
    'name': 'SwissCapital Management',
    'version': '1.0',
    'category': 'swisscapital tasks',
    'author': 'Giorgi',
    'website': 'https://www.google.com',
    'license': 'AGPL-3',
    'summary' : 'Management Software',
    'sequence': -100,
    'description': """Management Software""",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/employee.xml',
        'views/department.xml',
        'views/characteristics.xml',
    ],
    'demo' : [],
    'qweb' : [],
    'installable' : True,
    'application' : True,
    'auto_install': False
}
