all: version1 version2 dependent

version1:
	cd version-1 && clang -dynamiclib \
        libshare.c \
        -current_version 1.0 \
        -compatibility_version 1.0 \
        -fvisibility=hidden \
        -o libshare.1.0.dylib
	install_name_tool -id @loader_path/libshare.1.0.dylib version-1/libshare.1.0.dylib
	cd version-1 && ../node_modules/.bin/node-gyp rebuild
	cp version-1/libshare.1.0.dylib version-1/build/Release
	node -p 'require("./version-1")'

version2:
	cd version-2 && clang -dynamiclib \
        libshare.c \
        -current_version 1.1 \
        -compatibility_version 1.0 \
        -fvisibility=hidden \
        -o libshare.1.1.dylib
	install_name_tool -id @loader_path/libshare.1.1.dylib version-2/libshare.1.1.dylib
	cd version-2 && ../node_modules/.bin/node-gyp rebuild
	cp version-2/libshare.1.1.dylib version-2/build/Release
	node -p 'require("./version-2")'

dependent:
	cd dependent && ../node_modules/.bin/node-gyp rebuild

clean:
	rm -rf dependent/build version-1/libshare.1.0.dylib version-1/build version-2/libshare.1.1.dylib version-2/build
