from mycroft import MycroftSkill, intent_file_handler


class LightScreenTvpower(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tvpower.screen.light.intent')
    def handle_tvpower_screen_light(self, message):
        self.speak_dialog('tvpower.screen.light')


def create_skill():
    return LightScreenTvpower()

