class Solution:
    def myAtoi(self, input):
        sign = 1
        result = 0
        index = 0
        n = len(input)

        #INT_MAX = pow(2,31) - 1
        #INT_MIN = -pow(2,31)

        # Discard all spaces from the beginning of the input string.
        while index < n and input[index] == ' ':
            index += 1

        # sign = +1, if it's positive number, otherwise sign = -1.
        if index < n and input[index] == '+':
            sign = 1
            index += 1
        elif index < n and input[index] == '-':
            sign = -1
            index += 1

        # Traverse next digits of input and stop if it is not a digit.
        # End of string is also non-digit character.
        while index < n and input[index].isdigit():
            digit = int(input[index])
            print(result)
            print(digit)

            # Check overflow and underflow conditions.
            #if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
            #    # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
            #    return INT_MAX if sign == 1 else INT_MIN

            # Append current digit to the result.
            result = 10 * result + digit
            index += 1

        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result

s= Solution()
str=" 234 -457 -word"
res=s.myAtoi(str)
print(res)

#We need to implement a function that converts the given string into a signed 32-bit integer.Intuitively, we could build the output number out of the input string by iterating over it character by character. However, we stop building the number when a non-digit character is spotted, or the number becomes too large to fit inside a 32-bit signed integer. In the latter case, we need to clamp the result to fit the range.