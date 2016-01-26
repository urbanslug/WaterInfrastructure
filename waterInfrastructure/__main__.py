import waterInfrastructure.waterInfrastructure as waterInfrastructure

if __name__ == "__main__":
    x = waterInfrastructure.calculate("https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json")
    print (x)
