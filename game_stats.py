class GameStats():
    """Отслеживает статистики для игры Alien Invansion."""

    def __init__(self, ai_game):
        """Инициализирует статистику игры."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Рекорд не должен сбрасываться
        self.high_score = 0

        # Alien Invansion запускается в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
