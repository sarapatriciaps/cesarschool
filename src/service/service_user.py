from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name and job and isinstance(name, str) and isinstance(job, str):
            for x in self.store.bd:
                if x.name == name:
                    return "usuário inválido, nome já existe"
            user = User(name=name, job=job)
            self.store.bd.append(user)
            return "Usuario adicionado"
        else:
            return "Usuario invalido"
    def remove_user(self, name):
        if name and isinstance(name, str):
            list_all_names = [x.name for x in self.store.bd]
            if name not in list_all_names:
                return 'usuário não existe'
            index = list_all_names.index(name)
            self.store.bd.pop(index)
            return 'usuário excluído'
        else:
            return "usuário inválido"

    def update_user(self, name, newjob):
        if name and newjob and isinstance(name, str):
            list_all_names = [x.name for x in self.store.bd]
            if name not in list_all_names:
                return 'usuário não existe'
            index = list_all_names.index(name)
            updated_user = User(name, newjob)
            self.store.bd[index] = updated_user
            return 'usuário atualizado'
        return 'usuário inválido'
    def get_user_by_name(self, name):
        if name and isinstance(name, str):
            list_of_users_names = [x.name for x in self.store.bd]
            if name in list_of_users_names:
                index = list_of_users_names.index(name)
                return f"name: {self.store.bd[index].name}, job: {self.store.bd[index].job}"
        return "Nome inválido ou usuário não existe na base de dados"
