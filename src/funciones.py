
import pandas as pd


### Funciones para limpieza de datos

def capitalizar(row):
    row=row.capitalize()
    return row


def pasar_ms_a_min(row):
    row = int(row/(1000*60))
    return row


def abs_coord(row):
    row = 0.5 + (0.5 - row)
    return row


### Funciones para cálculo de métricas y estadísticas de cada partido mediante la transformaación de los datos del eventing.

def calculo_corners(df):
    
    lista_corners = []

    spain_corners = len(df[(df.event=='corner') & (df.team_name=='SPAIN')])
    r_corners = len(df[(df.event=='corner') & (df.team_name!='SPAIN')])
    
    lista_corners.append(spain_corners)
    lista_corners.append(r_corners)
    
    return lista_corners


def calculo_faltas(df):
    
    lista_faltas = []
    
    spain_faltas = len(df[(df.event=='freekick') & (df.team_name=='SPAIN')])
    spain_faltas_directas = len(df[(df.event=='freekick')  & (df.action_type=='direct') & (df.team_name=='SPAIN')])
    spain_faltas_realizadas = len(df[(df.event=='freekick') & (df.team_name!='SPAIN')])
    r_faltas = len(df[(df.event=='freekick') & (df.team_name!='SPAIN')])
    r_faltas_directas = len(df[(df.event=='freekick')  & (df.action_type=='direct') & (df.team_name!='SPAIN')])
    r_faltas_realizadas = len(df[(df.event=='freekick') & (df.team_name=='SPAIN')])
    
    lista_faltas.append(spain_faltas)
    lista_faltas.append(spain_faltas_directas)
    lista_faltas.append(spain_faltas_realizadas)
    lista_faltas.append(r_faltas)
    lista_faltas.append(r_faltas_directas)
    lista_faltas.append(r_faltas_realizadas)
    
    return lista_faltas


def calculo_penaltis(df):
    
    lista_penaltis=[]
    
    spain_penaltis = len(df[(df.event=='penalty') & (df.team_name=='SPAIN')])
    spain_penaltis_marcados = len(df[(df.event=='penalty')  & (df.outcome_additional=='goal') & (df.team_name=='SPAIN')])
    if spain_penaltis > 0:
        spain_porc_acierto_pm = round(spain_penaltis_marcados/spain_penaltis * 100, 1)
    else:
        spain_porc_acierto_pm = 'none'

    r_penaltis = len(df[(df.event=='penalty') & (df.team_name!='SPAIN')])
    r_penaltis_marcados = len(df[(df.event=='penalty')  & (df.outcome_additional=='goal') & (df.team_name!='SPAIN')])
    if r_penaltis > 0:
        r_porc_acierto_pm = round(r_penaltis_marcados/r_penaltis * 100, 1)
    else:
        r_porc_acierto_pm = 'none'
    
    lista_penaltis.append(spain_penaltis)
    lista_penaltis.append(spain_penaltis_marcados)
    lista_penaltis.append(spain_porc_acierto_pm)
    lista_penaltis.append(r_penaltis)
    lista_penaltis.append(r_penaltis_marcados)
    lista_penaltis.append(r_porc_acierto_pm)
    
    return lista_penaltis


def calculo_saques_banda(df):
     
    lista_saques_banda = []
    
    spain_saques_banda = len(df[(df.event=='throwin') & (df.team_name=='SPAIN')])
    spain_saques_banda_recepcionados = len(df[(df.event=='throwin')  & (df.outcome=='teammate_reception') & (df.team_name=='SPAIN')])
    spain_porc_acierto_sb = round(spain_saques_banda_recepcionados/spain_saques_banda * 100, 1)
    
    r_saques_banda = len(df[(df.event=='throwin') & (df.team_name!='SPAIN')])
    r_saques_banda_recepcionados = len(df[(df.event=='throwin')  & (df.outcome=='teammate_reception') & (df.team_name!='SPAIN')])
    r_porc_acierto_sb = round(r_saques_banda_recepcionados/r_saques_banda * 100, 1)
    
    lista_saques_banda.append(spain_saques_banda)
    lista_saques_banda.append(spain_saques_banda_recepcionados)
    lista_saques_banda.append(spain_porc_acierto_sb)
    lista_saques_banda.append(r_saques_banda)
    lista_saques_banda.append(r_saques_banda_recepcionados)
    lista_saques_banda.append(r_porc_acierto_sb)
    
    return lista_saques_banda


def calculo_ofrecimientos(df):

    lista_ofrecimientos = []
     
    spain_ofrecimientos = len(df[(df.event_type=='offering_to_receive') & (df.team_name=='SPAIN')])
    spain_ofrecimientos_offer = len(df[(df.event_type=='offering_to_receive')  & (df.event=='offer') & (df.team_name=='SPAIN')])
    spain_ofrecimientos_offer_camp_contr = len(df[(df.event_type=='offering_to_receive')  & (df.event=='offer') & (df.x_mirrored>0.5) & (df.team_name=='SPAIN')]) 
    spain_ofrecimientos_offer_ult_terc = len(df[(df.event_type=='offering_to_receive')  & (df.event=='offer') & (df.x_mirrored>0.66) & (df.team_name=='SPAIN')]) 
    
    r_ofrecimientos = len(df[(df.event_type=='offering_to_receive') & (df.team_name!='SPAIN')])
    r_ofrecimientos_offer = len(df[(df.event_type=='offering_to_receive')  & (df.event=='offer') & (df.team_name!='SPAIN')])
    r_ofrecimientos_offer_camp_contr = len(df[(df.event_type=='offering_to_receive')  & (df.event=='offer') & (df.x_mirrored>0.5) & (df.team_name!='SPAIN')]) 
    r_ofrecimientos_offer_ult_terc = len(df[(df.event_type=='offering_to_receive')  & (df.event=='offer') & (df.x_mirrored>0.66) & (df.team_name!='SPAIN')])    
    
    lista_ofrecimientos.append(spain_ofrecimientos)
    lista_ofrecimientos.append(spain_ofrecimientos_offer)
    lista_ofrecimientos.append(spain_ofrecimientos_offer_camp_contr)
    lista_ofrecimientos.append(spain_ofrecimientos_offer_ult_terc)
    lista_ofrecimientos.append(r_ofrecimientos)
    lista_ofrecimientos.append(r_ofrecimientos_offer)
    lista_ofrecimientos.append(r_ofrecimientos_offer_camp_contr)
    lista_ofrecimientos.append(r_ofrecimientos_offer_ult_terc)
    
    return lista_ofrecimientos


def calculo_remates(df):
    
    lista_remates = []
    
    spain_ocasiones = len(df[(df.event=='attempt_at_goal') & (df.team_name=='SPAIN')])
    spain_ocasiones_fa = len(df[(df.event=='attempt_at_goal') & (df.x_mirrored<0.83) &(df.team_name=='SPAIN')])
    spain_ocasiones_completadas = len(df[(df.event=='attempt_at_goal') & (df.team_name=='SPAIN') & (df.outcome=='on_target')])
    spain_ocasiones_completadas_fa = len(df[(df.event=='attempt_at_goal') & (df.x_mirrored<0.83) & (df.team_name=='SPAIN') & (df.outcome=='on_target')])
    spain_ocasiones_falladas = len(df[(df.event=='attempt_at_goal') & (df.team_name=='SPAIN') & (df.outcome=='off_target')])
    if spain_ocasiones > 0:
        spain_porc_acierto_ocasiones = round(spain_ocasiones_completadas/spain_ocasiones * 100, 1)
    else:
        spain_porc_acierto_ocasiones = 0
    spain_goles = len(df[(df.event=='attempt_at_goal') & (df.team_name=='SPAIN') & (df.outcome_additional=='goal')])
    spain_goles_fa = len(df[(df.event=='attempt_at_goal') & (df.x_mirrored<0.83) & (df.team_name=='SPAIN') & (df.outcome_additional=='goal')])    
    if spain_ocasiones > 0:
        spain_porc_acierto_goles = round(spain_goles/spain_ocasiones_completadas * 100, 1)
    else:
        spain_porc_acierto_goles = 0
    spain_goles_concedidos = len(df[(df.event=='attempt_at_goal') & (df.team_name!='SPAIN') & (df.outcome_additional=='goal')])
    
    r_ocasiones = len(df[(df.event=='attempt_at_goal') & (df.team_name!='SPAIN')])
    r_ocasiones_fa = len(df[(df.event=='attempt_at_goal') & (df.x_mirrored<0.83) &(df.team_name!='SPAIN')])
    r_ocasiones_completadas = len(df[(df.event=='attempt_at_goal') & (df.team_name!='SPAIN') & (df.outcome=='on_target')])
    r_ocasiones_completadas_fa = len(df[(df.event=='attempt_at_goal') & (df.x_mirrored<0.83) & (df.team_name!='SPAIN') & (df.outcome=='on_target')])
    r_ocasiones_falladas = len(df[(df.event=='attempt_at_goal') & (df.team_name=='SPAIN') & (df.outcome=='off_target')])
    if r_ocasiones > 0:
        r_porc_acierto_ocasiones = round(r_ocasiones_completadas/r_ocasiones * 100, 1)   
    else:
        r_porc_acierto_ocasiones=0
    r_goles = len(df[(df.event=='attempt_at_goal') & (df.team_name!='SPAIN') & (df.outcome_additional=='goal')])
    r_goles_fa = len(df[(df.event=='attempt_at_goal') & (df.x_mirrored<0.83) & (df.team_name!='SPAIN') & (df.outcome_additional=='goal')])
    if r_ocasiones > 0:
        r_porc_acierto_goles = round(r_goles/r_ocasiones_completadas * 100, 1)
    else:
        r_porc_acierto_goles=0
    r_goles_concedidos = len(df[(df.event=='attempt_at_goal') & (df.team_name=='SPAIN') & (df.outcome_additional=='goal')])
        
    lista_remates.append(spain_ocasiones)
    lista_remates.append(spain_ocasiones_fa)
    lista_remates.append(spain_ocasiones_completadas)
    lista_remates.append(spain_ocasiones_completadas_fa)
    lista_remates.append(spain_ocasiones_falladas)
    lista_remates.append(spain_porc_acierto_ocasiones)
    lista_remates.append(spain_goles)
    lista_remates.append(spain_goles_fa)
    lista_remates.append(spain_porc_acierto_goles)
    lista_remates.append(spain_goles_concedidos)
    lista_remates.append(r_ocasiones)
    lista_remates.append(r_ocasiones_fa)
    lista_remates.append(r_ocasiones_completadas)
    lista_remates.append(r_ocasiones_completadas_fa)
    lista_remates.append(r_ocasiones_falladas)
    lista_remates.append(r_porc_acierto_ocasiones)
    lista_remates.append(r_goles)
    lista_remates.append(r_goles_fa)
    lista_remates.append(r_porc_acierto_goles)  
    lista_remates.append(r_goles_concedidos) 
    
    return lista_remates      


def calculo_centros(df):
    
    lista_centros = []
    
    spain_centros = len(df[(df.event=='cross') & (df.team_name=='SPAIN')])
    spain_centros_completados = len(df[(df.event=='cross') & (df.team_name=='SPAIN') & (df.outcome=='possession_complete')])
    spain_asistencias_de_centro = len(df[(df.event=='cross') & (df.team_name=='SPAIN') & (df.outcome_additional=='assist')])

    r_centros = len(df[(df.event=='cross') & (df.team_name!='SPAIN')])
    r_centros_completados = len(df[(df.event=='cross') & (df.team_name!='SPAIN') & (df.outcome=='possession_complete')])
    r_asistencias_de_centro = len(df[(df.event=='cross') & (df.team_name!='SPAIN') & (df.outcome_additional=='assist')])

    lista_centros.append(spain_centros) 
    lista_centros.append(spain_centros_completados)  
    lista_centros.append(spain_asistencias_de_centro)  
    lista_centros.append(r_centros)  
    lista_centros.append(r_centros_completados)  
    lista_centros.append(r_asistencias_de_centro)  
    
    return lista_centros


def calculo_pases(df):
    
    lista_pases = []
    
    spain_pases = len(df[(df.event=='pass') & (df.team_name=='SPAIN')])
    spain_pases_completados = len(df[(df.event=='pass') & (df.team_name=='SPAIN') & (df.outcome=='possession_complete')])
    spain_porc_acierto_pases = round(spain_pases_completados/spain_pases * 100, 1)
    spain_pases_completados_linebreak = len(df[(df.event=='pass') & (df.team_name=='SPAIN') & (df.outcome=='possession_complete') & (df.line_break_outcome=='line_break_complete')])
    spain_asistencias = len(df[(df.event=='pass') & (df.team_name=='SPAIN') & (df.outcome_additional=='assist')])
    spain_cdj = len(df[(df.event=='pass') & (df.team_name=='SPAIN') & (df.outcome=='possession_complete') & (df.style_additional=='switch_of_play')])
    spain_pases_ultimo_tercio = len(df[(df.event=='pass') & (df.team_name=='SPAIN') & (df.x_mirrored>0.66)])
    spain_pases_completados_ultimo_tercio = len(df[(df.event=='pass') & (df.outcome=='possession_complete') & (df.team_name=='SPAIN') & (df.x_mirrored>0.66)])
    
    r_pases = len(df[(df.event=='pass') & (df.team_name!='SPAIN')])
    r_pases_completados = len(df[(df.event=='pass') & (df.team_name!='SPAIN') & (df.outcome=='possession_complete')])
    r_porc_acierto_pases = round(r_pases_completados/r_pases * 100, 1)
    r_pases_completados_linebreak = len(df[(df.event=='pass') & (df.team_name!='SPAIN') & (df.outcome=='possession_complete') & (df.line_break_outcome=='line_break_complete')])
    r_asistencias = len(df[(df.event=='pass') & (df.team_name!='SPAIN') & (df.outcome_additional=='assist')])
    r_cdj = len(df[(df.event=='pass') & (df.team_name!='SPAIN') & (df.outcome=='possession_complete') & (df.style_additional=='switch_of_play')])
    r_pases_ultimo_tercio = len(df[(df.event=='pass') & (df.team_name!='SPAIN') & (df.x_mirrored>0.66)])
    r_pases_completados_ultimo_tercio = len(df[(df.event=='pass') & (df.outcome=='possession_complete') & (df.team_name!='SPAIN') & (df.x_mirrored>0.66)])
    
    lista_pases.append(spain_pases)
    lista_pases.append(spain_pases_completados)
    lista_pases.append(spain_porc_acierto_pases)
    lista_pases.append(spain_pases_completados_linebreak)
    lista_pases.append(spain_asistencias)
    lista_pases.append(spain_cdj)
    lista_pases.append(spain_pases_ultimo_tercio)
    lista_pases.append(spain_pases_completados_ultimo_tercio)
    lista_pases.append(r_pases)
    lista_pases.append(r_pases_completados)
    lista_pases.append(r_porc_acierto_pases)
    lista_pases.append(r_pases_completados_linebreak)
    lista_pases.append(r_asistencias)
    lista_pases.append(r_cdj)
    lista_pases.append(r_pases_ultimo_tercio)
    lista_pases.append(r_pases_completados_ultimo_tercio)
    
    return lista_pases


def calculo_progresiones(df):
    
    lista_prog = []
    
    spain_prog = len(df[(df.event=='ball_progression') & (df.team_name=='SPAIN')])
    spain_intentos_regate = len(df[(df['style']=='take_on_1v1') & (df.team_name=='SPAIN')])
    spain_intentos_regate_ult_terc = len(df[(df['style']=='take_on_1v1') & (df.x_mirrored>0.66) & (df.team_name=='SPAIN')])
    spain_regates_exitosos = len(df[(df['style']=='take_on_1v1') & (df.outcome=='opposition_beaten') & (df.team_name=='SPAIN')])
    spain_regates_exitosos_ult_terc = len(df[(df['style']=='take_on_1v1') & (df.x_mirrored>0.66) & (df.outcome=='opposition_beaten') & (df.team_name=='SPAIN')])
       
    r_prog = len(df[(df.event=='ball_progression') & (df.team_name!='SPAIN')])
    r_intentos_regate = len(df[(df['style']=='take_on_1v1') & (df.team_name!='SPAIN')])
    r_intentos_regate_ult_terc = len(df[(df['style']=='take_on_1v1') & (df.x_mirrored>0.66) & (df.team_name!='SPAIN')])
    r_regates_exitosos = len(df[(df['style']=='take_on_1v1') & (df.outcome=='opposition_beaten') & (df.team_name!='SPAIN')])
    r_regates_exitosos_ult_terc = len(df[(df['style']=='take_on_1v1') & (df.x_mirrored>0.66) & (df.outcome=='opposition_beaten') & (df.team_name!='SPAIN')])
    
    lista_prog.append(spain_prog)
    lista_prog.append(spain_intentos_regate)
    lista_prog.append(spain_intentos_regate_ult_terc)    
    lista_prog.append(spain_regates_exitosos)
    lista_prog.append(spain_regates_exitosos_ult_terc)    
    lista_prog.append(r_prog)
    lista_prog.append(r_intentos_regate)
    lista_prog.append(r_intentos_regate_ult_terc)    
    lista_prog.append(r_regates_exitosos)
    lista_prog.append(r_regates_exitosos_ult_terc)
    
    return lista_prog


def calculo_recepciones(df):
    
    lista_recepciones=[]
    
    spain_rec = len(df[(df.event=='reception') & (df.team_name=='SPAIN')])
    spain_rec_bh = len(df[(df.event=='reception') & (df.team_name=='SPAIN') & (df.team_unit=='in_behind')])
    spain_rec_b34 = len(df[(df.event=='reception') & (df.team_name=='SPAIN') & (df.team_unit=='between_3_4')])
    spain_rec_b23 = len(df[(df.event=='reception') & (df.team_name=='SPAIN') & (df.team_unit=='between_2_3')])
    spain_rec_b12 = len(df[(df.event=='reception') & (df.team_name=='SPAIN') & (df.team_unit=='between_1_2')])
    spain_rec_interiores = len(df[(df.event=='reception') & (df.team_name=='SPAIN') & (df.team_shape=='inside')])
    spain_perc_rec_interiores = round(spain_rec_interiores / spain_rec * 100, 1)
    spain_rec_exteriores = len(df[(df.event=='reception') & (df.team_name=='SPAIN') & (df.team_shape=='outside')])
    spain_perc_rec_exteriores = round(spain_rec_exteriores / spain_rec * 100, 1)
    spain_rec_ut = len(df[(df.event=='reception') & (df.team_name=='SPAIN') & (df.x_mirrored>0.66)])
    
    r_rec = len(df[(df.event=='reception') & (df.team_name!='SPAIN')])
    r_rec_bh = len(df[(df.event=='reception') & (df.team_name!='SPAIN') & (df.team_unit=='in_behind')])
    r_rec_b34 = len(df[(df.event=='reception') & (df.team_name!='SPAIN') & (df.team_unit=='between_3_4')])
    r_rec_b23 = len(df[(df.event=='reception') & (df.team_name!='SPAIN') & (df.team_unit=='between_2_3')])
    r_rec_b12 = len(df[(df.event=='reception') & (df.team_name!='SPAIN') & (df.team_unit=='between_1_2')])
    r_rec_interiores = len(df[(df.event=='reception') & (df.team_name!='SPAIN') & (df.team_shape=='inside')])
    r_perc_rec_interiores = round(r_rec_interiores / r_rec * 100, 1)
    r_rec_exteriores = len(df[(df.event=='reception') & (df.team_name!='SPAIN') & (df.team_shape=='outside')])
    r_perc_rec_exteriores = round(r_rec_exteriores / r_rec * 100, 1)
    r_rec_ut = len(df[(df.event=='reception') & (df.team_name!='SPAIN') & (df.x_mirrored>0.66)])
    
    lista_recepciones.append(spain_rec)
    lista_recepciones.append(spain_rec_bh)
    lista_recepciones.append(spain_rec_b34)
    lista_recepciones.append(spain_rec_b23)
    lista_recepciones.append(spain_rec_b12)
    lista_recepciones.append(spain_rec_interiores)
    lista_recepciones.append(spain_perc_rec_interiores)
    lista_recepciones.append(spain_rec_exteriores)
    lista_recepciones.append(spain_perc_rec_exteriores)
    lista_recepciones.append(spain_rec_ut)
    lista_recepciones.append(r_rec)
    lista_recepciones.append(r_rec_bh)
    lista_recepciones.append(r_rec_b34)
    lista_recepciones.append(r_rec_b23)
    lista_recepciones.append(r_rec_b12)
    lista_recepciones.append(r_rec_interiores)
    lista_recepciones.append(r_perc_rec_interiores)
    lista_recepciones.append(r_rec_exteriores)
    lista_recepciones.append(r_perc_rec_exteriores)
    lista_recepciones.append(r_rec_ut)
    
    return lista_recepciones


def calculo_blocks(df):

    lista_blocks = []
    
    spain_blocks = len(df[(df.event=='block') & (df.team_name=='SPAIN')])
    r_blocks = len(df[(df.event=='block') & (df.team_name!='SPAIN')])
    
    lista_blocks.append(spain_blocks)
    lista_blocks.append(r_blocks)
    
    return lista_blocks


def calculo_despejes(df):

    lista_despejes = []
    
    spain_desp = len(df[(df.event=='clearance') & (df.team_name=='SPAIN')])
    r_desp = len(df[(df.event=='clearance') & (df.team_name!='SPAIN')])
    
    lista_despejes.append(spain_desp)
    lista_despejes.append(r_desp)    
    
    return lista_despejes


def calculo_intercepciones(df):

    lista_intercep = []
    
    spain_int = len(df[(df.event=='interception') & (df.team_name=='SPAIN')])
    r_int = len(df[(df.event=='interception') & (df.team_name!='SPAIN')])
    
    lista_intercep.append(spain_int)
    lista_intercep.append(r_int)
    
    return lista_intercep


def calculo_entradas(df):

    lista_entradas = []
    
    spain_ent = len(df[(df.event=='tackle') & (df.team_name=='SPAIN')])
    spain_ent_ex = len(df[(df.event=='tackle') & (df.team_name=='SPAIN') & (df.outcome=='possession_won')])
    spain_ent_ex_perc = round(spain_ent_ex / spain_ent * 100, 1)
    
    r_ent = len(df[(df.event=='tackle') & (df.team_name!='SPAIN')])
    r_ent_ex = len(df[(df.event=='tackle') & (df.team_name!='SPAIN') & (df.outcome=='possession_won')])
    r_ent_ex_perc = round(r_ent_ex / r_ent * 100, 1)
    
    lista_entradas.append(spain_ent)
    lista_entradas.append(spain_ent_ex)
    lista_entradas.append(spain_ent_ex_perc)
    lista_entradas.append(r_ent)
    lista_entradas.append(r_ent_ex)
    lista_entradas.append(r_ent_ex_perc)
    
    return lista_entradas


def calculo_toas(df):
    
    list_toas=[]

    spain_toas = len(df[(df.event=='take_on_against') & (df.team_name=='SPAIN')])
    r_toas = len(df[(df.event=='take_on_against') & (df.team_name!='SPAIN')])
    
    list_toas.append(spain_toas)
    list_toas.append(r_toas)
    
    return list_toas


def calculo_pushings_on(df):
    
    lista_push = []

    spain_push = len(df[(df.event=='pushing_on') & (df.team_name=='SPAIN')])
    r_push = len(df[(df.event=='pushing_on') & (df.team_name!='SPAIN')])
    
    lista_push.append(spain_push)
    lista_push.append(r_push)    
    
    return lista_push


def calculo_presion(df):
   
    lista_presion=[]

    spain_presion = len(df[(df.event=='pressing') & (df.team_name=='SPAIN')])
    spain_presion_directa = len(df[(df.event=='pressing') & (df.pressure=='direct_pressure') & (df.team_name=='SPAIN')])
    spain_presion_directa_perc = round(spain_presion_directa / spain_presion * 100, 1)
    
    r_presion = len(df[(df.event=='pressing') & (df.team_name!='SPAIN')])
    r_presion_directa = len(df[(df.event=='pressing') & (df.pressure=='direct_pressure') & (df.team_name!='SPAIN')])
    r_presion_directa_perc = round(r_presion_directa / r_presion * 100, 1)
    
    lista_presion.append(spain_presion)
    lista_presion.append(spain_presion_directa)
    lista_presion.append(spain_presion_directa_perc)
    lista_presion.append(r_presion)
    lista_presion.append(r_presion_directa)
    lista_presion.append(r_presion_directa_perc)
    
    return lista_presion


def gk_active_eng(df):
    
    lista_gk_active_eng = []

    spain_act_engagement = len(df[(df.event_type=='goal_keeping') & (df.event=='active_engagement') & (df.team_name=='SPAIN')])
    r_act_engagement = len(df[(df.event_type=='goal_keeping') & (df.event=='active_engagement') & (df.team_name!='SPAIN')])

    lista_gk_active_eng.append(spain_act_engagement)
    lista_gk_active_eng.append(r_act_engagement)
    
    return lista_gk_active_eng


def gk_aerial_control(df):
    
    lista_gk_aerial_control = []

    spain_gk_aerial_control = len(df[(df.event_type=='goal_keeping') & (df.event=='aerial_control') & (df.team_name=='SPAIN')])
    r_gk_aerial_control = len(df[(df.event_type=='goal_keeping') & (df.event=='aerial_control') & (df.team_name!='SPAIN')])

    lista_gk_aerial_control.append(spain_gk_aerial_control)
    lista_gk_aerial_control.append(r_gk_aerial_control)
    
    return lista_gk_aerial_control


def gk_def_support(df):
    
    lista_gk_def_support = []

    spain_gk_def_support = len(df[(df.event_type=='goal_keeping') & (df.event=='defensive_line_support') & (df.team_name=='SPAIN')])
    r_gk_def_support = len(df[(df.event_type=='goal_keeping') & (df.event=='defensive_line_support') & (df.team_name!='SPAIN')])

    lista_gk_def_support.append(spain_gk_def_support)
    lista_gk_def_support.append(r_gk_def_support)
    
    return lista_gk_def_support


def gk_goal_prevention(df):

    lista_gk_goal_prevention=[]
    
    spain_gk_goal_preventions = len(df[(df.event_type=='goal_keeping') & (df.event=='goal_prevention') & (df.team_name=='SPAIN')])
    spain_gk_goal_preventions_saved = len(df[(df.event_type=='goal_keeping') & (df.event=='goal_prevention') & (df.outcome=='complete') & (df.team_name=='SPAIN')]) 

    r_gk_goal_preventions = len(df[(df.event_type=='goal_keeping') & (df.event=='goal_prevention') & (df.team_name!='SPAIN')])
    r_gk_goal_preventions_saved = len(df[(df.event_type=='goal_keeping') & (df.event=='goal_prevention') & (df.outcome=='complete') & (df.team_name!='SPAIN')])
    
    lista_gk_goal_prevention.append(spain_gk_goal_preventions)
    lista_gk_goal_prevention.append(spain_gk_goal_preventions_saved)
    lista_gk_goal_prevention.append(r_gk_goal_preventions)
    lista_gk_goal_prevention.append(r_gk_goal_preventions_saved)
    
    return lista_gk_goal_prevention


def calculo_duelos(df):
    
    lista_duelos = []
    
    spain_total_duels = len(df[(df.category=='in_contest') & ((df.event=='duel') | (df.event=='physical_duel') | (df.event=='aerial_duel')) & (df.team_name=='SPAIN')])
    spain_total_duels_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & ((df.event=='duel') | (df.event=='physical_duel') | (df.event=='aerial_duel')) & (df.team_name=='SPAIN')])
    spain_perc_duels_won = round((spain_total_duels_won/spain_total_duels)*100)
    spain_duels_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & (df.event=='duel') & (df.team_name=='SPAIN')])
    spain_physical_duel_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & (df.event=='physical_duel') & (df.team_name=='SPAIN')])
    spain_aerial_duel_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & (df.event=='aerial_duel') & (df.team_name=='SPAIN')])

    r_total_duels = len(df[(df.category=='in_contest') & ((df.event=='duel') | (df.event=='physical_duel') | (df.event=='aerial_duel')) & (df.team_name!='SPAIN')])
    r_total_duels_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & ((df.event=='duel') | (df.event=='physical_duel') | (df.event=='aerial_duel')) & (df.team_name!='SPAIN')])
    r_perc_duels_won = round((r_total_duels_won/r_total_duels)*100)
    r_duels_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & (df.event=='duel') & (df.team_name!='SPAIN')])
    r_physical_duel_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & (df.event=='physical_duel') & (df.team_name!='SPAIN')])
    r_aerial_duel_won = len(df[(df.category=='in_contest') & (df.outcome_additional=='won') & (df.event=='aerial_duel') & (df.team_name!='SPAIN')])

    lista_duelos.append(spain_total_duels)
    lista_duelos.append(spain_total_duels_won)
    lista_duelos.append(spain_perc_duels_won)
    lista_duelos.append(spain_duels_won)
    lista_duelos.append(spain_physical_duel_won)
    lista_duelos.append(spain_aerial_duel_won)
    lista_duelos.append(r_total_duels)
    lista_duelos.append(r_total_duels_won)
    lista_duelos.append(r_perc_duels_won)
    lista_duelos.append(r_duels_won)
    lista_duelos.append(r_physical_duel_won)
    lista_duelos.append(r_aerial_duel_won)
    
    return lista_duelos


def calculo_sustituciones(df):
    
    lista_sustituciones = []
    
    spain_sub = len(df[(df.event_type=='substitution') & (df.team_name=='SPAIN')])
    r_sub = len(df[(df.event_type=='substitution') & (df.team_name!='SPAIN')])
                
    lista_sustituciones.append(spain_sub)
    lista_sustituciones.append(r_sub)
    
    return lista_sustituciones


def posesion(df): 
    
    lista_posesion=[]
    
    eventos_pos_esp = len(df[(df.category=='in_possession') & (df.team_name=='SPAIN')])
    eventos_pos_r = len(df[(df.category=='in_possession') & (df.team_name!='SPAIN')])
    eventos_pos_ic = len(df[(df.category=='in_contest')])
    
    posesion_total = eventos_pos_esp + eventos_pos_r + eventos_pos_ic
    posesion_spain = round(eventos_pos_esp / posesion_total * 100, 2)
    posesion_r = round(eventos_pos_r / posesion_total * 100, 2)
    posesion_ic = round(eventos_pos_ic / posesion_total * 100, 2)
    
    lista_posesion.append(posesion_spain)
    lista_posesion.append(posesion_r)
    lista_posesion.append(posesion_ic)
    
    return lista_posesion


def direccion_pases(df):  
    
    lista_direccion_pases = []

    spain_pases_verticales = len(df[(df.event=='pass') & (df.x_location_end_mirrored>(df.x_location_start_mirrored+0.1)) \
& ((df.y_location_end_mirrored<(df.y_location_start_mirrored+0.2)) & (df.y_location_end_mirrored>(df.y_location_start_mirrored-0.2)))
& (df.outcome=='possession_complete') & (df.team_name=='SPAIN')])
    spain_pases_adelante = len(df[(df.event=='pass') & (df.x_location_end_mirrored>(df.x_location_start_mirrored+0.1)) & (df.outcome=='possession_complete') & (df.team_name=='SPAIN')])
    spain_pases_atras = len(df[(df.event=='pass') & (df.x_location_end_mirrored<(df.x_location_start_mirrored-0.1)) & (df.outcome=='possession_complete') & (df.team_name=='SPAIN')])
    spain_pases_horizontales = (len(df[(df.event=='pass') & (df.x_location_end_mirrored>(df.x_location_start_mirrored-0.1)) & (df.x_location_end_mirrored<(df.x_location_start_mirrored+0.1)) 
& (df.outcome=='possession_complete') & (df.team_name=='SPAIN')]))
    spain_pases_totales = spain_pases_adelante+spain_pases_atras+spain_pases_horizontales
    spain_perc_pases_verticales = round((spain_pases_verticales / spain_pases_totales)*100)
    spain_perc_pases_adelante = round((spain_pases_adelante / spain_pases_totales)*100)
    spain_perc_pases_atras = round((spain_pases_atras / spain_pases_totales)*100)
    spain_perc_pases_horizontales = round((spain_pases_horizontales / spain_pases_totales)*100)

    r_pases_verticales = len(df[(df.event=='pass') & (df.x_location_end_mirrored>(df.x_location_start_mirrored+0.1)) \
& ((df.y_location_end_mirrored<(df.y_location_start_mirrored+0.2)) & (df.y_location_end_mirrored>(df.y_location_start_mirrored-0.2)))
& (df.outcome=='possession_complete') & (df.team_name!='SPAIN')])
    r_pases_adelante = (len(df[(df.event=='pass') & (df.x_location_end_mirrored>(df.x_location_start_mirrored+0.1)) & (df.outcome=='possession_complete') & (df.team_name!='SPAIN')]))
    r_pases_atras = len(df[(df.event=='pass') & (df.x_location_end_mirrored<(df.x_location_start_mirrored-0.1)) & (df.outcome=='possession_complete') & (df.team_name!='SPAIN')])
    r_pases_horizontales = (len(df[(df.event=='pass') & (df.x_location_end_mirrored>(df.x_location_start_mirrored-0.1)) & (df.x_location_end_mirrored<(df.x_location_start_mirrored+0.1)) 
& (df.outcome=='possession_complete') & (df.team_name!='SPAIN')]))
    r_pases_totales = r_pases_adelante+r_pases_atras+r_pases_horizontales
    r_perc_pases_verticales = round((r_pases_verticales / r_pases_totales)*100)
    r_perc_pases_adelante = round((r_pases_adelante / r_pases_totales)*100)
    r_perc_pases_atras = round((r_pases_atras / r_pases_totales)*100)
    r_perc_pases_horizontales = round((r_pases_horizontales / r_pases_totales)*100)

    
    lista_direccion_pases.append(spain_pases_verticales)
    lista_direccion_pases.append(spain_pases_adelante)
    lista_direccion_pases.append(spain_pases_atras)
    lista_direccion_pases.append(spain_pases_horizontales)
    lista_direccion_pases.append(spain_perc_pases_verticales)
    lista_direccion_pases.append(spain_perc_pases_adelante)
    lista_direccion_pases.append(spain_perc_pases_atras)
    lista_direccion_pases.append(spain_perc_pases_horizontales)
    lista_direccion_pases.append(r_pases_verticales)
    lista_direccion_pases.append(r_pases_adelante)
    lista_direccion_pases.append(r_pases_atras)
    lista_direccion_pases.append(r_pases_horizontales)
    lista_direccion_pases.append(r_perc_pases_verticales)
    lista_direccion_pases.append(r_perc_pases_adelante)
    lista_direccion_pases.append(r_perc_pases_atras)
    lista_direccion_pases.append(r_perc_pases_horizontales)
    
    return lista_direccion_pases


def recuperaciones(df):
    
    lista_recuperaciones = []
    
    spain_recuperaciones = len(df[(df.outcome=='possession_won') & (df.event!='possession_outcome') & (df.team_name=='SPAIN')])
    spain_recuperaciones_campo_contrario = len(df[(df.outcome=='possession_won') & (df.event!='possession_outcome') & (df.x_mirrored>0.5) & (df.team_name=='SPAIN')])
    spain_perc_rcc = round((spain_recuperaciones_campo_contrario / spain_recuperaciones)*100)
    spain_recuperaciones_campo_propio = len(df[(df.outcome=='possession_won') & (df.event!='possession_outcome') & (df.x_mirrored<0.5) & (df.team_name=='SPAIN')])
    spain_perc_rcp = round((spain_recuperaciones_campo_propio / spain_recuperaciones)*100)
    
    r_recuperaciones = len(df[(df.outcome=='possession_won') & (df.event!='possession_outcome') & (df.team_name!='SPAIN')])
    r_recuperaciones_campo_contrario = len(df[(df.outcome=='possession_won') & (df.event!='possession_outcome') & (df.x_mirrored>0.5) & (df.team_name!='SPAIN')])
    r_perc_rcc = round((r_recuperaciones_campo_contrario / r_recuperaciones)*100)
    r_recuperaciones_campo_propio = len(df[(df.outcome=='possession_won') & (df.event!='possession_outcome') & (df.x_mirrored<0.5) & (df.team_name!='SPAIN')])
    r_perc_rcp = round((r_recuperaciones_campo_propio / r_recuperaciones)*100)

    lista_recuperaciones.append(spain_recuperaciones)
    lista_recuperaciones.append(spain_recuperaciones_campo_contrario)
    lista_recuperaciones.append(spain_perc_rcc)
    lista_recuperaciones.append(spain_recuperaciones_campo_propio)
    lista_recuperaciones.append(spain_perc_rcp)
    lista_recuperaciones.append(r_recuperaciones)
    lista_recuperaciones.append(r_recuperaciones_campo_contrario)
    lista_recuperaciones.append(r_perc_rcc)
    lista_recuperaciones.append(r_recuperaciones_campo_propio)
    lista_recuperaciones.append(r_perc_rcp)
    
    return lista_recuperaciones


def recuperaciones1(df):
    
    lista_recuperaciones1 = []
    
    spain_recuperaciones = len(df[((df.outcome=='possession_won') | (df.outcome=='possession_out_of_play_won')) & (df.event!='possession_outcome') & (df.team_name=='SPAIN')])
    spain_recuperaciones_campo_contrario = len(df[((df.outcome=='possession_won') | (df.outcome=='possession_out_of_play_won')) & (df.event!='possession_outcome') & (df.x_mirrored>0.5) & (df.team_name=='SPAIN')])
    spain_perc_rcc = round((spain_recuperaciones_campo_contrario / spain_recuperaciones)*100)
    spain_recuperaciones_campo_propio = len(df[((df.outcome=='possession_won') | (df.outcome=='possession_out_of_play_won')) & (df.event!='possession_outcome') & (df.x_mirrored<0.5) & (df.team_name=='SPAIN')])
    spain_perc_rcp = round((spain_recuperaciones_campo_propio / spain_recuperaciones)*100)
    
    r_recuperaciones = len(df[((df.outcome=='possession_won') | (df.outcome=='possession_out_of_play_won')) & (df.event!='possession_outcome') & (df.team_name!='SPAIN')])
    r_recuperaciones_campo_contrario = len(df[((df.outcome=='possession_won') | (df.outcome=='possession_out_of_play_won')) & (df.event!='possession_outcome') & (df.x_mirrored>0.5) & (df.team_name!='SPAIN')])
    r_perc_rcc = round((r_recuperaciones_campo_contrario / r_recuperaciones)*100)
    r_recuperaciones_campo_propio = len(df[((df.outcome=='possession_won') | (df.outcome=='possession_out_of_play_won')) & (df.event!='possession_outcome') & (df.x_mirrored<0.5) & (df.team_name!='SPAIN')])
    r_perc_rcp = round((r_recuperaciones_campo_propio / r_recuperaciones)*100)

    lista_recuperaciones1.append(spain_recuperaciones)
    lista_recuperaciones1.append(spain_recuperaciones_campo_contrario)
    lista_recuperaciones1.append(spain_perc_rcc)
    lista_recuperaciones1.append(spain_recuperaciones_campo_propio)
    lista_recuperaciones1.append(spain_perc_rcp)
    lista_recuperaciones1.append(r_recuperaciones)
    lista_recuperaciones1.append(r_recuperaciones_campo_contrario)
    lista_recuperaciones1.append(r_perc_rcc)
    lista_recuperaciones1.append(r_recuperaciones_campo_propio)
    lista_recuperaciones1.append(r_perc_rcp)
    
    return lista_recuperaciones1


def perdidas(df):
    
    lista_perdidas = []

    spain_perdidas = len(df[(df.event=='possession_outcome') & ((df.outcome=='possession_lost') | (df.outcome=='possession_incomplete') | 
(df.outcome=='possession_out_of_play_lost'))  & (df.team_name=='SPAIN')])
    spain_perdidas_campo_prop = len(df[(df.event=='possession_outcome') & ((df.outcome=='possession_lost') | (df.outcome=='possession_incomplete') | 
(df.outcome=='possession_out_of_play_lost')) & (df.x_mirrored<0.5)  & (df.team_name=='SPAIN')])
    spain_perc_perdidas_campo_prop = round((spain_perdidas_campo_prop/spain_perdidas)*100)

    r_perdidas = len(df[(df.event=='possession_outcome') & ((df.outcome=='possession_lost') | (df.outcome=='possession_incomplete') | 
(df.outcome=='possession_out_of_play_lost'))  & (df.team_name!='SPAIN')])
    r_perdidas_campo_prop = len(df[(df.event=='possession_outcome') & ((df.outcome=='possession_lost') | (df.outcome=='possession_incomplete') | 
(df.outcome=='possession_out_of_play_lost')) & (df.x_mirrored<0.5)  & (df.team_name!='SPAIN')])
    r_perc_perdidas_campo_prop = round((r_perdidas_campo_prop/r_perdidas)*100)
    
    lista_perdidas.append(spain_perdidas)
    lista_perdidas.append(spain_perdidas_campo_prop)
    lista_perdidas.append(spain_perc_perdidas_campo_prop)
    lista_perdidas.append(r_perdidas)
    lista_perdidas.append(r_perdidas_campo_prop)
    lista_perdidas.append(r_perc_perdidas_campo_prop)
    
    return lista_perdidas


def disciplina(df):
    
    lista_disciplina = []
    
    spain_tarj_amarillas = len(df[(df.outcome_additional=='yellow_card') & (df.team_name=='SPAIN')])
    spain_tarj_rojas = len(df[(df.outcome_additional=='red_card') & (df.team_name=='SPAIN')])
    
    r_tarj_amarillas = len(df[(df.outcome_additional=='yellow_card') & (df.team_name!='SPAIN')])
    r_tarj_rojas = len(df[(df.outcome_additional=='red_card') & (df.team_name!='SPAIN')])
    
    lista_disciplina.append(spain_tarj_amarillas)
    lista_disciplina.append(spain_tarj_rojas)
    lista_disciplina.append(r_tarj_amarillas)
    lista_disciplina.append(r_tarj_rojas)
    
    return lista_disciplina


def metricas_partido(df):
      
    lista_estadisticas_spain = []
    lista_estadisticas_rival = []
    lista_partido = []
    
    match_id = df.match_id.unique()[0]
    team_name_1 = 'SPAIN'
    team_name_2 = df[df.team_name!='SPAIN'].team_name.unique()[0]
            
    lista_estadisticas_spain.append(match_id)
    lista_estadisticas_spain.append(team_name_1)  
    lista_estadisticas_spain.append(calculo_corners(df)[0])
    lista_estadisticas_spain.append(calculo_faltas(df)[0])  
    lista_estadisticas_spain.append(calculo_faltas(df)[1]) 
    lista_estadisticas_spain.append(calculo_faltas(df)[2]) 
    lista_estadisticas_spain.append(calculo_penaltis(df)[0]) 
    lista_estadisticas_spain.append(calculo_penaltis(df)[1]) 
    lista_estadisticas_spain.append(calculo_penaltis(df)[2]) 
    lista_estadisticas_spain.append(calculo_saques_banda(df)[0]) 
    lista_estadisticas_spain.append(calculo_saques_banda(df)[1]) 
    lista_estadisticas_spain.append(calculo_saques_banda(df)[2]) 
    lista_estadisticas_spain.append(calculo_ofrecimientos(df)[0]) 
    lista_estadisticas_spain.append(calculo_ofrecimientos(df)[1])
    lista_estadisticas_spain.append(calculo_ofrecimientos(df)[2])
    lista_estadisticas_spain.append(calculo_ofrecimientos(df)[3])
    lista_estadisticas_spain.append(calculo_remates(df)[0])
    lista_estadisticas_spain.append(calculo_remates(df)[1])
    lista_estadisticas_spain.append(calculo_remates(df)[2])
    lista_estadisticas_spain.append(calculo_remates(df)[3])
    lista_estadisticas_spain.append(calculo_remates(df)[4])
    lista_estadisticas_spain.append(calculo_remates(df)[5])
    lista_estadisticas_spain.append(calculo_remates(df)[6])
    lista_estadisticas_spain.append(calculo_remates(df)[7])
    lista_estadisticas_spain.append(calculo_remates(df)[8])
    lista_estadisticas_spain.append(calculo_remates(df)[9])
    lista_estadisticas_spain.append(calculo_centros(df)[0])
    lista_estadisticas_spain.append(calculo_centros(df)[1])
    lista_estadisticas_spain.append(calculo_centros(df)[2])
    lista_estadisticas_spain.append(calculo_pases(df)[0])
    lista_estadisticas_spain.append(calculo_pases(df)[1])
    lista_estadisticas_spain.append(calculo_pases(df)[2])
    lista_estadisticas_spain.append(calculo_pases(df)[3])
    lista_estadisticas_spain.append(calculo_pases(df)[4])
    lista_estadisticas_spain.append(calculo_pases(df)[5])
    lista_estadisticas_spain.append(calculo_pases(df)[6])
    lista_estadisticas_spain.append(calculo_pases(df)[7])
    lista_estadisticas_spain.append(calculo_progresiones(df)[0])
    lista_estadisticas_spain.append(calculo_progresiones(df)[1])
    lista_estadisticas_spain.append(calculo_progresiones(df)[2])
    lista_estadisticas_spain.append(calculo_progresiones(df)[3])
    lista_estadisticas_spain.append(calculo_progresiones(df)[4])
    lista_estadisticas_spain.append(calculo_recepciones(df)[0])
    lista_estadisticas_spain.append(calculo_recepciones(df)[1])
    lista_estadisticas_spain.append(calculo_recepciones(df)[2])
    lista_estadisticas_spain.append(calculo_recepciones(df)[3])
    lista_estadisticas_spain.append(calculo_recepciones(df)[4])
    lista_estadisticas_spain.append(calculo_recepciones(df)[5])
    lista_estadisticas_spain.append(calculo_recepciones(df)[6])
    lista_estadisticas_spain.append(calculo_recepciones(df)[7])
    lista_estadisticas_spain.append(calculo_recepciones(df)[8])
    lista_estadisticas_spain.append(calculo_recepciones(df)[9])
    lista_estadisticas_spain.append(calculo_blocks(df)[0])
    lista_estadisticas_spain.append(calculo_despejes(df)[0])
    lista_estadisticas_spain.append(calculo_intercepciones(df)[0])
    lista_estadisticas_spain.append(calculo_entradas(df)[0])
    lista_estadisticas_spain.append(calculo_entradas(df)[1])
    lista_estadisticas_spain.append(calculo_entradas(df)[2])
    lista_estadisticas_spain.append(calculo_toas(df)[0])
    lista_estadisticas_spain.append(calculo_pushings_on(df)[0])
    lista_estadisticas_spain.append(calculo_presion(df)[0])
    lista_estadisticas_spain.append(calculo_presion(df)[1])
    lista_estadisticas_spain.append(calculo_presion(df)[2])
    lista_estadisticas_spain.append(gk_active_eng(df)[0])
    lista_estadisticas_spain.append(gk_aerial_control(df)[0])
    lista_estadisticas_spain.append(gk_def_support(df)[0])
    lista_estadisticas_spain.append(gk_goal_prevention(df)[0])
    lista_estadisticas_spain.append(gk_goal_prevention(df)[1])
    lista_estadisticas_spain.append(calculo_duelos(df)[0])
    lista_estadisticas_spain.append(calculo_duelos(df)[1])
    lista_estadisticas_spain.append(calculo_duelos(df)[2])
    lista_estadisticas_spain.append(calculo_duelos(df)[3])
    lista_estadisticas_spain.append(calculo_duelos(df)[4])
    lista_estadisticas_spain.append(calculo_duelos(df)[5])
    lista_estadisticas_spain.append(calculo_sustituciones(df)[0])
    lista_estadisticas_spain.append(posesion(df)[0])
    lista_estadisticas_spain.append(posesion(df)[2])
    lista_estadisticas_spain.append(direccion_pases(df)[0])
    lista_estadisticas_spain.append(direccion_pases(df)[1])
    lista_estadisticas_spain.append(direccion_pases(df)[2])
    lista_estadisticas_spain.append(direccion_pases(df)[3])
    lista_estadisticas_spain.append(direccion_pases(df)[4])
    lista_estadisticas_spain.append(direccion_pases(df)[5])
    lista_estadisticas_spain.append(direccion_pases(df)[6])
    lista_estadisticas_spain.append(direccion_pases(df)[7])
    lista_estadisticas_spain.append(recuperaciones(df)[0])
    lista_estadisticas_spain.append(recuperaciones(df)[1])
    lista_estadisticas_spain.append(recuperaciones(df)[2])
    lista_estadisticas_spain.append(recuperaciones(df)[3])
    lista_estadisticas_spain.append(recuperaciones(df)[4])
    lista_estadisticas_spain.append(recuperaciones1(df)[0])
    lista_estadisticas_spain.append(recuperaciones1(df)[1])
    lista_estadisticas_spain.append(recuperaciones1(df)[2])
    lista_estadisticas_spain.append(recuperaciones1(df)[3])
    lista_estadisticas_spain.append(recuperaciones1(df)[4])
    lista_estadisticas_spain.append(perdidas(df)[0])
    lista_estadisticas_spain.append(perdidas(df)[1])
    lista_estadisticas_spain.append(perdidas(df)[2])
    lista_estadisticas_spain.append(disciplina(df)[0])
    lista_estadisticas_spain.append(disciplina(df)[1])
    
    
    lista_estadisticas_rival.append(match_id)
    lista_estadisticas_rival.append(team_name_2)
    lista_estadisticas_rival.append(calculo_corners(df)[1])
    lista_estadisticas_rival.append(calculo_faltas(df)[3])
    lista_estadisticas_rival.append(calculo_faltas(df)[4])
    lista_estadisticas_rival.append(calculo_faltas(df)[5])
    lista_estadisticas_rival.append(calculo_penaltis(df)[3]) 
    lista_estadisticas_rival.append(calculo_penaltis(df)[4]) 
    lista_estadisticas_rival.append(calculo_penaltis(df)[5]) 
    lista_estadisticas_rival.append(calculo_saques_banda(df)[3]) 
    lista_estadisticas_rival.append(calculo_saques_banda(df)[4]) 
    lista_estadisticas_rival.append(calculo_saques_banda(df)[5])
    lista_estadisticas_rival.append(calculo_ofrecimientos(df)[4])
    lista_estadisticas_rival.append(calculo_ofrecimientos(df)[5])
    lista_estadisticas_rival.append(calculo_ofrecimientos(df)[6])
    lista_estadisticas_rival.append(calculo_ofrecimientos(df)[7])
    lista_estadisticas_rival.append(calculo_remates(df)[10])
    lista_estadisticas_rival.append(calculo_remates(df)[11])
    lista_estadisticas_rival.append(calculo_remates(df)[12])
    lista_estadisticas_rival.append(calculo_remates(df)[13])
    lista_estadisticas_rival.append(calculo_remates(df)[14])
    lista_estadisticas_rival.append(calculo_remates(df)[15])
    lista_estadisticas_rival.append(calculo_remates(df)[16])
    lista_estadisticas_rival.append(calculo_remates(df)[17])
    lista_estadisticas_rival.append(calculo_remates(df)[18])
    lista_estadisticas_rival.append(calculo_remates(df)[19])
    lista_estadisticas_rival.append(calculo_centros(df)[3])
    lista_estadisticas_rival.append(calculo_centros(df)[4])
    lista_estadisticas_rival.append(calculo_centros(df)[5])
    lista_estadisticas_rival.append(calculo_pases(df)[8])
    lista_estadisticas_rival.append(calculo_pases(df)[9])
    lista_estadisticas_rival.append(calculo_pases(df)[10])
    lista_estadisticas_rival.append(calculo_pases(df)[11])
    lista_estadisticas_rival.append(calculo_pases(df)[12])
    lista_estadisticas_rival.append(calculo_pases(df)[13])
    lista_estadisticas_rival.append(calculo_pases(df)[14])
    lista_estadisticas_rival.append(calculo_pases(df)[15])
    lista_estadisticas_rival.append(calculo_progresiones(df)[5])
    lista_estadisticas_rival.append(calculo_progresiones(df)[6])
    lista_estadisticas_rival.append(calculo_progresiones(df)[7])
    lista_estadisticas_rival.append(calculo_progresiones(df)[8])
    lista_estadisticas_rival.append(calculo_progresiones(df)[9])
    lista_estadisticas_rival.append(calculo_recepciones(df)[10])
    lista_estadisticas_rival.append(calculo_recepciones(df)[11])
    lista_estadisticas_rival.append(calculo_recepciones(df)[12])
    lista_estadisticas_rival.append(calculo_recepciones(df)[13])
    lista_estadisticas_rival.append(calculo_recepciones(df)[14])
    lista_estadisticas_rival.append(calculo_recepciones(df)[15])
    lista_estadisticas_rival.append(calculo_recepciones(df)[16])
    lista_estadisticas_rival.append(calculo_recepciones(df)[17])
    lista_estadisticas_rival.append(calculo_recepciones(df)[18])
    lista_estadisticas_rival.append(calculo_recepciones(df)[19])
    lista_estadisticas_rival.append(calculo_blocks(df)[1])
    lista_estadisticas_rival.append(calculo_despejes(df)[1])
    lista_estadisticas_rival.append(calculo_intercepciones(df)[1])
    lista_estadisticas_rival.append(calculo_entradas(df)[3])
    lista_estadisticas_rival.append(calculo_entradas(df)[4])
    lista_estadisticas_rival.append(calculo_entradas(df)[5])
    lista_estadisticas_rival.append(calculo_toas(df)[1])
    lista_estadisticas_rival.append(calculo_pushings_on(df)[1])
    lista_estadisticas_rival.append(calculo_presion(df)[3])
    lista_estadisticas_rival.append(calculo_presion(df)[4])
    lista_estadisticas_rival.append(calculo_presion(df)[5])
    lista_estadisticas_rival.append(gk_active_eng(df)[1])
    lista_estadisticas_rival.append(gk_aerial_control(df)[1])
    lista_estadisticas_rival.append(gk_def_support(df)[1])
    lista_estadisticas_rival.append(gk_goal_prevention(df)[2])
    lista_estadisticas_rival.append(gk_goal_prevention(df)[3])
    lista_estadisticas_rival.append(calculo_duelos(df)[6])
    lista_estadisticas_rival.append(calculo_duelos(df)[7])
    lista_estadisticas_rival.append(calculo_duelos(df)[8])
    lista_estadisticas_rival.append(calculo_duelos(df)[9])
    lista_estadisticas_rival.append(calculo_duelos(df)[10])
    lista_estadisticas_rival.append(calculo_duelos(df)[11])
    lista_estadisticas_rival.append(calculo_sustituciones(df)[1])
    lista_estadisticas_rival.append(posesion(df)[1])
    lista_estadisticas_rival.append(posesion(df)[2])
    lista_estadisticas_rival.append(direccion_pases(df)[8])
    lista_estadisticas_rival.append(direccion_pases(df)[9])
    lista_estadisticas_rival.append(direccion_pases(df)[10])
    lista_estadisticas_rival.append(direccion_pases(df)[11])
    lista_estadisticas_rival.append(direccion_pases(df)[12])
    lista_estadisticas_rival.append(direccion_pases(df)[13])
    lista_estadisticas_rival.append(direccion_pases(df)[14])
    lista_estadisticas_rival.append(direccion_pases(df)[15])
    lista_estadisticas_rival.append(recuperaciones(df)[5])
    lista_estadisticas_rival.append(recuperaciones(df)[6])
    lista_estadisticas_rival.append(recuperaciones(df)[7])
    lista_estadisticas_rival.append(recuperaciones(df)[8])
    lista_estadisticas_rival.append(recuperaciones(df)[9])
    lista_estadisticas_rival.append(recuperaciones1(df)[5])
    lista_estadisticas_rival.append(recuperaciones1(df)[6])
    lista_estadisticas_rival.append(recuperaciones1(df)[7])
    lista_estadisticas_rival.append(recuperaciones1(df)[8])
    lista_estadisticas_rival.append(recuperaciones1(df)[9])
    lista_estadisticas_rival.append(perdidas(df)[3])
    lista_estadisticas_rival.append(perdidas(df)[4])
    lista_estadisticas_rival.append(perdidas(df)[5])
    lista_estadisticas_rival.append(disciplina(df)[2])
    lista_estadisticas_rival.append(disciplina(df)[3])
    
    lista_partido.append(lista_estadisticas_spain)
    lista_partido.append(lista_estadisticas_rival)    
    
    columnas = ['match_id', 'team', 'corners', 'faltas_lanzadas', 'faltas_directas_lanzadas', 'faltas_realizadas', 'penaltis',
    'penaltis_marcados', '%_acierto_penaltis', 'saques_banda', 'saques_banda_recepcionados', '%_acierto_sb',
    'ofrecimientos', 'ofrecimientos_con_movimiento', 'ofrecimientos_con_movimiento_camp_contr', 'ofrecimientos_con_movimiento_ult_terc', 
    'remates_totales', 'remates_totales_fa', 'remates_on_target', 'remates_on_target_fa', 'remates_off_target',
    '%_remates_on_target', 'goles', 'goles_fa', '%_gol/on_target', 'goles_concedidos', 'centros_totales', 'centros_completados', 'asistencias_centro',
    'pases', 'pases_completados', '%_acierto_pases', 'pases_completados_linebreak', 'asistencias_pase',
    'cambios_de_juego', 'pases_ultimo_tercio', 'pases_completados_ultimo_tercio', 'progresiones', 'intentos_regate',
    'intentos_regate_ult_terc', 'regates_completados', 'regates_completados_ult_terc', 'recepciones', 'recep_behind', 'recep_3_4', 'recep_2_3', 'recep_1_2', 
    'recep_inside', '%_recep_inside', 'recep_outside', '%_recep_outside', 'recep_ultimo_tercio', 'bloqueos', 'despejes',
    'intercepciones', 'entradas_totales', 'entradas_exitosas', '%_entradas_exitosas', 'take_on_against', 'pushing-on',
    'presiones', 'presiones_directas', '%_presion_directa', 'gk_active_eng', 'gk_aerial_control', 'gk_def_support',
    'gk_goalprevention_tot', 'gk_goalprevention_tot_saved', 'duelos_totales', 'duelos_totales_ganados', '%_duelos_totales_ganados',
    'duelos_campo_ganados', 'duelos_físicos_ganados', 'duelos_aereos_ganados', 'sustituciones', 'posesion',
    'posesión_disputa', 'pases_verticales', 'pases_adelante','pases_atras','pases_horizontales','%_pases_verticales',
    '%_pases_adelante', '%_pases_atras',  '%_pases_horizontales', 'recuperaciones', 'recuperaciones_campo_contr', 
    '%_recuperaciones_campo_contr', 'recuperaciones_campo_prop', '%_recuperaciones_campo_prop', 'recuperaciones1', 
    'recuperaciones_campo_contr1', '%_recuperaciones_campo_contr1', 'recuperaciones_campo_prop1', '%_recuperaciones_campo_prop1',
    'perdidas', 'perdidas_campo_prop', '%_perdidas_campo_prop', 'tarj_amarillas', 'tarjetas_rojas']
    
    df_estadisticas = pd.DataFrame(lista_partido, columns = columnas)
    
    return df_estadisticas


### Funciones para cálculo de métricas y estadísticas de cada partido mediante la transformaación de los datos del tracking.

def distancia_recorrida(df):
    
    lista_distancia_recorrida=[]
    
    spain_distancia_recorrida = df[df.Team=='Spain']['Distance (m)'].sum()/1000
    spain_runs_15_20 = df[df.Team=='Spain']['Number of speed runs (15-20km/h)'].sum()
    spain_runs_mas20 = df[df.Team=='Spain']['Number of sprints (>20km/h)'].sum()
        
    rival_distancia_recorrida = df[df.Team!='Spain']['Distance (m)'].sum()/1000
    rival_runs_15_20 = df[df.Team!='Spain']['Number of speed runs (15-20km/h)'].sum()
    rival_runs_mas20 = df[df.Team!='Spain']['Number of sprints (>20km/h)'].sum()
        
    lista_distancia_recorrida.append(spain_distancia_recorrida)
    lista_distancia_recorrida.append(spain_runs_15_20)
    lista_distancia_recorrida.append(spain_runs_mas20)
    
    lista_distancia_recorrida.append(rival_distancia_recorrida)
    lista_distancia_recorrida.append(rival_runs_15_20)
    lista_distancia_recorrida.append(rival_runs_mas20)
    
    return lista_distancia_recorrida


def velocidad_media_equipo(df):
    
    lista_velocidad_media_equipos = []
    
    spain_vme_total = 0
    for i in df[df.Team=='Spain']['Player']:
        peso = list(df[df.Player==i]['Distance (m)'])[0] / df[df.Team=='Spain']['Distance (m)'].sum()
        vmj = peso * list(df[df.Player==i]['Average Speed (km/h'])[0]
        spain_vme_total += vmj 
        
    rival_vme_total = 0
    for i in df[df.Team!='Spain']['Player']:
        peso = list(df[df.Player==i]['Distance (m)'])[0] / df[df.Team!='Spain']['Distance (m)'].sum()
        vmj = peso * list(df[df.Player==i]['Average Speed (km/h'])[0]
        rival_vme_total += vmj 
        
    lista_velocidad_media_equipos.append(spain_vme_total)
    lista_velocidad_media_equipos.append(rival_vme_total)    
        
    return lista_velocidad_media_equipos


def metricas_tracking_partido(df):
    
    lista_estadisticas_tr_spain = []
    lista_estadisticas_tr_rival = []
    lista_tr_partido = []
    
    team_name_1 = 'Spain'
    team_name_2 = df[df.Team!='Spain'].Team.unique()[0]
            
    lista_estadisticas_tr_spain.append(team_name_1)  
    lista_estadisticas_tr_spain.append(distancia_recorrida(df)[0])
    lista_estadisticas_tr_spain.append(distancia_recorrida(df)[1]) 
    lista_estadisticas_tr_spain.append(distancia_recorrida(df)[2])
    lista_estadisticas_tr_spain.append(velocidad_media_equipo(df)[0])
 
    lista_estadisticas_tr_rival.append(team_name_2)
    lista_estadisticas_tr_rival.append(distancia_recorrida(df)[3])
    lista_estadisticas_tr_rival.append(distancia_recorrida(df)[4])
    lista_estadisticas_tr_rival.append(distancia_recorrida(df)[5])
    lista_estadisticas_tr_rival.append(velocidad_media_equipo(df)[1])   
    
    lista_tr_partido.append(lista_estadisticas_tr_spain)
    lista_tr_partido.append(lista_estadisticas_tr_rival)    
    
    columnas = ['team', 'distancia_recorrida_km', 'n_speed_runs_(15-20km/h)', 'n_of_sprints_(>20km/h)', 
    'total_average_speed_(km/h)']
    
    df_estadisticas_tr = pd.DataFrame(lista_tr_partido, columns = columnas)
    
    return df_estadisticas_tr


### Función para cálculo de minutos jugados acumulados por cada jugador mediante la transformaación de los datos del eventing.

def minutos_jugados(df, df_minutos):
    for i in df_minutos.player_id:
        if i in df.from_player_id.unique():
            if i not in df[df.event=='substitution_on'].from_player_id.unique() and i not in df[df.event=='substitution_on'].to_player_id.unique():
                if df.match_time_in_min.max()<105:
                    index = df_minutos[df_minutos.player_id==i].index[0]
                    df_minutos.at[index,'minutos_jugados']+=90
                else:
                    index = df_minutos[df_minutos.player_id==i].index[0]
                    df_minutos.at[index,'minutos_jugados']+=120
            else:
                if i in df[df.event=='substitution_on'].from_player_id.unique():
                    minutos_jugados = list(df[(df.event=='substitution_on') & (df.from_player_id==i)].match_time_in_min)[0]
                    index = df_minutos[df_minutos.player_id==i].index[0]
                    df_minutos.at[index,'minutos_jugados']+=minutos_jugados
                else:
                    if df.match_time_in_min.max()<105:
                        minutos_jugados = 90 - list(df[(df.event=='substitution_on') & (df.to_player_id==i)].match_time_in_min)[0]
                        index = df_minutos[df_minutos.player_id==i].index[0]
                        df_minutos.at[index,'minutos_jugados']+=minutos_jugados
                    else:
                        minutos_jugados = 120 - list(df[(df.event=='substitution_on') & (df.to_player_id==i)].match_time_in_min)[0]
                        index = df_minutos[df_minutos.player_id==i].index[0]
                        df_minutos.at[index,'minutos_jugados']+=minutos_jugados
    return df_minutos

