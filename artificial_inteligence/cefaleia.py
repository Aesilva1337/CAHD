# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:52:07 2019

@author: LDarkz
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

vital_alter = ctrl.Antecedent(np.arange(0, 11, 1), 'Dados Vitais Alterados')
dor = ctrl.Antecedent(np.arange(0, 11, 1), 'Dor')
nuca = ctrl.Antecedent(np.arange(0, 11, 1), 'Nuca')
nausea = ctrl.Antecedent(np.arange(0,11,1), 'Nausea')
mental_alter = ctrl.Antecedent(np.arange(0,11,1), 'Alteração Estado Mental')
enxaqueca = ctrl.Antecedent(np.arange(0,11,1), 'Enxaqueca')
manchester = ctrl.Consequent(np.arange(0, 6, 1), 'Manchester')

vital_alter.automf(3)

nuca['nao_rigida'] = fuzz.piecemf(nuca.universe, [0, 8, 8])
nuca['rigida'] = fuzz.piecemf(nuca.universe, [8, 10, 10])

dor['nao_intensa'] = fuzz.piecemf(dor.universe, [0, 8, 8])
dor['intensa'] = fuzz.piecemf(dor.universe, [8, 10, 10])

manchester['vermelho'] = fuzz.trimf(manchester.universe, [0, 0, 3])
manchester['amarelo'] = fuzz.trimf(manchester.universe, [0, 3, 6])
manchester['verde'] = fuzz.trimf(manchester.universe, [3, 6, 6])

rule1 = ctrl.Rule(vital_alter['poor'] | vital_alter['good'] | dor['intensa'], manchester['vermelho'])
rule2 = ctrl.Rule(nuca['rigida'], manchester['amarelo'])
rule3 = ctrl.Rule(vital_alter['average'] | dor['nao_intensa'], manchester['verde'])

manchester_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

classificar = ctrl.ControlSystemSimulation(manchester_ctrl)

classificar.input['Dados Vitais Alterados'] = 5
classificar.input['Dor'] = 5
classificar.input['Nuca'] = 9

classificar.compute()

result = classificar.output['Manchester']
print ("Classificação: ", result)
manchester.view(sim=classificar)