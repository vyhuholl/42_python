def data_types():
    variables = [0, '', 0.0, False, [], dict(), (), set()]
    print([type(elem).__name__ for elem in variables])


if __name__ == '__main__':
    data_types()
