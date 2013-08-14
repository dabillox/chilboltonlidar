'''
Created on 31 Jul 2013

@author: danielfisher

“Copyright 2013 Daniel Fisher”

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Python wget equivalent to rip
Chilbolton data
'''
import urllib 
import os
import datetime 
import sys

def main():
    
    #set up loop
    start_date = datetime.date(2003,01,01)
    end_date = datetime.date(2008,12,31)
    d = start_date
    delta = datetime.timedelta(days=1)
    while d <= end_date:
         
        #set up url
        url = 'http://www.cloud-net.org/quicklooks/data/chilbolton/products/classification/' \
                + str(d.strftime("%Y")) \
                + '/' + str(d.strftime("%Y%m%d")) \
                + '_chilbolton_classification.png'
                
        #check if exists
        code = urllib.urlopen(url).code
        if (code / 100 >= 4):
            print "No data for ", str(d.strftime("%Y%m%d")), ' continuing...'
            d += delta
            continue

        #check size
        urllib.urlretrieve(url, str(d.strftime("%Y%m%d")) + '.png')
        
        #increment date
        print 'Succesfully retrieved ', str(d.strftime("%Y%m%d")), ' moving on...'
        d += delta

if __name__ == "__main__":
    sys.exit(main())
