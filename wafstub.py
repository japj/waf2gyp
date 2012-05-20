""" wafstub

    This module contains all the stubbed waf code
"""
bld = None
"singleton - safe to use when Waf is not used as a library"


class BuildContext(object):
    def __init__(self):
        # not a singleton, but provided for compatibility
        global bld
        bld = self

        self.all_task_gen = []

    def new_task_gen(self, *k, **kw):
        ret = task_gen(*k, **kw)
        return ret


class task_gen(object):
    def __init__(self, *kw, **kwargs):
        self.target = ''
        self.source = ''
        self.bld = kwargs.get('bld', bld)

        self.features = list(kw)

        for key, val in kwargs.iteritems():
            print key, val
            setattr(self, key, val)

        self.bld.all_task_gen.append(self)


def stubbedRunWscript(filePath):
    """ Run the wscript in a stubbed environment and return the BuildContext
    """
    wscriptGlobals = {}
    wscriptLocals = {}
    execfile(filePath, wscriptGlobals, wscriptLocals)
    # wscriptLocals will contain the 'module' wscript functions

    build = BuildContext()
    # run the build step of the wscript
    wscriptLocals["build"](build)

    return build
