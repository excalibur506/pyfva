'''
Created on 16/12/2015

@author: luisza
'''

from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


version = '0.0.5'



from setuptools.command.install import install
import pip
class my_install(install):
    def run(self):
        install.run(self)
        pip.main(['install', "git+https://github.com/soapteam/soapfish.git#egg=soapfish-0.5.2", '-q'])



setup(
    author='Luis Zarate Montero',
    author_email='luis.zarate@solvosoft.com',
    name='pyfva',
    version=version,
    description='Cliente para conectar instituciones con BCCR FVA.',
    long_description=README,
    url='https://github.com/solvo/pyfva',
    license='GNU General Public License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    cmdclass={'install': my_install},
)
