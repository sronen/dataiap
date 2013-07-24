import csv
import numpy

def read_csv(file_name, cols, check_reliable):
    reader = csv.DictReader(open(file_name, 'rU'))
    rows = {} # map "statename__countyname" to the column names in cols
    for row in reader:
        if check_reliable and row['Unreliable'] == "x": # discard unreliable data
            continue
        if row['County'] == "": # ignore the first entry for each state
            continue
        rname = "%s__%s" % (row['State'], row['County'])
        try: # if a row[col] is empty, float(row[col]) throws an exception
            rows[rname] = [float(row[col]) for col in cols]
        except:
            pass
    return rows


def get_arrs(dependent_cols, independent_cols):
	    ypll = read_csv("../../dataiap/datasets/county_health_rankings/ypll.csv", dependent_cols, True)
	    measures = read_csv("../../dataiap/datasets/county_health_rankings/additional_measures_cleaned.csv", independent_cols, False)

	    ypll_arr = []
	    measures_arr = []
	    for key, value in ypll.iteritems():
	        if key in measures: # join ypll and measures if county is in both
	            ypll_arr.append(value[0])
	            measures_arr.append(measures[key])
	    return (numpy.array(ypll_arr), numpy.array(measures_arr))

##########

dependent_cols = ["YPLL Rate"]
independent_cols = ["Population", "< 18", "65 and over", "African American",
	"Female", "Rural", "%Diabetes" , "HIV rate",
	"Physical Inactivity" , "mental health provider rate",
	"median household income", "% high housing costs",
	"% Free lunch", "% child Illiteracy", "% Drive Alone"]

ypll_arr, measures_arr = get_arrs(dependent_cols, independent_cols)
print ypll_arr.shape
print measures_arr[:,6].shape

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 8))

subplot = fig.add_subplot(311)
subplot.scatter(measures_arr[:,7], ypll_arr, color="#1f77b4") # :,7 means all rows of "HIV"
subplot.set_title("ypll vs. HIV patients")

subplot = fig.add_subplot(312)
subplot.scatter(measures_arr[:,4], ypll_arr, color="#1f77b4") # 4 = female
subplot.set_title("ypll vs. % female")

subplot = fig.add_subplot(313)
subplot.scatter(measures_arr[:,12], ypll_arr, color="#1f77b4") # 12 = lunch
subplot.set_title("ypll vs. % free lunch")

plt.savefig('three-scatters-exercise.png', format='png')

exit()