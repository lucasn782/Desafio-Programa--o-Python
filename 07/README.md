# Agendamento de Funções com `sched`

## Descrição
Este exercício demonstra como agendar a execução de uma função em um horário absoluto específico utilizando o módulo `sched` do Python.

Arquivo principal: `agendar_funcao.py`

## Funcionalidade
A função `agendamento(horario_do_evento, funcao, *args)`:
- Agenda a execução de `funcao(*args)` no timestamp POSIX `horario_do_evento`
- Exibe uma mensagem com o horário humano-legível do agendamento
- Executa a fila de eventos do `sched.scheduler`

## Algoritmo
1. Cria um `scheduler` com `time.time` e `time.sleep`
2. Enfileira um evento com `enterabs(horario_do_evento, prioridade=1, funcao, argument=args)`
3. Converte o timestamp para string com `time.asctime`
4. Executa `s.run()` para processar o evento no momento correto

## Código (núcleo da solução)
```python
import sched
import time

def agendamento(horario_do_evento, funcao, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(horario_do_evento, 1, funcao, argument=args)
    t = time.asctime(time.localtime(horario_do_evento))
    print(f'{funcao.__name__}() agendado para {t}')
    s.run()
```

## Exemplos de Uso
```python
>>> import time
>>> from agendar_funcao import agendamento
>>> def oi(nome):
...     print(f'Olá, {nome}!')
...
>>> quando = time.time() + 5  # 5 segundos a partir de agora
>>> agendamento(quando, oi, 'Lucas')
oi() agendado para Wed Jan 01 12:00:05 2025
Olá, Lucas!
```

## Como Usar
- Execute a partir de outro módulo ou REPL, calculando um timestamp futuro e passando a função-alvo.

## Requisitos
- Python 3.x
- Módulos padrão `sched` e `time`

## Observações
- `enterabs` usa timestamp absoluto (epoch). Para agendar relativo, use `enter`.
- O processo deve permanecer ativo até a execução do evento.

## Melhorias Futuras
- Adicionar suporte a múltiplos eventos e cancelamento
- Interface de linha de comando para agendar comandos rapidamente