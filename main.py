from src.service.service_user import ServiceUser

service = ServiceUser()
resposta = service.add_user('marcelo','test job 1')
resposta = service.add_user('','test')

#none
resposta = service.add_user(None, 'test')
resposta = service.add_user('test1', None)

#tipo diferente de string
resposta = service.add_user(5, 'job')
resposta = service.add_user('marcelo', 5)

resposta = service.add_user(True, 'job')
resposta = service.add_user('marcelo', True)

resposta = service.add_user('marcelo','test')
resposta = service.add_user('marcelo novo','test')

resposta = service.add_user('sara','test')
resposta = service.add_user('ricardo','test')

#print([x.name for x in service.store.bd])
#print([x.job for x in service.store.bd])
#print(resposta)

print([(x.name, x.job) for x in service.store.bd])
print(service.remove_user('marcelo asdasdasdasdas'))
print(service.remove_user('sara'))
print([(x.name, x.job) for x in service.store.bd])
service.update_user('marcelo', 'astronautaaaa')
print([(x.name, x.job) for x in service.store.bd])

print(service.get_user_by_name('marcelo'))