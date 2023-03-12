from setuptools import setup, find_packages


setup(
    name='fastapi_http_response',
    description="This is a Python package that simplifies the definition of standard HTTP responses for FastAPI APIs.",
    long_description=open('README.md').read(),
    version='0.0.1',
    setup_requires=['pytest-runner'],
    author='Tharles Amaro',
    author_email='tharlesamaro@gmail.com',
    url="https://github.com/tharlesamaro/fastapi-doc-http-response",
    license='MIT',
    keywords=["fastapi", "http", "response", "api", "documentation"],
    packages=find_packages(),
    install_requires=[
        'fastapi',
    ],
    python_requires='>=3.10', 
)

setup_re