from setuptools import setup
import os

desc = open("README.rst").read() if os.path.isfile("README.rst") else ""


setup(
    name='datatables',
    version='0.4.9',
    packages=['datatables'],
    url='https://github.com/actuarial-tools/py-datatables/',
    license='MIT',
    long_description=desc,
    keywords='sqlalchemy datatables jquery pyramid flask',
    author='',
    author_email='email@google.com',
    description='Integrates SQLAlchemy with DataTables (framework agnostic)',
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Pyramid',
        'Framework :: Flask',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
