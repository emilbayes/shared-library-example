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
  return 2;
}

int newmethod(void) {
  return 3;
}

#ifdef __cplusplus
}
#endif
