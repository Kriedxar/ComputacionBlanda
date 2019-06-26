import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

dia = ctrl.Antecedent(np.arange(0, 7, 1),'dia')
mes = ctrl.Antecedent(np.arange(0, 12, 1),'mes')
hora = ctrl.Antecedent(np.arange(0,24, 0.1), 'hora') 
lluvia = ctrl.Antecedent(np.arange(0, 11, 0.1),'lluvia')   
riesgo = ctrl.Consequent(np.arange(0, 11,0.1),'riesgo')

dia['semana'] = fuzz.trapmf(dia.universe,[0,0,4,4])
dia['fin_semana'] = fuzz.trapmf(dia.universe,[4,5,6,6])

mes['primavera'] = fuzz.trapmf(mes.universe,[0,0,2,3])
mes['verano'] = fuzz.trapmf(mes.universe,[2,3,4,5])
mes['otono'] = fuzz.trapmf(mes.universe,[4,5,6,9])
mes['invierno'] = fuzz.trapmf(mes.universe,[8,9,11,11])

hora['madrugada'] = fuzz.trapmf(hora.universe,[0,0,6,6])
hora['manana'] = fuzz.trapmf(hora.universe,[5,9,10,13])
hora['tarde'] = fuzz.trapmf(hora.universe,[12,16,17,19])
hora['noche'] = fuzz.trapmf(hora.universe,[18,19,23,23])

lluvia['no_lluvia'] = fuzz.trapmf(lluvia.universe,[0,0,2,3])
lluvia['lluvia'] = fuzz.trapmf(lluvia.universe,[2,4,5,8])
lluvia['tormenta'] = fuzz.trapmf(lluvia.universe,[7,8,10,10])

riesgo['bajo'] = fuzz.trapmf(riesgo.universe,[0,0,2,3])
riesgo['medio'] = fuzz.trapmf(riesgo.universe,[2,4,5,7])
riesgo['alto'] = fuzz.trapmf(riesgo.universe,[6,7,10,10])

regla1 = ctrl.Rule(mes['invierno'] & (lluvia['lluvia'] | lluvia['tormenta'] & (hora['madrugada']|hora['manana']|hora['tarde']|hora['noche']) & (dia['semana']|dia['fin_semana'])) , riesgo['alto'])
regla2 = ctrl.Rule((mes['invierno']|mes['otono']|mes['verano']|mes['primavera'])&(hora['noche']|hora['madrugada']) & lluvia['tormenta'] & (dia['semana']|dia['fin_semana']), riesgo['alto'])
regla3 = ctrl.Rule((mes['invierno']|mes['otono']|mes['verano']|mes['primavera'])&(hora['noche']|hora['madrugada']) & lluvia['lluvia'] & (dia['semana']|dia['fin_semana']), riesgo['medio'])
regla4 = ctrl.Rule((mes['invierno']|mes['otono']|mes['verano']|mes['primavera'])&(hora['tarde']|hora['manana']) & lluvia['no_lluvia']& (dia['semana']|dia['fin_semana']), riesgo['bajo'])

regla5 = ctrl.Rule(mes['primavera'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla6 = ctrl.Rule(mes['primavera'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])
regla7 = ctrl.Rule(mes['primavera'] & hora['manana'] & lluvia['lluvia'] & dia['semana'] , riesgo['bajo'])
regla8 = ctrl.Rule(mes['primavera'] & hora['manana'] & lluvia['lluvia'] & dia['fin_semana'] , riesgo['medio'])
regla9 = ctrl.Rule(mes['primavera'] & hora['manana'] & lluvia['tormenta'] & dia['semana'] , riesgo['medio'])
regla10 = ctrl.Rule(mes['primavera'] & hora['manana'] & lluvia['tormenta'] & dia['fin_semana'] , riesgo['medio'])
regla11 = ctrl.Rule(mes['primavera'] & hora['tarde'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla12 = ctrl.Rule(mes['primavera'] & hora['tarde'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])
regla13 = ctrl.Rule(mes['primavera'] & hora['tarde'] & lluvia['tormenta'] & dia['semana'] , riesgo['medio'])
regla14 = ctrl.Rule(mes['primavera'] & hora['tarde'] & lluvia['tormenta'] & dia['fin_semana'] , riesgo['medio'])
regla15 = ctrl.Rule(mes['primavera'] & hora['noche'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla16 = ctrl.Rule(mes['primavera'] & hora['noche'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])

regla17 = ctrl.Rule(mes['verano'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla18 = ctrl.Rule(mes['verano'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])
regla19 = ctrl.Rule(mes['verano'] & hora['manana'] & lluvia['lluvia'] & dia['semana'] , riesgo['bajo'])
regla20 = ctrl.Rule(mes['verano'] & hora['manana'] & lluvia['lluvia'] & dia['fin_semana'] , riesgo['medio'])
regla21 = ctrl.Rule(mes['verano'] & hora['manana'] & lluvia['tormenta'] & dia['semana'] , riesgo['medio'])
regla22 = ctrl.Rule(mes['verano'] & hora['manana'] & lluvia['tormenta'] & dia['fin_semana'] , riesgo['medio'])
regla23 = ctrl.Rule(mes['verano'] & hora['tarde'] & lluvia['lluvia'] & dia['semana'] , riesgo['bajo'])
regla24 = ctrl.Rule(mes['verano'] & hora['tarde'] & lluvia['lluvia'] & dia['fin_semana'] , riesgo['medio'])
regla25 = ctrl.Rule(mes['verano'] & hora['tarde'] & lluvia['tormenta'] & dia['semana'] , riesgo['medio'])
regla26 = ctrl.Rule(mes['verano'] & hora['tarde'] & lluvia['tormenta'] & dia['fin_semana'] , riesgo['alto'])
regla27 = ctrl.Rule(mes['verano'] & hora['noche'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla28 = ctrl.Rule(mes['verano'] & hora['noche'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])

regla29 = ctrl.Rule(mes['otono'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla30 = ctrl.Rule(mes['otono'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])
regla31 = ctrl.Rule(mes['otono'] & hora['manana'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla32 = ctrl.Rule(mes['otono'] & hora['manana'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])
regla33 = ctrl.Rule(mes['otono'] & hora['manana'] & lluvia['tormenta'] & dia['semana'] , riesgo['medio'])
regla34 = ctrl.Rule(mes['otono'] & hora['manana'] & lluvia['tormenta'] & dia['fin_semana'] , riesgo['alto'])
regla35 = ctrl.Rule(mes['otono'] & hora['tarde'] & lluvia['lluvia'] & dia['semana'] , riesgo['medio'])
regla36 = ctrl.Rule(mes['otono'] & hora['tarde'] & lluvia['lluvia'] & dia['fin_semana'] , riesgo['medio'])
regla37 = ctrl.Rule(mes['otono'] & hora['tarde'] & lluvia['tormenta'] & dia['semana'] , riesgo['alto'])
regla38 = ctrl.Rule(mes['otono'] & hora['tarde'] & lluvia['tormenta'] & dia['fin_semana'] , riesgo['alto'])
regla39 = ctrl.Rule(mes['otono'] & hora['noche'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla40 = ctrl.Rule(mes['otono'] & hora['noche'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])

regla41 = ctrl.Rule(mes['invierno'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla42 = ctrl.Rule(mes['invierno'] & hora['madrugada'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['bajo'])
regla43 = ctrl.Rule(mes['invierno'] & hora['noche'] & lluvia['no_lluvia'] & dia['semana'] , riesgo['bajo'])
regla44 = ctrl.Rule(mes['invierno'] & hora['noche'] & lluvia['no_lluvia'] & dia['fin_semana'] , riesgo['medio'])

riesgo_ctrl = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9, regla10, regla11, regla12, 
                                 regla13, regla14, regla15, regla16, regla17, regla18, regla19, regla20, regla21, regla22, regla23, regla24, 
                                 regla25, regla26, regla27, regla28, regla29, regla30, regla31, regla32, regla33, regla34, regla35, regla36, 
                                 regla37, regla38, regla39, regla40, regla41, regla42, regla43, regla44])

probriesgo = ctrl.ControlSystemSimulation(riesgo_ctrl)

def aplicar(ddia, dmes, dhora, dlluvia):
	probriesgo.input['dia']= ddia
	probriesgo.input['mes']= dmes
	probriesgo.input['hora']= dhora
	probriesgo.input['lluvia']= dlluvia

	probriesgo.compute()

	return (probriesgo.output['riesgo'])