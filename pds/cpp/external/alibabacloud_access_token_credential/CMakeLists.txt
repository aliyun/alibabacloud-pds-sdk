find_package(alibabacloud_access_token_credential QUIET)

if(alibabacloud_access_token_credential_FOUND)
  message(STATUS "Found alibabacloud_access_token_credential version ${alibabacloud_access_token_credential_VERSION}")
else()
  message(STATUS "alibabacloud_access_token_credential could not be located, Building alibabacloud_access_token_credential instead.")
  include(FetchContent)

  FetchContent_Declare(
    _alibabacloud_access_token_credential
    GIT_REPOSITORY https://github.com/alibabacloud-sdk-cpp/pds-credentials.git
    GIT_TAG master
    CMAKE_ARGS
      -DENABLE_UNIT_TESTS:BOOL="0")

  FetchContent_GetProperties(_alibabacloud_access_token_credential)
  if(NOT _alibabacloud_access_token_credential_POPULATED)
    FetchContent_Populate(_alibabacloud_access_token_credential)
    message(STATUS "Added alibabacloud_access_token_credential source : ${_alibabacloud_access_token_credential_SOURCE_DIR}")
    message(STATUS "Added alibabacloud_access_token_credential binary : ${_alibabacloud_access_token_credential_BINARY_DIR}")
    add_subdirectory(
      ${_alibabacloud_access_token_credential_SOURCE_DIR}
      ${_alibabacloud_access_token_credential_BINARY_DIR}
    )
  endif()
  target_include_directories(alibabacloud_pds PRIVATE "${_alibabacloud_access_token_credential_SOURCE_DIR}/include")
endif()
