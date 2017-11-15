# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

from players.models import Player

class PlayerList(ListView):
	model = Player


def index(request):
	num_players = Player.objects.all().count()
	return render(
		request,
		'index.html',
		context={'num_players':num_players}
		)

