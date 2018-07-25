class Character:
    def __init__(self) -> None:
        self.name = 'Nagibator'
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()


QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = 'QSPEAK', 'QHUNT', 'QCARRY'


class Event:

    def __init__(self, kind) -> None:
        self.kind = kind


class NullHandler:

    def __init__(self, successor=None) -> None:
        self.__successor = successor

    def handle(self, char: Character, event):
        if self.__successor is not None:
            self.__successor.handle(char, event)


class QuestSpeak(NullHandler):

    def handle(self, char, event):
        if event.kind == QUEST_SPEAK:
            quest_name = 'Talk to farmer'
            xp = 100
            if quest_name not in (char.passed_quests | char.taken_quests):
                print(f'Quest taken: {quest_name}')
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f'Quest completed: {quest_name}')
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print('...going to another accessor...')
            super().handle(char, event)


class QuestHunt(NullHandler):

    def handle(self, char, event):
        if event.kind == QUEST_HUNT:
            quest_name = 'Hunt on rats'
            xp = 300
            if quest_name not in (char.passed_quests | char.taken_quests):
                print(f'Quest taken: {quest_name}')
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f'Quest completed: {quest_name}')
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print('...going to another accessor...')
            super().handle(char, event)


class QuestCarry(NullHandler):

    def handle(self, char, event):
        if event.kind == QUEST_CARRY:
            quest_name = 'Carry some wood'
            xp = 200
            if quest_name not in (char.passed_quests | char.taken_quests):
                print(f'Quest taken: {quest_name}')
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f'Quest completed: {quest_name}')
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print('...going to another accessor...')
            super().handle(char, event)


class QuestGiver:

    def __init__(self) -> None:
        self.handlers = QuestCarry(QuestHunt(QuestSpeak(NullHandler)))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, char: Character):
        for event in self.events:
            self.handlers.handle(char, event)


if __name__ == '__main__':
    # All events that can happen
    events = [Event(QUEST_CARRY), Event(QUEST_HUNT), Event(QUEST_SPEAK)]

    quest_giver = QuestGiver()
    # Quest giver can handle all of the events
    for event in events:
        quest_giver.add_event(event)

    player = Character()

    quest_giver.handle_quests(player)
    print()
    player.taken_quests = {'Carry some wood', 'Talk to farmer'}
    quest_giver.handle_quests(player)
    print()
    quest_giver.handle_quests(player)
