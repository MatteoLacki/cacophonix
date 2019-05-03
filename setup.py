from setuptools import setup, find_packages

setup(
    name='cacophonix',
    packages=find_packages(),
    version='0.0.1',
    description="Replace Water's Symphony Pipeline.",
    long_description="Replace Water's Symphony Pipeline.",
    author=u'Mateusz Krzysztof Łącki',
    author_email='matteo.lacki@gmail.com',
    url='https://github.com/MatteoLacki/cacophonix',
    # download_url='https://github.com/MatteoLacki/MassTodonPy/tree/GutenTag',
    keywords=[
        'Analitical Chemistry',
        'Mass Spectrometry',
        'Automating Boring Stuff'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Programming Language :: Python :: 3.6'],
    install_requires=[],
    extras_require={}
    # include_package_data=True,
    # package_data={
    #     'data': 'data/annotated_data.csv'
    # }
    # scripts=[
    #     'bin/rta']
)
