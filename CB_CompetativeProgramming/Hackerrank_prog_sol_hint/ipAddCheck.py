import re


class MyRegex:
    def __init__(self, strIp: str):
        self.strIp = strIp

    def check_ip(self) -> bool:
        zero_to_255 = "(\\d{1,2}|(0|1)\\d{2}|2[0-4]\\d|25[0-5])"
        regex = "^" + zero_to_255 + "\\." \
                + zero_to_255 + "\\." \
                + zero_to_255 + "\\." \
                + zero_to_255 + "$"
        print(f"search item: {self.strIp}")
        print(f"matched item: {re.search(regex, self.strIp)}")
        result = bool(re.search(regex, self.strIp))
        return result


if __name__ == '__main__':
    test_case = int(input("Test Case: "))
    test = list(map(str, input("values:\n").strip().split()))
    status = list()
    for i in range(len(test)):
        checker = MyRegex(test[i])
        status.append(str(checker.check_ip()))
        if checker.check_ip():
            print("Test Case Passed")
        else:
            print("Test Case Failed!")

    if all(_ == 'True' for _ in status):
        print("All Test Case Passed!")
    elif all(_ == 'False' for _ in status):
        print("All Test Case Failed!")
    else:
        print("Some Test case Failed!")

