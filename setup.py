#!/usr/bin/env python

from distutils.core import setup
from distutils.cmd import Command
class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        raise SystemExit(
            subprocess.call(['nosetests',
                             '--verbosity=999']))

setup(name='saltstack-tomcat-formula',
      version='1.0',
      description='Salt formula for tomcat',
      author='Thomas S Hatch',
      author_email='thatch@saltstack.com',
      url='https://github.com/saltstack-formulas/tomcat-formula',
      requires=['saltstack', 'nose'],

      data_files=[
          ('/etc/salt/master.d/', 
           [
               'pillar.example'
           ]),

          ('/srv/formulas/tomcat', 
           [
               'tomcat/init.sls',
               'tomcat/native.sls',
               'tomcat/package.sls',
               'tomcat/vhosts.sls',
               'tomcat/map.jinja',
               'tomcat/manager.sls',
               'tomcat/ssl.sls',               
          ]),

          ('/srv/formulas/tomcat/files', 
           [
               'tomcat/files/tomcat-users.xml',
               'tomcat/files/server.xml'
           ])
      ],

      cmdclass={
          'test': TestCommand
      }
  )
