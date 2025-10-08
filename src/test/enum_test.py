from enum import Enum


class MyEnum(Enum):
    A = "Value_A"
    B = "Value_B"
    C = "Value_C"


print(MyEnum['A'])