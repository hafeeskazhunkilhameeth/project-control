from project_control.data import validate_project_costing


def validate(invoice, method):
    for item in invoice.items:
        validate_project_costing(item.project, item.amount)
