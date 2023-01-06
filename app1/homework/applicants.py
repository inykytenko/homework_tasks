class Education:
    def print(self):
        pass

    def collect_docs(self) -> int:
        pass


class School(Education):
    _docs = []
    def __int__(self, docs = []):
        self._docs = []

    @property
    def documents(self):
        return self._docs

    @documents.setter
    def documents(self, value):
        self._docs = value

    def print(self):
        print("The applicant enters on the basis of school education")

    def collect_docs(self) -> int:
        c_docs = self.documents
        user_action = int(input("Enter the number which of the listed documents you have. (1) school certificate and appendix, (2) certificate ZNO, (3) SSN, (4) passport, (5) military ticket, (6) exit: "))
        if user_action == 1:
            c_docs.append("School certificate and appendix")
            print(c_docs)

        elif user_action == 2:
            c_docs.append("certificate ZNO")
            print(c_docs)

        elif user_action == 3:
            c_docs.append("SSN")
            print(c_docs)

        elif user_action == 4:
            c_docs.append("passport")
            print(c_docs)

        elif user_action == 5:
            c_docs.append("military ticket")
            print(c_docs)

        elif user_action == 6:
            return 0

        else:
            print("Command is not valid.")

        self.documents = c_docs

        return 1

class College(Education):
    _docs = []
    def __int__(self, docs = []):
        self._docs = []

    @property
    def documents(self):
        return self._docs

    @documents.setter
    def documents(self, value):
        self._docs = value

    def print(self):
        print("The applicant enters on the basis of education at the college")

    def collect_docs(self) -> int:
        c_docs = self.documents
        user_action = input("Enter the number which of the listed documents you have. (1) college certificate, (2) certificate ZNO, (3) SSN, (4) passport, (5) military ticket, (6) exit: ")
        user_action = user_action.strip()

        if user_action == 1:
            c_docs.append("College certificate")
            print(c_docs)

        elif user_action == 2:
            c_docs.append("certificate ZNO")
            print(c_docs)

        elif user_action == 3:
            c_docs.append("SSN")
            print(c_docs)

        elif user_action == 4:
            c_docs.append("passport")
            print(c_docs)

        elif user_action == 5:
            c_docs.append("military ticket")
            print(c_docs)

        else:
            print("Command is not valid.")

        self.documents = c_docs

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

        user_action_gpa = input("Enter the type of score do you have. (1) school gpa, (2) college gpa, (3) zno, (4) exit: ")
        user_action = user_action.strip()
        
        if







def main():
    choose_education = int(input("1. Does the applicant enter on the basis of school education?, 2. Does the applicant enter on the basis of college education. Type 1 or 2: "))
    factory = Factory()
    obj = factory.create(choose_education)
    obj.print()
    result = 1
    while result == 1:
        result = obj.collect_docs()

    print(obj.documents)


main()