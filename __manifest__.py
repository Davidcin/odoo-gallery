# -*- coding: utf-8 -*-
{
    'name' : 'Gallery',
    'version' : '1.0',
    'summary': 'Images in the galleries',
    'sequence': -199,
    'description': "With this module you can add images in the galleries.",
    'category': 'Productivity',
    'website': 'https://github.com/Davidcin',
    'images' : ['icon.png'],
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/gallery.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}