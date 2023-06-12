# -*- coding: utf-8 -*-
"""Astar.ipynb

Da bismo mogil da imlementiramo **A*** moramo:
* kao argumente prihvata: **pocetak, kraj, funkcija_heuristike**
* imati *otvorenu listu* u kojoj ce se inicijalno naci pocetni cvor pretrage
  * obavezno ukalanjanje trenutnog obradjenog cvora iz otvorene liste
* imati heuristicku funkciju - neke procene koje se korist, npr: vazdusna rastojanja od gradova, euklidska rastojanja, menhetn, ..
* da bismo ispisali putanju, treba da pamtnimo roditelje(mapa) svakog cvora
* heuristicke procene za svaki cvor (mapa)
* funkciju koja nalazi sledeci_cvor
  * argumenti su joj: **otvorena_lista, heuristicka_procena**
"""

import sys
import pandas as pd
import json

try:
  with open('cities.json', 'r') as f:
    lista_susedstva = dict(json.load(f))

except:
  sys.exit('datoteka ne postoji')

lista_susedstva

for sused, tezina in lista_susedstva['Arad']:
  print(sused, tezina)

"""**otvorena i zatvorena lista** 
* u otvorenu listu na pocetku stavimo pocetni cvor
* funkcija nagadjanja

"""

def astar(lista_susedstva, pocetak, kraj, h):
  otvorena_lista = set([pocetak])

  pronadjen_put = False
  roditelji = {}
  roditelji[pocetak] = None 
  
  udaljenost = {v : float('inf') for v in lista_susedstva}
  udaljenost[pocetak] = 0

  heuristicka_procena = {v : float('inf') for v in lista_susedstva}
  heuristicka_procena[pocetak] = h(pocetak)

  while len(otvorena_lista) > 0:
    tmp = sledeci_cvor(otvorena_lista, heuristicka_procena)

    if (tmp == kraj):
      pronadjen_put = True
      break

    otvorena_lista.remove(tmp)

    for sused, tezina in lista_susedstva[tmp]:
      nova_udaljenost = udaljenost[tmp] + tezina
      if (udaljenost[sused] > nova_udaljenost):

        udaljenost[sused] = nova_udaljenost
        roditelji[sused] = tmp

        heuristicka_procena[sused] = nova_udaljenost + h(sused)

        if sused is not otvorena_lista:
          otvorena_lista.add(sused)

  put = []
  if pronadjen_put == True:
    while kraj is not None:
      put.append(kraj)
      kraj = roditelji[kraj]

  put.reverse()
  return put

def sledeci_cvor(otvorena_lista, heuristicka_procena):
  v = None
  min_d = float('inf')

  for cvor in otvorena_lista:
    if cvor in heuristicka_procena:
      p = heuristicka_procena[cvor]

      if p < min_d:
        min_d = p
        v = cvor

  return v

def h(n):
  H = {
    'Oradea' : 380,
    'Zerind' : 374,
    'Timisoara' : 329,
    'Lugoj' : 244,
    'Mehadia' : 241,
    'Drobeta' : 242,
    'Sibiu' : 253,
    'Fagaras' : 176,
    'Rimnicu Vilacea' : 193,
    'Pitesti' : 100,
    'Craiova' : 160,
    'Buchares' : 0
  }

  return H[n] if n in H else 400

pocetak = 'Arad'
kraj = 'Buchares'

path = astar(lista_susedstva, pocetak, kraj, h)
print(path)