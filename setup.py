from setuptools import setup, find_packages

VERSION = '1.02'

setup(name='daikon',
        version=VERSION,
        description='ElasticSearch CLI',
        long_description=''' ''',
        classifiers=[],
        keywords='',
        author='Patrick Ancillotti',
        author_email='patrick@eefy.net',
        url='http://www.github.com/neogenix/daikon',
        license='LICENSE',
        packages=find_packages(
            exclude=[
                'ez_setup',
                'examples',
                'tests'
            ]
        ),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'requests',
            'anyjson'
        ],
        data_files=[
            ('/etc/daikon', ['daikon.conf'])
        ],
        entry_points={
            'console_scripts':
                ['daikon = daikon.daikon:main']
        }
)
