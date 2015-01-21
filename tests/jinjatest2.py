import salt.renderers.jinja

class Salt:

    class Grains:
        def filter_by(self,x=None, merge=None, c=None):
            print "Filterby",x, merge, c
            return x['Debian']

    # class Opts(object):
    #     def __init__(self) :
    #         self.data={
    #             'file_client': 'remote',
    #             '0': 'what',
    #             'transport': 'local',
    #             'jinja_trim_blocks': False,
    #             'jinja_lstrip_blocks': False,
    #             'allow_undefined' :  False,
    #             'file_roots' : {
    #                 'base' : "bla"
    #             }
    #         }
    #     def __getitem__(self, x):
    #         if isinstance(x,int):
    #             return "What?"
    #         print "opts get item", x
    #         if x in self.data:
    #             return self.data[x]
    #         else:
    #             raise Exception("Missing {0}".format(x))
    #             print "adding", x
    #             return "unknown"
    #     def get(self, item, default):
    #         print "get item", item            
    #         return self.data[item]

    class Pillar:
        def __init__(self):
            self.data = {
                'tomcat:sites' : { "funky"  : "cold"}       ,
                'tomcat:version' : 5,
                'tomcat:lookup' : True,
                'java:home' : '/usr',
                'java:Xmx': '3G',
                'java:MaxPermSize': '256m',
                'java:UseConcMarkSweepGC' : False,
                'java:CMSIncrementalMode' : False,
                'tomcat:security' : True,
                'limit:soft' : True, 

            }

        def get(self,x, default=None):
            print "Pillar.get key='{0}' default='{1}'".format(x, default)
            if x in self.data:
                v = self.data[x]
                print "Pillar.get found key='{0}' value='{1}'".format(x, v)
                return v
            else:
                return default

    pass

#opts=#Salt.Opts() 
opts={
    'cachedir' : '/tmp',
    'file_client': 'remote',
    'transport': 'local',
    'jinja_trim_blocks': False,
    'jinja_lstrip_blocks': False,
    'allow_undefined' :  False,
    'file_roots' : {
        'base' : ["./"]
    }
}
grains=Salt.Grains()

pillar=Salt.Pillar()
class TomCat:
    def native(self, x):
        return "True"
tomcat = TomCat()
salt.renderers.jinja.__salt__={
#    'tomcat.native' : tomcat.native,
    'pillar.get' : pillar.get,
    'grains.filter_by' : grains.filter_by,
}

salt.renderers.jinja.__opts__=opts
salt.renderers.jinja.__pillar__=pillar
salt.renderers.jinja.__grains__=grains
opts['__pillar']=pillar

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
