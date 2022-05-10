def eat_ghost(power_pellet_active, touching_ghost):
    """Determine if pacman can eat a ghost

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if power_pellet_active * touching_ghost:
        return True
    else:
        return False
    # This can be replaced by "return bool(test)"
    #  return bool(power_pellet_active * touching_ghost)


def score(touching_power_pellet, touching_dot):
    """Determine if pacman scores

    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    """
    #  if touching_power_pellet + touching_dot:
    #  return True
    #  else:
    #  return False
    # This can be replaced by "return bool(test)"
    # This will ensure that the returned value is a boolean
    return bool(touching_power_pellet + touching_dot)


def lose(power_pellet_active, touching_ghost):
    """Determine if pacman losess after touching ghost

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    """
    if touching_ghost:
        return not power_pellet_active
    # There is no need for else here after a "return" statement
    # Since the next part won't be executed if the conditional goes through
    #  else:
    return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Determine if pacman has win the game without dying

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    """
    if not lose(power_pellet_active, touching_ghost):
        return has_eaten_all_dots
    # There is no need for else here after a "return" statement
    #  else:
    return False
