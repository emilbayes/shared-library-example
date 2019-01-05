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
            'OTHER_LDFLAGS': [
                '-L../version-2/build/Release',
                '-lazy-lshare',
            ],
        }
    }]
}
