import re

#function for check the elements of the list if contain not valid
#operator or not valid digit or the nums of digit is longer

def check_list_valid(check_list, regex_verify):
  have_invalid_operator = False

  for i in check_list:
    if not re.search(regex_verify, i):
      have_invalid_operator = True
      break

  return have_invalid_operator


def arithmetic_arranger(problems, want_total=None):

  arranged_problems = ""

  num1, num2, sym_equal, total = [], [], [], []
  space_op = "    "

  if len(problems) > 5:
    arranged_problems = "Error: Too many problems."
  elif check_list_valid(problems, "^\w+\ [\+|\-]\ \w+$"):
    arranged_problems = "Error: Operator must be '+' or '-'."
  elif check_list_valid(problems, "^\d+\ [\+|\-]\ \d+$"):
    arranged_problems = "Error: Numbers must only contain digits."
  elif check_list_valid(problems, "^\d{1,4}\ [\+|\-]\ \d{1,4}$"):
    arranged_problems = "Error: Numbers cannot be more than four digits."
  else:
    for a in problems:
      list_operation = a.split(" ")
      space = len(list_operation[0]) if len(list_operation[0]) >= len(
        list_operation[2]) else len(list_operation[2])
      num1.append(list_operation[0].rjust(space + 2))
      num2.append(list_operation[1] + " " + list_operation[2].rjust(space))
      sym_equal.append("-" * (space + 2))

      if want_total == True:
        total.append(str(eval(a)).rjust(space + 2))

    arranged_problems = space_op.join(num1) + "\n" + space_op.join(
      num2) + "\n" + space_op.join(sym_equal)

    if want_total == True:
      arranged_problems = arranged_problems + "\n" + space_op.join(total)

  return arranged_problems
