import sys


def call_center():
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
        ]
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return sorted(list(set(clients) - set(recipients)))


def potential_clients():
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
        ]
    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
        'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
        'mr@robot.gov', 'eleven@yahoo.com'
        ]
    return sorted(list(set(participants) - set(clients)))


def loyalty_program():
    clients = [
        'andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com'
        ]
    participants = [
        'walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
        'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
        'mr@robot.gov', 'eleven@yahoo.com'
        ]
    return sorted(list(set(clients) - set(participants)))


def marketing(command):
    if command == 'call_center':
        return call_center()
    elif command == 'potential_clients':
        return potential_clients()
    elif command == 'loyalty_program':
        return loyalty_program()
    raise ValueError('Unknown command')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(marketing(sys.argv[1]))
    else:
        print("usage: python3 marketing.py command")
