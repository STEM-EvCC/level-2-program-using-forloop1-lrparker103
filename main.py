mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

mission_amount= (len(mission_names))

first_line = f"Total number of missions: {mission_amount}"


successfull_true = 0
for success in mission_success:
    if success ==True:
        successfull_true += 1


second_line = f"Number of successful missions: {successfull_true}"

only_true_success =[]
for true in mission_success:
    if true ==True:
        only_true_success.append(true)

true_amount =(len(only_true_success))

total_amount= (len(mission_success))

success_rate_decimal = true_amount / total_amount
success_rate_percent = f"{success_rate_decimal *100:.2f}%"

