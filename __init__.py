from mycroft import MycroftSkill, intent_file_handler


class AtividadeSexual(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sexual.atividade.intent')
    def handle_sexual_atividade(self, message):
        self.speak_dialog('sexual.atividade')


def create_skill():
    return AtividadeSexual()

