from django.shortcuts import render
from .models import Antenna
# from map.utils import load_antennas_from_csv # Miayn ashxtacnel projecti arajin RUN-i depqum

def index(request):
    # load_antennas_from_csv()  # Miayn ashxtacnel projecti arajin RUN-i depqum
    antennas = Antenna.objects.all()
    return render(request, 'map/map.html', {'antennas': antennas})