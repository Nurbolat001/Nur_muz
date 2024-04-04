from setuptools import setup, find_packages

setup(
    name='music_project',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
        # Другие зависимости вашего проекта, если они есть
    ],
    entry_points={
        'console_scripts': [
            'my_script = music_project.my_script:main',
            # Здесь можно добавить скрипты вашего проекта для выполнения из командной строки
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
