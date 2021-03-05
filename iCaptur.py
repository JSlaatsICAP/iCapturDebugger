#exercises iCapturApp
from exercises import bicycle_crunch
from exercises import birddog
from exercises import bridge
from exercises import burpee
from exercises import calf_raises
from exercises import crabwalk
from exercises import forward_lunge
from exercises import hurksprong
from exercises import jumping_jacks
from exercises import plank
from exercises import push_ups
from exercises import reverse_plank
from exercises import side_plank
from exercises import single_leg_bridge
from exercises import single_leg_deadlift
from exercises import single_leg_squat
from exercises import squat
from exercises import superman
from exercises import triceps_dips
from exercises import windshield_wiper
from exercises import schaatssprong

#exercises nierstichting
from exercises import achterwaarts_strekken_been_links
from exercises import achterwaarts_strekken_been_rechts
from exercises import krachtoefening_achterzijde_knie_links
from exercises import krachtoefening_achterzijde_knie_rechts
from exercises import strekking_benen_links
from exercises import strekking_benen_rechts
from exercises import voorwaarts_heffen_beide_armen_stok
from exercises import zijwaarts_heffen_beide_armen
from exercises import zijwaarts_heffen_been_links
from exercises import zijwaarts_heffen_been_rechts
from exercises import rotatie_romp_stok

def analyze(data, exercise):     
    splitData = globals()[exercise].detect(data)
    result = globals()[exercise].analyse(splitData)
    print("amount of detected exercises = ",len(splitData))    
    print(result)