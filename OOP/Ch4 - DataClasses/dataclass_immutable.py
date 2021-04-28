from dataclasses import dataclass


@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0


obj = ImmutableClass()
print(obj.value1)


obj.value1("something")  # not allowed will throw exception
print(obj.value1)