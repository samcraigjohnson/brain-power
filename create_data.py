from pynia import NIA, NiaData
import random
import time

training_options = ["up-left", "up", "up-right", "left", "center", "right", "down-left", "down", "down-right", "click"]

curr_option = training_options[0]

training_file = open("./training_data.txt", 'w')

mili = 50

def get_random_option():
	new_num = random.randint(0, len(training_options) -1) 	 
	return training_options[new_num]

def collect_data(curr_option, nia_data, nia):
	print curr_option
	nia_data.get_data_nia(nia)
	data = nia_data.Processed_Data
	training_file.write("*****")
	for number in data.tolist():
		training_file.write(str(number)+"\n")
	training_file.write("%"+curr_option+"%")

# open the NIA, or exit with a failure code
nia = NIA()
if not nia.open():
	sys.exit(1)

nia_data = NiaData(mili)

print "Get Ready. Training about to begin."
time.sleep(.5)
print "3"
time.sleep(1.0)
print "2"
time.sleep(1.0)
print "1"
time.sleep(1.0)
print "Start..."
time.sleep(1.0)

for i in range(2500):
	if (i % 50) == 0:
		curr_option = get_random_option()
	collect_data(curr_option, nia_data, nia)
	time.sleep(.08)

training_file.close()
