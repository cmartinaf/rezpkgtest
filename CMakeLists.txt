cmake_minimum_required(VERSION 2.8)
include(RezBuild)

file(GLOB_RECURSE py_files "python/*.py")

rez_install_python(
    py
    FILES ${py_files}
    DESTINATION .
    LOCAL_SYMLINK
)

file(GLOB bin_files "bin/*")

#rez_install_files(
#    ${bin_files}
#    DESTINATION .
#    EXECUTABLE
#    LOCAL_SYMLINK
#)

file(GLOB etc_files "etc/*")

#rez_install_files(
#    ${etc_files}
#    DESTINATION .
#    EXECUTABLE
#    LOCAL_SYMLINK
#)
