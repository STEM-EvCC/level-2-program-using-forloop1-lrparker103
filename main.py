mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

mission_amount= (len(mission_names))

firstline = f"Total number of missions: {mission_amount}"

successfull_true = 0
for success in mission_success:
    if success ==True:
        successfull_true += 1





