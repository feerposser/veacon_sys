
def is_from_group(user, group):
    """
    Verifica se um usuário é de algum grupo específico
    :param user: django.contrib.auth.models.User
    :param group: str
    :return: true, false
    """

    for group_name in user.groups.all():
        if group_name.name == group:
            # print(group_name.name)
            return True
        return False
