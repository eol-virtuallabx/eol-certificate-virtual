import setuptools

setuptools.setup(
    name="eol-certificate-virtual",
    version="0.0.1",
    author="constanzaaltamirano",
    author_email="constanzaaltamirano@uchile.cl",
    description="Eol certificate virtual",
    long_description="Eol certificate virtual",
    url="https://cajalosandes.virtual-labx.cl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "lms.djangoapp": [
            "eol_certificate_virtual = certificate_virtual.apps:EolCertificateConfig",
        ]
    },
)
