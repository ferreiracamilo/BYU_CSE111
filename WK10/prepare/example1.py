# Example 1

try:
    # Write normal code here. This block must include
    # code that falls into two groups:
    # 1. Code that may cause an exception to be raised
    # 2. Code that depends on the results of the code
    #    in the first group
    print("try")
except ZeroDivisionError as zero_div_err:
    # Code that the computer executes if the code in the try
    # block caused a function to raise a ZeroDivisionError.
    print(zero_div_err)
except ValueError as val_err:
    # Code that the computer executes if the code in the
    # try block caused a function to raise a ValueError.
    print(val_err)
except (TypeError, KeyError, IndexError) as error:
    # Code that the computer executes if the code in the
    # try block caused a function to raise a TypeError,
    # KeyError, or IndexError.
    print(error)
except Exception as excep:
    # Code that the computer executes if the code in the try
    # block caused a function to raise any exception that
    # was not handled by one of the previous except blocks.
    print(excep)
except:
    # Code that the computer executes if the code in the
    # try block caused a function to raise anything that
    # was not handled by one of the previous except blocks.
    print("last except")
else:
    # Code that the computer executes after the code
    # in the try block if the code in the try block
    # did not cause any function to raise an exception.
    print("else")
finally:
    # Code that the computer executes after all the other
    # code in try, except, and else blocks regardless of
    # whether an exception was raised or not.Copy code to the clipboard
    print("finally")