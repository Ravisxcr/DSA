class Student:
    pass

if __name__ == "__main__":

    s1 = Student()
    s1.name = "ravi"
    print(type(s1))
    print(s1.name)

    print("\n To display attributes as dictionary")
    print(s1.__dict__)

    print("\nTo check attributes of the s1")
    print(hasattr(s1,"name"))

    print("\nTo display value of attributes")
    print(getattr(s1,"name"))