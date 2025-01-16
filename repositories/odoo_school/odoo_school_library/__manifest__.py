{
    'name': 'Odoo School Library',
    'version': '17.0.1.0.0',
    'author': 'Odoo School',
    'website': 'https://odoo.school/',
    'category': 'Customizations',
    'license': 'OPL-1',

    'depends': [
        'base',
    ],

    'external_dependencies': {
        'python': [],
    },

    'data': [
        'views/odoo_school_library_menu.xml',
        'views/odoo_school_library_book_views.xml'
    ],

    'demo': [

    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png'
    ],
}
