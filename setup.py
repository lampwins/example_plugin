import os

from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


setup(
    name='netbox-firewall-policy',
    version='1.0.0',
    description='This plugin is a test',
    long_description=long_description,
    url='https://github.com/lampwins/netbox-firewall-policy',
    author='John Anderson',
    author_email='lampwins@gmail.com',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    entry_points="""
[netbox.plugin]
netbox_firewall_policy=netbox_firewall_policy:NetBoxPluginMeta
""",
)
