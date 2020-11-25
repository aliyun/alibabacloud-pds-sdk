find_package(alibabacloud_roautil QUIET)

if(alibabacloud_roautil_FOUND)
  message(STATUS "Found alibabacloud_roautil version ${alibabacloud_roautil_VERSION}")
else()
  message(STATUS "alibabacloud_roautil could not be located, Building alibabacloud_roautil instead.")
  include(FetchContent)

  FetchContent_Declare(
    _alibabacloud_roautil
    GIT_REPOSITORY https://github.com/alibabacloud-sdk-cpp/roautil.git
    GIT_TAG master
    CMAKE_ARGS
      -DENABLE_UNIT_TESTS:BOOL="0")

  FetchContent_GetProperties(_alibabacloud_roautil)
  if(NOT _alibabacloud_roautil_POPULATED)
    FetchContent_Populate(_alibabacloud_roautil)
    message(STATUS "Added alibabacloud_roautil source : ${_alibabacloud_roautil_SOURCE_DIR}")
    message(STATUS "Added alibabacloud_roautil binary : ${_alibabacloud_roautil_BINARY_DIR}")
    add_subdirectory(
      ${_alibabacloud_roautil_SOURCE_DIR}
      ${_alibabacloud_roautil_BINARY_DIR}
    )
  endif()
  target_include_directories(alibabacloud_pds PRIVATE "${_alibabacloud_roautil_SOURCE_DIR}/include")
endif()
