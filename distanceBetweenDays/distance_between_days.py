class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]


class DistanceBetweenDays:
    def __init__(self, d1, d2):
        _dt1 = d1.split('/')
        _dt2 = d2.split('/')
        self.d1 = Date(int(_dt1[0]), int(_dt1[1]), int(_dt1[2]))
        self.d2 = Date(int(_dt2[0]), int(_dt2[1]), int(_dt2[2]))
        if self.d1.y < 1900:
            raise ValueError("Start date should be greater than 01/01/1900")
        if self.d2.y > 2999:
            raise ValueError("End date should be less than 31/12/2999")

    @staticmethod
    def count_leap_years(d):
        years = d.y
        if d.m <= 2:
            years -= 1
        return int(years / 4) - int(years / 100) + int(years / 400)

    def get_difference(self):
        n1 = self.d1.y * 365 + self.d1.d
        for i in range(0, self.d1.m - 1):
            n1 += monthDays[i]
        n1 += self.count_leap_years(self.d1)

        n2 = self.d2.y * 365 + self.d2.d
        for i in range(0, self.d2.m - 1):
            n2 += monthDays[i]
        n2 += self.count_leap_years(self.d2)

        return n2 - n1 - 1


if __name__ == '__main__':
    dt1 = raw_input("Enter Date1 in DD/MM/YYYY: ")
    dt2 = raw_input("Enter Date2 in DD/MM/YYYY: ")
    print("{0} days".format(DistanceBetweenDays(dt1, dt2).get_difference()))
