import sched
import time

def agendamento(horario_do_evento, funcao, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(horario_do_evento, 1, funcao, argument=args)
    t = time.asctime(time.localtime(horario_do_evento))
    print(f'{funcao.__name__}() agendado para {t}')
    s.run()