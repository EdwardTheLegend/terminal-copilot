from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

with open('README.md') as f:
    readme = f.read()

long_description = readme

setup(
        name ='terminal-copilot',
        version ='1.2.1',
        author ='Methexis',
        author_email ='joelkronander@gmail.com',
        url ='https://github.com/Methexis-Inc/terminal-copilot',
        description ='A smart terminal assistant that helps you find the right command',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='Apache License 2.0',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'copilot=copilot.copilot:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ),
        keywords ='terminal copilot openai gpt3',
        install_requires = requirements,
        zip_safe = False
)