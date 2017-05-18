import os
import settings
import sys
from shapely.geometry import Polygon


class WaterCalculator:
    def __init__(self):
        self.user=settings.validateUser()
        self.extents=settings.getExtents()
        self.polygon=''
        self.area=0
        self.panVolume=0
        self.dailyUsage=0

    def createPolygon(self):
        print('Creating the Polygon and computing area...')

        poly=Polygon(self.extents)
        self.polygon=poly
        self.area=poly.area

    def calculate(self):
        print('Calculating Volume: Assuming default units are meters...')

        self.panVolume=self.area*0.3*1000

        x=sys.argv[3]
        self.dailyUsage=int(x) * self.area

    def housekeeping(self):
        print('User: {}'.format(self.user))
        print('Pan Volume: {} Litres'.format(self.panVolume))
        print('Daily Water Usage: {} Litres'.format(self.dailyUsage))

def main():
    calculator=WaterCalculator()
    calculator.createPolygon()
    calculator.calculate()
    calculator.housekeeping()

if __name__=='__main__':
    if len(sys.argv)==4:
        if sys.argv[2].isdigit():
            main()
        else:
            raise ValueError('Parameter Two Should Be Numeric')
    else:
        raise ValueError('Tool Takes Exactly Three Parameters')    
