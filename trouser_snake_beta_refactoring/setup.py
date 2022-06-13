import cx_freeze

executable = [cx_Freeze.executable('Trouser_snake.py')]

cx_Freeze.setup(
    name="Trouser Snake",
    options={'build_exe': {'packages': ['pygame'],
                           'include_files': ['snakehead.png', 'speed.png', 'pill.png', 'taco.png', 'bggame.jpeg']}},

    description='Trouser snake game',
    executables=executable
)
