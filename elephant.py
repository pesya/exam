def elephant():
    """
    функция, которая пытается продать тебе слона
    """

    arguments = ('ну пожалуйста', 'очень прошу', 'умоляю', 'заклинаю тебя', 'последний раз прошу')
    positive_answers = ('да', 'ок', 'окей', 'согласен', 'покупаю', 'хорошо', 'куплю')
    counter = 0
    elephant_request = 'купи слона'

    print('{}?'.format(elephant_request))
    while counter <= 5:
        user_response = str(input())
        if user_response.lower() in positive_answers:
            print('Слон продан! Поздравляю с удачной сделкой')
            return
        if counter == 5:
            break

        print('Все говорят {}, а ты купи слона, {}'.format(user_response.lower(), arguments[counter]))
        counter += 1

    print('Ну не хочешь покупать слона, ну и ладно')
    return


if __name__ == '__main__':
    elephant()
