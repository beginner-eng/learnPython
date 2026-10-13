# import My_Package.Pmodule1
# import My_Package.Pmodule2
# My_Package.Pmodule1.info_print()
# My_Package.Pmodule2.info_print2()

from My_Package import Pmodule1
Pmodule1.info_print()

from My_Package.Pmodule2 import info_print2
info_print2()