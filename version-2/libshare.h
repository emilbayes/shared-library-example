#include <stdint.h>

#define EXPORT __attribute__((visibility("default")))

#ifdef __cplusplus
extern "C" {
#endif

EXPORT int init(void);

EXPORT int version(void);

EXPORT int newmethod(void);

#ifdef __cplusplus
}
#endif
