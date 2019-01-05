{
    'variables': {
        'target_arch%': '<!(node -p "os.arch()")>'
    },
    'targets': [
        {
            'target_name': 'libshare',
            'product_prefix': 'lib',
            'type': 'shared_library',
            'sources': ['libshare.c'],
            'xcode_settings': {
                'LD_DYLIB_INSTALL_NAME': '@rpath/libshare.2.dylib',
                'DYLIB_COMPATIBILITY_VERSION': '2.0',
                'DYLIB_CURRENT_VERSION': '2.0',
                'OTHER_CFLAGS': [
                    '-fvisibility=hidden'
                ]
            }
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
