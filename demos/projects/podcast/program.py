import service
import random


def main():
    """
    A short comment to test commit feature with github
    :return:
    """
    show_header()

    service.download_info()
    print("Working with total of {} episodes".format(service.get_latest_show_id()))
    display_results()


def show_header():
    """

    :return:
    """
    print("Welcome to the talk python info downloader.")
    print()


def display_results():
    """
    A new comment for tests with github integration
    :return:
    """
    start = random.randint(90, 110)
    end = random.randint(130, service.get_latest_show_id()+1)

    for show_id in range(start, end):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


if __name__ == '__main__':
    main()
