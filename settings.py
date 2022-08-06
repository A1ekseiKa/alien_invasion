class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5

        # Параметры снаяда.
        self.bulet_speed = 1
        self.bulet_width = 3
        self.bulet_height = 15
        self.bulet_color = (60, 60, 60)