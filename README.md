Notes:

* Shared libraries on Windows are identified by their filenames and collisions
  will cause the following error:  
  `Error: The specified procedure could not be found.`  
  To rename a `.dll` file, you need to unpack all exported symbols and generate
  a `.def` file, which then can be modified and compiled back into a `.lib`.
  See [How do I rename a DLL but still allow the EXE to find it?](https://stackoverflow.com/questions/280485/how-do-i-rename-a-dll-but-still-allow-the-exe-to-find-it) and [How To Create 32-bit Import Libraries Without .OBJs or Source](https://support.microsoft.com/da-dk/help/131313/how-to-create-32-bit-import-libraries-without--objs-or-source)
* Lazy loading / Delay-load / Lazy binding
