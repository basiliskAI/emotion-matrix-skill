from mycroft import MycroftSkill, intent_file_handler


class EmotionMatrix(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('matrix.emotion.intent')
    def handle_matrix_emotion(self, message):
        self.speak_dialog('matrix.emotion')


def create_skill():
    return EmotionMatrix()

