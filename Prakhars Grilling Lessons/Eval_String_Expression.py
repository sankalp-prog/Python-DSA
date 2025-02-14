# for 1 - 100, prints foo when number is divisible by 15, prints bar if divisible by 10 and foobar if divisible by 15 and 10

# def test(num):
#     if num % 30 == 0:
#         return 'foobar'
#     elif num % 15 == 0:
#         return 'foo'
#     elif num % 10 == 0:
#         return 'bar'
#     else:
#         return 'none'


# example = '(((1+2)*3)+4)*5'
# Goal: Solve using recursion


# def inner_expression(expression, operator):
#     breaker = expression.index(operator)
#     result = ""
#     if operator == '(':
#         end_breaker = ')'
#         result = expression[breaker+1:end_breaker]
#     else:
#         result = expression[:breaker] + expression[breaker+1:]
#     return result


def find_matching_closing_parenthesis_index(expression, start_index):
    count = 0
    sub_expression = expression[start_index:]
    for i in range(len(sub_expression)):
        if sub_expression[i] == "(":
            count += 1
        if sub_expression[i] == ")":
            count -= 1
            if count == 0:
                return i + start_index


# print(find_matching_closing_parenthesis_index(problem1, 2))

operators = ["/", "*", "-", "+"]


def eval_non_bracket_expression(problem_string):
    for i,letter  in enumerate(problem_string):
        if letter in operators:
            temp_left_side = problem_string[:i]
            temp_right_side = problem_string[i + 1 :]
            if any(char in operators for char in temp_left_side):
                temp_left_side = eval_non_bracket_expression(temp_left_side)
            if any(char in operators for char in temp_right_side):
                temp_right_side = eval_non_bracket_expression(temp_right_side)
            if letter == "/":
                return str(int(temp_left_side) / int(temp_right_side))
            elif letter == "*":
                return str(int(temp_left_side) * int(temp_right_side))
            elif letter == "-":
                return str(int(temp_left_side) - int(temp_right_side))
            elif letter == "+":
                return str(int(temp_left_side) + int(temp_right_side))


def eval_expression(problem_string):
    """
    >>> eval_expression("(((1+2)*3)+4)*5")
    '65'
    >>> eval_expression("1*2+3+3+3")
    '11'
    """
    if len(problem_string) == 0:
        return ""
    if (problem_string[0] in operators) or (problem_string[-1] in operators):
        return problem_string
    if "(" in problem_string:
        start_index = problem_string.index("(")
        end_index = find_matching_closing_parenthesis_index(problem_string, start_index)
        # end_index = problem_string.index(")")
        left_side = problem_string[:start_index]
        right_side = problem_string[end_index + 1 :]
        middle = problem_string[start_index + 1 : end_index]
        return eval_expression(
            eval_expression(left_side)
            + eval_expression(middle)
            + eval_expression(right_side)
        )
    return eval_non_bracket_expression(problem_string)



if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)


problem1 = "(((1+2)*3)+4)*5"  # 65
problem2 = "(1+2)+(3+4)"  # 10

# print(eval_expression(problem1))
# print(eval_expression(problem2))
# print(eval_expression('1'))
# print(eval_expression('1*2+3+3'))
print(eval_non_bracket_expression("1*2+3+3+3"))
# print(eval_expression('(2*2)+3'))
# print(eval_expression('2*(2+3)'))
