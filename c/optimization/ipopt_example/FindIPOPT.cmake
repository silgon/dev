# includes
SET(POSSIBLE_INC_PATHS 
  /usr/include
  /usr/include/coin
  /usr/include/coin/ThirdParty
  /usr/local/include
  /usr/local/include/coin
  /usr/local/include/coin/ThirdParty
  )
FIND_PATH(IPOPT_INCLUDE_DIR NAMES IpIpoptApplication.hpp defs.h
  PATHS
  ${POSSIBLE_INC_PATHS}
)
FIND_PATH(IPOPT_THIRDPARTY_INCLUDE_DIR NAMES defs.h
  PATHS
  ${POSSIBLE_INC_PATHS}
)

SET(IPOPT_INCLUDE_DIRS ${IPOPT_INCLUDE_DIR} ${IPOPT_THIRDPARTY_INCLUDE_DIR})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -DHAVE_CSTDDEF")

# libraries
SET(POSSIBLE_LIB_PATHS
  /lib/
  /usr/lib/
  /usr/local/lib 
  /usr/lib/gcc/x86_64-linux-gnu/4.8 
  /usr/lib/x86_64-linux-gnu 
  /opt/local/lib
  )

SET(LIBS ipopt lapack dl coinmumps blas gfortran m quadmath coinmetis)
FOREACH (LIB ${LIBS})
  FIND_LIBRARY(FOUND_${LIB} NAMES ${LIB}
    PATHS ${POSSIBLE_LIB_PATHS})
  SET(IPOPT_LIBRARIES ${IPOPT_LIBRARIES} ${FOUND_${LIB}})
ENDFOREACH(LIB)

IF (IPOPT_INCLUDE_DIRS AND IPOPT_LIBRARIES)
  SET(IPOPT_FOUND TRUE)
  MESSAGE(STATUS "IPOPT found")
  MESSAGE(STATUS "IPOPT Include dirs: " ${IPOPT_INCLUDE_DIRS})
  MESSAGE(STATUS "IPOPT Libraries: " ${IPOPT_LIBRARIES})
ELSE (IPOPT_INCLUDE_DIRS AND IPOPT_LIBRARIES)
  MESSAGE(STATUS "IPOPT was not found")
ENDIF(IPOPT_INCLUDE_DIRS AND IPOPT_LIBRARIES)