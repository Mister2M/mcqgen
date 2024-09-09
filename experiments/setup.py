from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version= '0.0.1',
    author='daniel mabanza',
    author_email='mrdanielmabanza@gmail.com',
    install_requires = ['google-generativeai', 'streamlit', 'python-dotenv','PyPDF2'],
    packages=find_packages()
)