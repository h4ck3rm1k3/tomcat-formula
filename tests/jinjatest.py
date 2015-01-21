import salt.renderers.jinja

class Salt:
    class Grains:
        pass

    class Opts(object):

        def __init__(self) :
            self.data={
                'jinja_trim_blocks': False,
                'jinja_lstrip_blocks': False,
                'allow_undefined' :  False,
                'file_roots' : {
                    'base' : "bla"
                }
            }

        def __getitem__(self, x):
            return self.data[x]

        def get(self, item, default):
            print "get item", item
            
            return self.data[item]

    class Pillar:
        pass

    pass

opts=Salt.Opts() 
pillar=Salt.Pillar()
salt.renderers.jinja.__salt__=Salt()
salt.renderers.jinja.__grains__=Salt.Grains()
salt.renderers.jinja.__opts__=opts
salt.renderers.jinja.__pillar__=pillar
opts.data['__pillar']=pillar

context = {
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
}

x= salt.renderers.jinja.render("./tomcat/files/server.xml",
                            saltenv='base', 
                            sls='', 
                            argline='',
                            context=context)
print str(x.getvalue())
