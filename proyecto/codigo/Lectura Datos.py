
import csv
##from pympler.asizeof import asizeof
##import time

##print(asizeof(self.data)/1024/1024)
##start = time.time()
##print(tiem.time()-start)


class Lectura:
    data = []
    column = []
    students = []

    def main(self):
        size = -1
        with open('datos4.csv', encoding='utf-8', mode='r') as file:
            read_csv = csv.reader(file, delimiter=';')
            for row in read_csv:
                if (size == -1):
                    self.column = (row)
                    size += 1
                else:
                    self.data.append(row)
                    size += 1
        file.close()
        for row in range(len(self.data)):
            self.students.append(self.data [row][0])

    def get_student(self,student_code):
        for i in range(len(self.data)):
            if (student_code == self.data[i][0]):
                print(self.data[i])

    def get_student_data(self, student_code, column_name):
        column_num = -1
        for i in range(len(self.column)):
            if (self.column[i] == column_name):
                column_num = i

        for i in range(len(self.data)):
            if (student_code == self.data[i][0]):
                print(self.data[i][column_num])

    def add_student(self,student):
        self.data.append(student)


