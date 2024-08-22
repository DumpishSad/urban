def send_email(message, recipient, sender ='university.help@gmail.com'):
    if not is_email(recipient) or not is_email(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


def is_email(message):
    if '@' not in message:
        return False

    last_str = ['.com', '.ru', '.net']
    for i in last_str:
        if message[-len(i):] == i:
            return True
    return False
