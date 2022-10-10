import urllib.request
import os
import csv



def download(url):
    #print('aaa')
    filename = url.split('/')[-1]
    if(os.path.exists(filename)):
        print("File already exists")
    else:
        print("Downloading file")
        urllib.request.urlretrieve(url, filename)
        print("Download complete")
    return filename

def parseCSV(fName):
    reader = csv.DictReader(open(fName))

    result = {}
    for row in reader:
        for column, value in row.items():  # consider .iteritems() for Python 2
            result.setdefault(column, []).append(value)
    return result



if __name__ == "__main__":
    #print('bbb')
    fName = download('https://gis.data.cnra.ca.gov/datasets/CALFIRE-Forestry::recent-large-fire-perimeters-5000-acres.csv') # download https://gis.data.cnra.ca.gov/datasets/CALFIRE-Forestry::recent-large-fire-perimeters-5000-acres.csv if it doesn't exist

    csv = parseCSV(fName) # parse the csv file
    #print(repr(csv)) # print the csv file
    # find out the starting year of the data
    lowerYear = int(min(csv['YEAR_']))
    upperYear = int(max(csv['YEAR_']))
    print("The data starts from year " + str(lowerYear) + " to year " + str(upperYear))

    # find out number of in total
    print("There are " + str(len(csv['YEAR_'])) + " fires in total")

    # find out number of fires in each year
    for year in range(lowerYear, upperYear+1):
        print("There are " + str(csv['YEAR_'].count(str(year))) + " fires in year " + str(year))

    # find out the year with largest value in GIS_ACRES
    maxAcres = max(csv['GIS_ACRES'])
    fIndex = csv['GIS_ACRES'].index(maxAcres)
    print("The year with largest value in GIS_ACRES is " + str(csv['YEAR_'][fIndex])+'it has a name of'+str(csv['FIRE_NAME'][fIndex])+'and it has a size of'+str(csv['GIS_ACRES'][fIndex])+'with OBJECTID of'+str(csv['\ufeffOBJECTID'][fIndex]))

    # find out the total acreage burned in each year
    for year in range(lowerYear, upperYear+1):
        print("The total acreage burned in year " + str(year) + " is " + str(sum([float(i) for i in csv['GIS_ACRES'] if csv['YEAR_'][csv['GIS_ACRES'].index(i)] == str(year)])))

