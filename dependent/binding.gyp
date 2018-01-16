{
    'variables': {
        'target_arch%': '<!(node -p "os.arch()")>'
    },
    'targets': [{
        'target_name': 'libdep',
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
                        '-L<!(pwd)/../version-2',
                        '-lshare.1.1', # Linux is lazy by default
                    ]
                }
            }],
            ['OS == "mac"', {
                'link_settings': {
                    'libraries': [
                        '-L<!(pwd)/../version-2',
                        '-lazy-lshare.1.1',
                    ]
                }
            }]
        ],
    }]
}
