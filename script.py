def render_ui(self):
    """Render UI overlay"""
    # Dark panel background
    panel_rect = pygame.Rect(20, 20, 200, 100)
    pygame.draw.rect(self.screen, UI_DARK_GRAY, panel_rect, border_radius=8)
    pygame.draw.rect(self.screen, (100, 100, 100), panel_rect, 1, border_radius=8)

    # Health line: heart icon + "Health: 5/5"
    heart = self.font_large.render("♥", True, HEART_RED)
    self.screen.blit(heart, (35, 28))

    health_text = self.font_small.render(f"Health: {self.health}/{self.max_health}", True, TEXT_WHITE)
    self.screen.blit(health_text, (65, 32))

    # Level line
    level_text = self.font_small.render(f"Level: {self.level}", True, TEXT_WHITE)
    self.screen.blit(level_text, (35, 65))# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
