from detecto.core import Model 
from detecto.visualize import detect_live

model = Model()
 

 
  
detect_live(model, score_filter=0.8)