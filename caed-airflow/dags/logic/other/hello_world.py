import time

def hello_world(text: str):
    print(text)


def just_sleeping():
    try:
        time.sleep(1)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    hello_world(text='hello world !')
    just_sleeping()