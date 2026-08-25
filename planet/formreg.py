_forms = {}


def register(name, form):
    _forms[name] = form
    return form


def get_form(name):
    return _forms.get(name)


def close_all_except(except_name):
    for k, v in list(_forms.items()):
        if k != except_name:
            v.hide()
