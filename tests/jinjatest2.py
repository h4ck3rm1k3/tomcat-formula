import salt.renderers.jinja
import support
grains=support.Grains()

pillar=support.Pillar()
tomcat = support.TomCat()
salt.renderers.jinja.__salt__={
    'pillar.get' : pillar.get,
    'grains.filter_by' : grains.filter_by,
}

salt.renderers.jinja.__pillar__=pillar
salt.renderers.jinja.__grains__=grains

opts=support.Opts({
    'hash_type': 'md5',
    'cachedir' : '/tmp',
    'file_client': 'remote',
    'transport': 'local',
    'jinja_trim_blocks': False,
    'jinja_lstrip_blocks': False,
    'allow_undefined' :  False,
    '__pillar':pillar,
    'file_roots' : {
        'base' : ["./"]
    }
})

salt.renderers.jinja.__opts__=opts
if 'transport' in opts:
    ttype = opts['transport']


context = {
    'user':  'someuser',
    'passwd':  'password',
    'SSLEnabled': True,
    'port': 8080,
    'protocol': 'https',
    'connectionTimeout': 50,
    'URIEncoding' : None,
    'maxHttpHeaderSize' : 1024,
    'maxThreads' : 800,
    'enableLookups' : False, 
    'disableUploadTimeout' : False,
    'acceptCount' : 1,
    'scheme' : 'help',
    'secure' : False,
    'clientAuth': None,
    'sslProtocol' : None,
    'keystoreFile' : '/tmp/g',
    'keystorePass' : '123',
    'tomcat' : {
        "native": False
    }
    
}

for fn in [
        'tomcat/init.sls',
        'tomcat/native.sls',
        'tomcat/package.sls',
        'tomcat/vhosts.sls',
        'tomcat/map.jinja',
        'tomcat/manager.sls',
        'tomcat/ssl.sls',               
        'tomcat/files/tomcat-users.xml',
        "tomcat/files/server.xml",
        ]:
    print "Processing", fn
    x= salt.renderers.jinja.render(
        "./" + fn,
        saltenv='base', 
        sls='', 
        argline='',
        context=context,
        tmplpath='./'
    )
    if x :
        print str(x.getvalue())
    else:
        print "NO Data"
