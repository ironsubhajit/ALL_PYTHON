# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
    valid = True
    credit = input().strip() #123445678998/1234-2341-5678-3245
    creditWithOutHyphen = credit.replace("-", "")
    len_16 = bool(re.match(r"^[456]\d{15}$", credit)) #123445678998
    len_19 = bool(re.match(r"^[456]\d{3}-\d{4}-\d{4}-\d{4}$", credit))#1234-2341-5678-3245
    consecutive_num = bool(re.findall(r"(\d)\1\1\1", creditWithOutHyphen))
    if len_16 or len_19:
        if consecutive_num:
            valid = False
    else:
        valid = False
    print("Valid" if valid else "Invalid")