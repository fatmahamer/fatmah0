
{
    
    
    'name': "School Manegment",
    'version': '1.0',
    'summary': "School Manegment",
    'sequnce': 10,
    'description': """School Manegment Softwer """,
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': ['sale','mail','website_slides','hr'],
    'data': [ 
    'data/data.xml', 
    'views/primary.xml',
    'views/appointment.xml',
    'views/gender.xml',
     'views/teacher.xml',
    'views/student.xml',
    'views/sale.xml',
   'security/ir.model.access.csv'
    ],
    'demo': [],
    'qweb':[],
    'installable': True,
    'appliction': True,
    'auto_install': False,
}
