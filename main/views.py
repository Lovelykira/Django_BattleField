from django.shortcuts import render, redirect
from django.http import HttpResponse

from main.battle_field_control import BFControl
from main.bf_logic.battle_field import Battlefield


def index(request):
    return render(request, 'index.html')


def battle(request):
    num_armies = int(request.POST['num_armies'])
    battlef_id = BFControl.get_ID()
    new_bf = Battlefield(num_armies)
    battlef_log = new_bf.next_step()
    BFControl.add_battlfield(battlef_id, new_bf)
    BFControl.add_log(battlef_id, battlef_log)
    alive_armies_log = new_bf.get_alive_armies_log()
    alive_armies = new_bf.get_alive_armies
    dict = {'log': battlef_log, 'alive_armies_log': alive_armies_log, "alive_armies":alive_armies }
    response = render(request, 'battle.html', dict)
    response.set_cookie('Battle_ID', battlef_id)
    return response


def step(request):
    if 'Battle_ID' in request.COOKIES:
        battlef_id = int(request.COOKIES['Battle_ID'])
        battlef = BFControl.get_battlfield(battlef_id)
        battlef_log = battlef.next_step()
        BFControl.add_log(battlef_id, battlef_log)
        battlef_log = BFControl.get_log(battlef_id)
        alive_armies_log = battlef.get_alive_armies_log()
        dict = {'log': battlef_log, 'alive_armies_log': alive_armies_log}
        if 'WINS THE WAR' in battlef_log[-1]:
            return redirect('/winner')
        else:
            return render(request, 'battle.html', dict)


def winner(request):
    battlef_id = int(request.COOKIES['Battle_ID'])
    battlef = BFControl.get_battlfield(battlef_id)
    battlef_log = BFControl.get_log(battlef_id)
    winner = battlef_log[-1]
    dict = {'log': battlef_log, 'winner': winner}
    return render(request, 'winner.html', dict)