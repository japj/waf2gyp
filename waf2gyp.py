""" waf2gyp

    Converts node-waf (wscript) files to node-gyp (binding.gyp)

    The idea is to enough 'stubbed' node-waf code that running a wscript will
    generate information to output a node-gyp file.

"""


def convertBuildContext2Gyp(build):
    """ convert a BuildContext to a GYP dictionary
    """
    assert len(build.all_task_gen), 1

    result = dict(
      targets=[
        dict(
            target_name=build.all_task_gen[0].target,
            sources=[build.all_task_gen[0].source]
        )
      ]
    )
    return result

if __name__ == '__main__':
    import sys
    import json
    import wafstub
    buildContext = wafstub.stubbedRunWscript(sys.argv[1])
    gypDict = convertBuildContext2Gyp(buildContext)
    print json.dumps(gypDict, indent=4)
