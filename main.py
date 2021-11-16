import pandas as pd
import matplotlib.pyplot as plt

from src.criterio_fall import *
from src.fall_cicle import *
from src.sexo_hos import *
from src.sexo_pos import *

data = pd.read_csv("data/falle_hos_vac.csv", sep=',')

criterio_fallecidos_bar("img/criterio_fall.jpg", data)
criterio_fallecidos_pie("img/fall_circle.jpg", data)
sexo_hos("img/sexo_hospitalizado.jpg", data)
sexo_pos("img/sexo_positividad.jpg", data)