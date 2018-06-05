class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        summation = 0
        size = len(self.scores)
        for i in self.scores:
            summation += i
        grade = summation / size

        if (grade >= 90 and grade <= 100):
            grade = "O"
        elif (grade >= 80 and grade < 90):
            grade = "E"
        elif (grade >= 70 and grade < 80):
            grade = "A"
        elif (grade >= 55 and grade < 70):
            grade = "P"
        elif (grade >= 40 and grade < 50):
            grade = "D"
        else:
            grade = "T"
        return grade
