from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'good night'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'i missing you'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'love you'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'i feel sad'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'i got sick'

# 1 #
    def on_enter_state1(self, update):
        update.message.reply_text("good night,Daring~")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')
# 2 #
    def on_enter_state2(self, update):
        update.message.reply_text("I'm missing you ,too.QQ")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
# 3 #
    def on_enter_state3(self, update):
        update.message.reply_text("really~~:)  me too ^o^")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
# 4 #
    def on_enter_state4(self, update):
        update.message.reply_text("Dear ,I'm not stay by your side, you have to take care of yourself QQ")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
# 5 #
    def on_enter_state5(self, update):
        update.message.reply_text("Daring your health is my greatest happiness , let me stay with you ~ ")
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')
#////////////////////////////////////////////
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'the weather is great today'
    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == '<3'
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == 'are you angry?'
    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == 'baby you on line?'
    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == 'where are you?'

# 6 #
    def on_enter_state6(self, update):
        update.message.reply_text("Lets go on a data! nowwwwwwwww!!")
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
# 7 #
    def on_enter_state7(self, update):
        update.message.reply_text("<333")
        self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')
# 8 #
    def on_enter_state8(self, update):
        update.message.reply_text("I think we can be better :(")
        self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')
# 9 #
    def on_enter_state9(self, update):
        update.message.reply_text("I stay by your side every moment :)")
        self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')
# 10 #
    def on_enter_state10(self, update):
        update.message.reply_text("I'm in the MRT station, do you missing me? hehe<3")
        self.go_back(update)

    def on_exit_state10(self, update):
        print('Leaving state10')


