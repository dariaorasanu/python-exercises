from my_package import submodul1
from my_package import submodul2

if __name__ == '__main__':
    print(submodul1.hello_from_the_first_submodule())
    print(submodul2.hello_from_the_second_submodule())
    print(submodul1.add(4, 5))
    print(submodul2.multiply(4, 5))

