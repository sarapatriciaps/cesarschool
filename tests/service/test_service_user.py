import unittest

from src.service.service_user import ServiceUser


class TestServiceUser(unittest.TestCase):
    def test_add_user_with_success(self):
        resposta_esperada = "Usuario adicionado"
        service = ServiceUser()
        resposta = service.add_user("Fabricio", "Eng")
        assert resposta == resposta_esperada
    def test_add_user_with_invalid_name(self):
        resposta_esperada = "Usuario invalido"
        service = ServiceUser()
        resposta = service.add_user(55, "Eng")
        assert resposta_esperada == resposta
    def test_user_that_already_exists_in_db(self):
        resposta_esperada = "usuário inválido, nome já existe"
        service = ServiceUser()
        service.add_user("macmf", "astronauta")
        resposta = service.add_user("macmf", "astronauta")
        assert resposta_esperada == resposta

    def test_get_user_by_name_when_name_exists(self):
        resposta_esperada = "name: marcelo, job: astronauta"
        service = ServiceUser()
        service.add_user("marcelo", "astronauta")
        resposta = service.get_user_by_name("marcelo")
        assert resposta_esperada == resposta
    def test_get_user_by_name_passing_a_invalid_name_to_method(self):
        resposta_esperada = "Nome inválido ou usuário não existe na base de dados"
        service = ServiceUser()
        service.add_user(5, "astronauta")
        resposta = service.get_user_by_name("marcelo")
        assert resposta_esperada == resposta

    def test_get_user_by_name_passing_a_name_which_does_not_exist_in_db_to_method(self):
        resposta_esperada = "Nome inválido ou usuário não existe na base de dados"
        service = ServiceUser()
        service.add_user("not marcelo", "astronauta")
        resposta = service.get_user_by_name("marcelo")
        assert resposta_esperada == resposta

    def test_remove_user_with_success(self):
        resposta_esperada = 'usuário excluído'
        service = ServiceUser()
        service.add_user("macmf", "demon slayer")
        resposta = service.remove_user("macmf")
        assert resposta == resposta_esperada
    def test_remove_user_which_does_not_exist(self):
        resposta_esperada = 'usuário não existe'
        service = ServiceUser()
        resposta = service.remove_user("macmf")
        assert resposta == resposta_esperada

    def test_remove_invalid_user(self):
        resposta_esperada = 'usuário inválido'
        service = ServiceUser()
        resposta = service.remove_user(5)
        assert resposta == resposta_esperada

    def test_update_a_valid_user(self):
        resposta_esperada = 'usuário atualizado'
        service = ServiceUser()
        service.add_user("macmf", "demon slayer")
        resposta = service.update_user("macmf", "aluno")
        assert resposta == resposta_esperada
    def test_update_a_invalid_user(self):
        resposta_esperada = 'usuário inválido'
        service = ServiceUser()
        service.add_user("macmf", "demon slayer")
        resposta = service.update_user(5, "aluno")
        assert resposta == resposta_esperada
    def test_update_a_user_which_does_not_exist(self):
        resposta_esperada = 'usuário não existe'
        service = ServiceUser()
        resposta = service.update_user('macmf', "aluno")
        assert resposta == resposta_esperada