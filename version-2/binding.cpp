#include <nan.h>
#include "libshare.h"

#define LOCAL_STRING(str) Nan::New<v8::String>(str).ToLocalChecked()
#define LOCAL_FUNCTION(fn) Nan::GetFunction(Nan::New<v8::FunctionTemplate>(fn)).ToLocalChecked()
#define EXPORT_FUNCTION(name) Nan::Set(target, LOCAL_STRING(#name), LOCAL_FUNCTION(name));

NAN_METHOD(version) {
  info.GetReturnValue().Set(Nan::New(version()));
}

NAN_METHOD(newmethod) {
  info.GetReturnValue().Set(Nan::New(newmethod()));
}

NAN_MODULE_INIT(InitAll) {
  int ret = init();
  printf("Init version 2: %d\n", ret);

  EXPORT_FUNCTION(version)
  EXPORT_FUNCTION(newmethod)
}

NODE_MODULE(libshare, InitAll)
