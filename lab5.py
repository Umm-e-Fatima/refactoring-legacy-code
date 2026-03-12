#LEGACY CODE
def compute_stats(file):
    total = 0
    summation = 0
    average = 0
    minimum = 0
    maximum = 0
    try:
        with open(file, "r") as f:
            line = f.readline().strip()
            first_line = int(line)
            minimum = first_line
            maximum = first_line

            while line:
                num = int(line)
                total += 1
                summation += num
                if minimum > num:
                    minimum = num
                if maximum < num:
                    maximum = num

                line = f.readline().strip()

        print("Total =", total)
        print("Summation =", summation)
        print("Average =", round(summation / total))
        print("Minimum =", minimum)
        print("Maximum =", maximum)
    except IOError:
        print("Error reading file")
# main function
compute_stats("random_nums.txt")











#REFACTORED CODE:

class ComputeStatistics:
    # constructor
    def __init__(self, file):
        self.file = file

    # read integers from file
    def read_int(self):
        data = []

        try:
            with open(self.file, "r") as f:
                for line in f:
                    data.append(int(line.strip()))
        except IOError:
            print("Error reading file")
        return data

    # count numbers
    def count(self):
        data = self.read_int()
        return len(data)

    # calculate sum
    def summation(self):
        data = self.read_int()
        return sum(data)

    # calculate average
    def average(self):
        return self.summation() / self.count()

    # find minimum
    def minimum(self):
        data = self.read_int()
        return min(data)

    # find maximum
    def maximum(self):
        data = self.read_int()
        return max(data)

# main program
file = "random_nums.txt"
cs = ComputeStatistics(file)
print("Values in file:", cs.read_int())
print("Total values:", cs.count())
print("Summation:", cs.summation())
print("Average:", cs.average())
print("Minimum:", cs.minimum())
print("Maximum:", cs.maximum())