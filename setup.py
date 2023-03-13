from setuptools import setup


setup(
    name='fastapi_http_response',
    description="This is a Python package that simplifies the definition of standard HTTP responses for FastAPI APIs.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    version='0.0.2',
    author='Tharles Amaro',
    author_email='tharlesamaro@gmail.com',
    url="https://github.com/tharlesamaro/fastapi-doc-http-response",
    license='MIT',
    keywords=["fastapi", "http", "response", "api", "documentation"],
    packages=['fastapi_doc_http_response', 'tests'],
    install_requires=[
        'fastapi',
    ],
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 4 - Beta',
        "Environment :: Web Environment",
        'License :: OSI Approved :: MIT License',
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development",
        "Typing :: Typed",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Programming Language :: Python',
    ],
    
)
