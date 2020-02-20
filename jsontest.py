import json
import csv


# Opening JSON file and loading the data 
# into the variable data 
json_file = open("fullresponse.json", "rU")
json_data = json.load(json_file)
print(json_data)

outFile = open("10years_histdata.csv", "w")

outWriter = csv.writer(outFile)

for id in json_data["data"]:
	row_array = []
	for attribute in id:
		row_array.append(id[attribute])
	outWriter.writerow(row_array)

#for formations in json_data["data"]:
#	for attribute in formations:
#		row_array.append(formations[attribute])
#	for attribute in weather_report:
#		row_array.append(weather_report[attribute])

#for weather_report in json_data["data"]:
#	row_array3 = []
#	for attribute in weather:
#		row_array3.append(weather_report[attribute])
#	outWriter.writerow(row_array3)

#fixture_data = datalist['data']

# now we will open a file for writing 
#data_file = open('1920updated.csv', 'w')

# create the csv writer object 
#csv_writer = csv.writer(data_file)

# Counter variable used for writing 
# headers to the CSV file 
#count = 0

#for id in fixture_data:
#	if count == 0:

		# Writing headers of CSV file 
#		header = id.keys()
#		csv_writer.writerow(header)
#		count += 1

	# Writing data of CSV file 
#	csv_writer.writerow(id.values())

#data_file.close()
