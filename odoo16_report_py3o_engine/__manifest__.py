{
    "name": "Py3o Report Engine",
    "summary": "Reporting engine based on Libreoffice (ODT -> ODT, "
    "ODT -> PDF, ODT -> DOC, ODT -> DOCX, ODS -> ODS, etc.)",
    "version": "16",
    "category": "Reporting",
    "author": "XCG Consulting," "ACSONE SA/NV," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/reporting-engine",
    "depends": ["base", "web","account","sale"],
    "external_dependencies": {
        "python": ["py3o.template", "py3o.formats"],
        "deb": ["libreoffice"],
    },
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/py3o_template.xml",
        "views/ir_actions_report.xml",
        "demo/report_py3o.xml",
    ],

    "assets": {
        "web.assets_backend": [
            "report_py3o/static/src/js/py3o_action_manager.esm.js",
        ]
    },
    "installable": True,
}
