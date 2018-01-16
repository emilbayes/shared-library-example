#include <stdint.h>

#define EXPORT __attribute__((visibility("default")))

#ifdef __cplusplus
extern "C" {
#endif

EXPORT int init(void);

EXPORT int version(void);

#ifdef __cplusplus
}
#endif
