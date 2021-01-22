file = open("test.csv", "r")
original_data = file.readlines()
training_data = []
for i in range(1, len(original_data)):
    training_data.append(original_data[i])
header = training_data[0]

def uniqueValues(rows, col):
    return set([row[col] for row in rows])
    
print(uniqueValues(training_data, 0))