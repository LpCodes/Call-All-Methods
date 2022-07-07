import platform


for i in dir(platform):
    try:
        print("Output for attr {} is below".format(i))
        c = getattr(platform, i)()
        print(c)
        print("%" * 100)

    except Exception:
        print("Output for attr {} had error".format(i))
        print("%" * 100)

