"""
Performs date and date-range (period) parsing on arbitrary strings using
Python, Pendulum, and love (hate)
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='arbitrary-dateparser',
    version='0.0.3',
    packages=['arbitrary_dateparser'],
    zip_safe=False,
    python_requires='>=3, <4',
    include_package_data=False,
    install_requires=[
        'pendulum==2.0.5',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Michael Phelps',
    author_email='michael.phelps@cpcc.edu',
    url='https://github.com/nottheswimmer/arbitrary-dateparser',
    description='Date parsing for arbitrary strings!',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    license='MIT',
)
