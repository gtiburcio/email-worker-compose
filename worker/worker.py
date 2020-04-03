import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
  redis_host = os.getenv('REDIS_HOST', 'queue')
  r = redis.Redis(host=redis_host, port=6379, db=0)
  print('Aguardando mensagens...')
  while True:
    mensagem = json.loads(r.blpop('sender')[1])
    # Simulando envio do e-mail...
    print('Mandando a mensagem', mensagem['assunto'])
    tempo = randint(10, 25)
    print('Espere', tempo, 'segundos')
    sleep(tempo)
    print('Mensagem', mensagem['assunto'], 'enviada com sucesso!')