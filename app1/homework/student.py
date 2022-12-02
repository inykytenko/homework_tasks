# class Education:
#     # def __int__(self):
#     #     self._docs = []
#     #
#     # @property
#     # def docs(self) -> list:
#     #     return self._docs
#     #
#     # @docs.setter
#     # def docs(self, value):
#     #     self._docs = value
#
#     def print(self):
#         pass
#
#     def collect_docs(self) -> int:
#         pass


class School(object):
    def __int__(self):
        self.docs = []

    @property
    def documents(self):
        return self.docs

    @documents.setter
    def documents(self, value):
        self.docs = value

    def print(self):
        print("The applicant enters on the basis of school education")

    def collect_docs(self) -> int:
        c_docs = self.documents
        user_action = input("Enter which of the listed documents you have. School certificate and appendix, certificate ZNO, SSN, passport, military ticket, exit: ")
        user_action = user_action.strip()
        if 'School certificate and appendix' in user_action:
            c_docs.append("School certificate and appendix")
            print(c_docs)

        elif 'certificate ZNO' in user_action:
            c_docs.append("certificate ZNO")
            print(c_docs)

        elif 'SSN' in user_action:
            c_docs.append("SSN")
            print(c_docs)

        elif 'passport' in user_action:
            c_docs.append("passport")
            print(c_docs)

        elif 'military ticket' in user_action:
            c_docs.append("military ticket")
            print(c_docs)

        elif 'exit' in user_action:
            return 0

        else:
            print("Command is not valid.")

        self.update_docs(c_docs)

        return 1


class College(object):
    def __int__(self):
        self._docs = []

    @property
    def docs(self) -> list:
        return self._docs

    @docs.setter
    def docs(self, value):
        self._docs = value

    def print(self):
        print("The applicant enters on the basis of education at the college")

    def collect_docs(self) -> int:
        c_docs = self.docs
        user_action = input("Enter which of the listed documents you have. College certificate, certificate ZNO, SSN, passport, military ticket, exit: ")
        user_action = user_action.strip()

        if 'College certificate' in user_action:
            c_docs.append("College certificate")
            print(c_docs)

        elif 'certificate ZNO' in user_action:
            c_docs.append("certificate ZNO")
            print(c_docs)

        elif 'SSN' in user_action:
            c_docs.append("SSN")
            print(c_docs)

        elif 'passport' in user_action:
            c_docs.append("passport")
            print(c_docs)

        elif 'military ticket' in user_action:
            c_docs.append("military ticket")
            print(c_docs)

        elif 'exit' in user_action:
            return 0

        else:
            print("Command is not valid.")

        self.update_docs(c_docs)

        return 1


class Factory:
    def create(self, choose_input: int) -> object:
        school_education = 1
        college_education = 2
        if choose_input == school_education:
            return School()
        elif choose_input == college_education:
            return College()
        else:
            raise Exception(f"No supported input: {choose_input}")

# class Grade:
#     def create(self, choose_input: int)-> Education:
#         gpa_school_check = 7
#         gpa_college_check = 75
#         zno_check = 95




def main():
    choose_education = int(input("1. Абітурієнт вступає на базі шкільної освіти?, 2. Aбітурієнт вступає на базі освіти в колледжі. Напишіть 1 чи 2: "))
    factory = Factory()
    obj = factory.create(choose_education)
    obj.print()
    result = 1
    while result == 1:
        result = obj.collect_docs()

    print(obj.get_docs())


main()
