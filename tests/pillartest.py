# load a pillar

input_file = 'pillar.example'
# yaml/jinja

#
from salt.template import compile_template
import salt.loader
import salt
import pprint

from support import Opts

opts=Opts({

    ## minion mods
    'extension_modules' : "",
    'module_dirs' : "",
    'whitelist_modules' : "",

    ## grains
    'skip_grains' : "",
    
    # 'hash_type': 'md5',
    'cachedir' : '/tmp',
    # 'file_client': 'remote',
    # 'transport': 'local',
    # 'jinja_trim_blocks': False,
    # 'jinja_lstrip_blocks': False,
    # 'allow_undefined' :  False,
    # #'__pillar':pillar,
    # 'file_roots' : {
    #     'base' : ["./"]
    # }
})
sls = 'top'
saltevn = 'base'

grains = salt.loader.grains(opts)
pprint.pprint(grains)

## used by the loader

opts['grains']=grains

opts['pillar']={} # empty to start with

#functions = salt.loader.minion_mods(opts)
functions = {}
load = salt.loader._create_loader(
    opts, 'renderers', 'render', ext_type_dirs='render_dirs'
)
rend = load.filter_func('render', {
    'name': 'funk',
    'value': 'test',
})
opts['renderer']="jinja|yaml"

rend2 = salt.loader.render(opts, functions)
saltenv="base"
sls='top.sls'
defaults = {
    'id' : "Funky!",
}
state = compile_template(
    "pillar.example",
    rend2, opts['renderer'], 
    saltenv, sls, _pillar_rend=True, **defaults)

# the results!
print "Results"
pprint.pprint(dict(state.items()))
