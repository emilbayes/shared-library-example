#include "libshare.h"

#ifdef __cplusplus
extern "C" {
#endif

static volatile int initialized;

int init(void) {
  if (initialized != 0) {
    return 1;
  }

  initialized = 1;

  return 0;
}

int version(void) {
  return 1;
}

#ifdef __cplusplus
}
#endif
