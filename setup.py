"""
Performs date and date-range (period) parsing on arbitrary strings using
Python, Pendulum, and love (hate)
"""

from setuptools import setup

setup(
    name='arbitrary-dateparser',
    version='0.0.0',
    packages=['arbitrary_dateparser'],
    zip_safe=False,
    python_requires='>=3, <4',
    include_package_data=False,
    install_requires=[
        'pendulum~=2.0.5',
        'python-dateutil~=2.8.0',
        'pytzdata~=2019.2',
        'six~=1.12.0',
    ],
    author='Michael Phelps',
    author_email='michael.phelps@cpcc.edu',
    url='https://github.com/nottheswimmer/arbitrary-dateparser',
    description='Date parsing for arbitrary strings!',
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
    license='MIT',
)
