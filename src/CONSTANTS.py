class CONSTANTS(object):
    """
    Contains miscellaneous constants that may be used throughout the program.
    The intention is to have a "catalogue" of variables set up before they're needed.
    """

    # File Constants
    JSON_DICT = {'Terrain': 'MapTerrain.json',
                 'Class': 'ClassLibrary.json',
                 'Enemy Race': 'EnemyRaceLibrary.json',
                 'Enemy Role': 'EnemyRoleLibrary.json',
                 'Encounter': 'Encounter.json',
                 'Equipment': 'EquipmentLibrary.json',
                 'Starting Equipment': 'StartingEquipmentLibrary.json',
                 'Card': 'CardLibrary.json',
                 'Starting Deck': 'StartingDeck.json'}

    IMAGE_DICTIONARY = {'Grass': 'GRASS.png',
                        'Hill': 'HILL.png',
                        'Mountain': 'MOUNTAIN.png',
                        'cursor': 'CURSOR.png',
                        'selected_cursor': 'SELECTED.png',
                        'targeting_tile': 'TARGETING_TILE.png',
                        'player_token': 'PLAYER.png',
                        'grunt_token': 'GRUNT.png',
                        'elite_token': 'ELITE.png',
                        'invalid_move_tile': 'INVALID_MOVE_TILE.png',
                        'valid_move_tile': 'VALID_MOVE_TILE.png',
                        'active_player': 'ACTIVE_PLAYER.png',
                        'insuf_stam_tile': 'INSUFFICIENT_STAMINA_TILE.png'}

    # Graphical Constants
    FPS = 60
    CAM_MOVE_SPEED = 10

    WINWIDTH = 1000
    WINHEIGHT = 700
    HALF_WINWIDTH = int(WINWIDTH / 2)
    HALF_WINHEIGHT = int(WINHEIGHT / 2)
    QUARTER_WINWIDTH = int(HALF_WINWIDTH / 2)
    THIRD_WINDOW_WIDTH = int(WINWIDTH / 3)

    TILE_SIZE = (50, 50)

    COLORS = {'white': (255, 255, 255),
              'black': (0, 0, 0),
              'light_grey': (211, 211, 211),
              'grey': (128, 128, 128),
              'slate_grey': (112, 128, 144),
              'red': (255, 0, 0),
              'dark_red': (160, 0, 0),
              'maroon': (128, 0, 0),
              'dark_orange': (255, 140, 0),
              'orange_red': (255, 69, 0),
              'yellow': (255, 255, 0),
              'green': (0, 255, 0),
              'medium_green': (0, 140, 0),
              'green_yellow': (173, 255, 47),
              'blue': (0, 0, 255),
              'cyan': (0, 255, 255),
              'pale_turquoise': (175, 238, 238),
              'turquoise': (64, 224, 208),
              'teal': (0, 128, 128),
              'magenta': (255, 0, 255),
              'purple': (128, 0, 128),
              'indigo': (75, 0, 130),
              'hot_pink': (255, 20, 147),
              'deep_pink': (255, 20, 147),
              'tan': (210, 180, 140),
              'golden_rod': (218, 165, 32),
              'saddle_brown': (139, 69, 19)}

    FONT_DICT = {'sans_bold': 'freesansbold.ttf'}

    # Game Logic Constants
    MAX_PLAYERS = 4

    DIFFICULTY_LIST = ['Easy',
                       'Medium',
                       'Hard',
                       'Boss']

    # Map Logic
    DIRECTION_TUPLES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    DIRECTION_DICT = {'up': (0, 1),
                      'down': (0, -1),
                      'left': (-1, 0),
                      'right': (1, 0)}

    STARTING_ROW_PERCENTAGE = 0.25
