{
    'variables': {
        'target_arch%': '<!(node -p "os.arch()")>'
    },
    'targets': [{
        'target_name': 'libshare',
        'include_dirs': [
          '<!(node -e "require(\'nan\')")'
        ],
        'sources': [
            'binding.cpp'
        ],
        'xcode_settings': {
            'OTHER_CFLAGS': ['-g', '-O3']
        },
        'cflags': ['-g', '-O3'],
        'conditions': [
            ['OS == "win"', {
                'link_settings': {
                    'libraries': [
                        'libshare.lib',
                    ]
                }
            }],
            ['OS == "linux"', {
                'link_settings': {
                    'libraries': [
                        '-lshare',
                    ]
                }
            }],
            ['OS == "mac"', {
                'link_settings': {
                    'libraries': [
                        '<!(pwd)/libshare.1.1.dylib',
                    ]
                }
            }]
        ],
    }]
}
