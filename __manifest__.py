{
    'name' : 'Courriel',
    'version' : '1.1',
    'summary': 'Gestion courriel',
    'sequence': 1,
    'description': """
     """,
    'category': 'App',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['base_setup'],
    'data': [
       'security/security.xml',
        'security/ir.model.access.csv',        
        'views/courriel_view.xml',
        'views/autio.xml'

    ],
    'demo': [

    ],
    'qweb': [

    ],
    'application': True

}