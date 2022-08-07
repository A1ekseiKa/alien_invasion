class GameStats():
    """Отслеживает статистики для игры Alien Invansion."""

    def __init__(self, ai_game):
        """Инициализирует статистику игры."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Alien Invansion запускается в активном состоянии.
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
