from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '晚安'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '我想你了'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'love you'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '我很難過'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '我生病了'

# 1 #
    def on_enter_state1(self, update):
        update.message.reply_text("晚安,親愛的:)")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')
# 2 #
    def on_enter_state2(self, update):
        update.message.reply_text("我也很想你ㄚ QQ..")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
# 3 #
    def on_enter_state3(self, update):
        update.message.reply_text("me too ^o^")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
# 4 #
    def on_enter_state4(self, update):
        update.message.reply_text("寶貝,我沒辦法時時刻刻再你身邊,你要好好照顧自己，我愛你")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
# 5 #
    def on_enter_state5(self, update):
        update.message.reply_text("你的健康是我最大的幸福，讓我一直陪伴你吧:))")
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')
#////////////////////////////////////////////
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == '今天天氣真好'
    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == '<3'
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '你在生氣嗎'
    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == '寶貝在嗎'
    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == '你在哪裡呢'

# 6 #
    def on_enter_state6(self, update):
        update.message.reply_text("那我們快去約會！！")
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
        update.message.reply_text("我只是覺得我們可以更好,不是嗎:(")
        self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')
# 9 #
    def on_enter_state9(self, update):
        update.message.reply_text("我一直都在")
        self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')
# 10 #
    def on_enter_state10(self, update):
        update.message.reply_text("我在捷運站,想我了嗎哈哈哈~~")
        self.go_back(update)

