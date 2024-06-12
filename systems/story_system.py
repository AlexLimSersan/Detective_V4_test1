class StoryGenerator:
    def __init__(self, story_templates, game_state):
        self.story_templates = story_templates
        self.game_state = game_state #might as well

    def generate_story(self, murderer_id, profile):
        story_texts = self.story_templates[murderer_id]
        for