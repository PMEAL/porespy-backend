# funcnames.py is concerned about any comprehensive metadata fetching from the porespy library itself.
# e.g. The PoreSpyFuncsNames model obtains the parameters and default values for each module in porespy.

from django.db import models
import inspect
import porespy as ps
import json

class PoreSpyFuncsNames(models.Model):
    @property
    def porespy_funcs(self):
        def return_arg_names_vals_and_types(f):
            s = inspect.signature(f)
            js = {}
            for item in s.parameters.keys():
                if item == 'shape':
                    js.update({'shape[0]': {'value': 100, 'type': 'int', 'required': True},
                               'shape[1]': {'value': 100, 'type': 'int', 'required': True},
                               'shape[2]': {'value': '', 'type': 'int', 'required': False}})
                else:
                    p = s.parameters[item]
                    info = {}
                    try:
                        info['value'] = json.dumps(p.default)
                        info['required'] = True
                    except TypeError:  # Means there is no default value
                        info['value'] = ''
                        info['required'] = False

                    dtype = p.annotation

                    if dtype is inspect._empty:
                        info['type'] = json.dumps(None)
                    elif hasattr(dtype, '__name__'):
                        info['type'] = dtype.__name__
                    else:
                        info['type'] = str(p.annotation)
                    js.update({item: info})
            return js

        func_details = {
            "filters": {},
            "generators": {},
            "io": {},
            "metrics": {},
            "networks": {}
        }

        def porespy_modules_populate(modules, module_strs):
            for i in range(len(modules)):
                for func in dir(modules[i]):
                    if not func.startswith('__'):
                        f = getattr(modules[i], func)
                        func_details[module_strs[i]][func] = return_arg_names_vals_and_types(f)

        # Currently, ps.networks is throwing an error and cannot be populated through the porespy_modules_populate function.
        # Will need to look into this further.
        modules = [ps.filters, ps.generators, ps.io, ps.metrics]
        modules_strs = ['filters', 'generators', 'io', 'metrics']
        porespy_modules_populate(modules, modules_strs)
        return func_details

