actual = input()
actual = list(map(int, actual.split(" ")))

expected = input()
expected = list(map(int, expected.split(" ")))

actualDate = actual[0]
actualMonth = actual[1]
actualYear = actual[2]

expectedDate = expected[0]
expectedMonth = expected[1]
expectedYear = expected[2]

fine = 0

if actualYear > expectedYear:
    fine = 10000
elif actualYear == expectedYear: #Same calender year
    if actualMonth > expectedMonth: #checking months
        fine = 500 * (actualMonth - expectedMonth)
    elif actualMonth == expectedMonth: #check dates now
        if actualDate > expectedDate:
            fine = 15 * (actualDate - expectedDate)
print(fine)
