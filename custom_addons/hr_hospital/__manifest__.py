{
    'name': 'Hospital Management',
    'version': '1.0',
    'category': 'Hospital',
    'author': 'Niktia Chernetskyi',
    'summary': 'Module for Hospital Management',
    'description': 'This module manages doctors, patients,\
     diseases, and visits.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'data/master_data.xml',
    ],
    'demo': ['data/demo_data.xml'],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
}
