def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Adds new customers to their desigened quee

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    quees = [normal_queue, express_queue]
    quees[ticket_type].append(person_name)
    return quees[ticket_type]


def find_my_friend(queue, friend_name):
    """Find where a friend is located in the quee

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Insert a friend in the specified quee position

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Remove an specific person from the queue

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """Count how many times a name is repeated in the queue

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    times_name_repeated = queue.count(person_name)
    return times_name_repeated


def remove_the_last_person(queue):
    """Remove the last person from the queue

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop()


def sorted_names(queue):
    """Sort the people in the queue

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    queue.sort()
    return queue
