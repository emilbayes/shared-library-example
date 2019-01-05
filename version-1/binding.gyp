{
    'variables': {
        'target_arch%': '<!(node -p "os.arch()")>',
        'lib_major': '1',
        'lib_minor': '0'
    },
    'targets': [
        {
            'target_name': 'libshare',
            'product_prefix': 'lib',
            'type': 'shared_library',
            'sources': ['libshare.c'],
            'xcode_settings': {
                'LD_DYLIB_INSTALL_NAME': '@rpath/libshare.<(lib_major).<(lib_minor).dylib',
                'DYLIB_COMPATIBILITY_VERSION': '1.0',
                'DYLIB_CURRENT_VERSION': '<(lib_major).<(lib_minor)',
                'OTHER_CFLAGS': [
                    '-fvisibility=hidden'
                ]
            },
            'conditions': [
                ['OS=="mac"', {'product_extension': '<(lib_major).dylib'}],
                ['OS=="linux"', {
                    'product_extension': 'so.<(lib_major).<(lib_minor)',
                    'link_settings': {
                    'ldflags': [
                      # Make binary search for libraries under current directory, so we
                      # don't have to manually set $LD_LIBRARY_PATH:
                      # http://serverfault.com/questions/279068/cant-find-so-in-the-same-directory-as-the-executable
                      '-soname=,
                      # Make native module dynamic loading work.
                    '-rdynamic',
                    ],
                }]
            ]
        },
        {
            'target_name': 'native-share',
            'dependencies': ['libshare'],
            'include_dirs': [
              '<!(node -e "require(\'nan\')")'
            ],
            'sources': [
                'binding.cpp'
            ],
            'xcode_settings': {
                'LD_RUNPATH_SEARCH_PATHS': [
                  '@loader_path',
                ],
            },
        }
    ]
}
