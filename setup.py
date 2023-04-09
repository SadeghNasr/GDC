from setuptools import setup, find_packages

setup(
    name="gdc_client",
    use_scm_version={"local_scheme": "dirty-tag",},
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    package_data={},
    scripts=["bin/gdc_client"],
    install_requires=[
        "cryptography",
        "jsonschema",
        "lxml",
        "ndg-httpsclient",
        "pyasn1",
        "pyOpenSSL",
        "PyYAML",
        "intervaltree",
        "importlib_metadata",
        "termcolor",
        "requests",
        "progressbar2",
        "boto3",
        "moto",
    ],
)
