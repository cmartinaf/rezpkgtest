CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)

set(package_version $ENV{REZ_BUILD_PROJECT_VERSION})
set(package_name $ENV{REZ_BUILD_PROJECT_NAME})

set(install_option --prefix=${CMAKE_INSTALL_PREFIX})

if(${REZ_BUILD_INSTALL})
    set(install_cmd pip install --ignore-installed --install-option=${install_option} --no-deps ${package_name}==${package_version})    
else()
    set(install_cmd "")
endif()

add_custom_target(
    pip_install
    ALL
    COMMAND ${install_cmd}
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
    VERBATIM
)

add_custom_target(
    install_shell_script    
    ALL
    COMMAND PYTHONPATH=${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages ${CMAKE_INSTALL_PREFIX}/bin/activate-global-python-argcomplete --dest=- > ${CMAKE_INSTALL_PREFIX}/argcomplete.sh
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
    VERBATIM
)

add_dependencies(install_shell_script pip_install)
