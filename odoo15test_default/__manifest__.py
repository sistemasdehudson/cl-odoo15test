{
    'name': 'odoo15test',
    'version': '15.0.0.0',
    'category': 'Tools',
    'summary': "Proyecto odoo15test",
    'author': 'Sdeh',
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',
    #'dbfilter': 'sat26-01-2022',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/sistemasdehudson/cl-odoo15test.git',
        'https://github.com/regaby/odoo-custom.git -b 15.0-adhoc',
        'https://github.com/regaby/l10n_ar_fe_qr ctmil/l10n_ar_fe_qr -b 15.0',
        #'https://github.com/regaby/sdeh-pos.git',
        #'https://github.com/jobiols/odoo-addons.git',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git -b 15.0',
        'https://github.com/ingadhoc/odoo-argentina-ce.git -b 15.0',
        'https://github.com/ingadhoc/argentina-sale.git -b 15.0',
        'https://github.com/ingadhoc/account-payment.git -b 15.0',
        'https://github.com/ingadhoc/account-invoicing.git -b 15.0',
        'https://github.com/ingadhoc/account-financial-tools.git -b 15.0',
        'https://github.com/ingadhoc/sale.git -b 15.0',
        'https://github.com/ingadhoc/stock.git -b 15.0',
        'https://github.com/ingadhoc/aeroo_reports.git -b 15.0',
        'https://github.com/ingadhoc/website.git -b 15.0',
        'https://github.com/OCA/account-financial-reporting.git -b 15.0',
        'https://github.com/OCA/reporting-engine.git -b 15.0',
        'https://github.com/OCA/server-ux.git -b 15.0',
        'https://github.com/OCA/mis-builder.git -b 15.0',
        'https://github.com/OCA/sale-workflow.git -b 15.0',
        'https://github.com/OCA/web.git -b 15.0',
        ##
        'https://github.com/OCA/contract.git -b 15.0',
        #'https://github.com/CybroOdoo/CybroAddons.git',
        #'https://github.com/itpp-labs/pos-addons.git',
        'https://github.com/odoomates/odooapps.git -b 15.0',
        #'https://github.com/sistemasdehudson/sdehposaddons.git',
        'https://github.com/OCA/manufacture.git -b 15.0',
        'https://github.com/OCA/manufacture-reporting.git -b 15.0',
        'https://github.com/OCA/helpdesk -b 15.0',
        'https://github.com/OCA/pos.git -b 15.0',
        'https://github.com/OCA/report-print-send.git -b 15.0',
    ],

    'docker-images': [
        'odoo regaby/odoo-ce:15.0',
        'postgres postgres:10.1-alpine',
        #'nginx nginx'
    ]
}
