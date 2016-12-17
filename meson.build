project('ffmpeg', 'c', 'cpp',
  version : '3.2.2',
  meson_version : '>= 0.36.0',
  default_options : [ 'warning_level=1',
                      'buildtype=debugoptimized' ])

python = find_program('python3')

configure_args = [
    '--enable-static', '--enable-pic',
    '--disable-avdevice', '--disable-postproc',
    '--disable-programs', '--disable-ffserver', '--disable-ffplay', '--disable-ffprobe', '--disable-ffmpeg',
    '--disable-encoder=flac', '--disable-protocols', '--disable-devices',
    '--disable-network', '--disable-hwaccels', '--disable-dxva2', '--disable-vdpau',
    '--disable-filters', '--enable-filter=yadif', '--disable-doc', '--disable-vda', '--disable-d3d11va', '--disable-dxva2',
    '--disable-audiotoolbox', '--disable-videotoolbox', '--disable-vaapi', '--disable-crystalhd',
    '--disable-mediacodec', '--disable-nvenc', '--disable-mmal', '--disable-omx',
    '--disable-omx-rpi', '--disable-cuda', '--disable-cuvid', '--disable-libmfx',
    '--disable-libnpp', '--disable-iconv', '--disable-jni', '--enable-optimizations']

cc = meson.get_compiler('c')
if cc.get_id() == 'msvc'
    configure_args += ['--toolchain=msvc']
endif

configure = find_program('configure')
message('Configuring ffmpeg, with options: @0@'.format(' '.join(configure_args)))
cres = run_command(configure, configure_args)
if cres.returncode() != 0
    error('Could not configure ffmpeg:\n@0@'.format(cres.stdout()))
endif

build = find_program('build.py')
libav = custom_target('ffmpeg',
  output : ['libavformat.a', 'libavcodec.a',
            'libavfilter.a', 'libswresample.a',
            'libavutil.a'],
  command : [build, meson.current_source_dir(), '@OUTPUT0@', '@OUTPUT1@', '@OUTPUT2@', '@OUTPUT3@', '@OUTPUT4@'])

compile_args = ['-I' + meson.current_build_dir()]
lzma_dep = cc.find_library('lzma')
bz2_dep = cc.find_library('bz2')
m_dep = cc.find_library('m')
z_dep = cc.find_library('z')
libav_deps = [bz2_dep, lzma_dep, m_dep, z_dep]
link_args = ['-Wl,-Bsymbolic']

libavfilter_dep = declare_dependency(compile_args: compile_args,
    link_args: link_args + [join_paths(meson.current_source_dir(), 'libavfilter/libavfilter.a')],
    version: '6.47.100', sources: libav,
    dependencies: libav_deps,
)

libavformat_dep = declare_dependency(compile_args: compile_args,
    link_args: link_args + [join_paths(meson.current_source_dir(), 'libavformat/libavformat.a')],
    version: '57.41.100', sources: libav,
    dependencies: libav_deps,
)

libavcodec_dep = declare_dependency(compile_args: compile_args,
    link_args: link_args + [join_paths(meson.current_source_dir(), 'libavcodec/libavcodec.a')],
    version: '57.48.101', sources: libav,
    dependencies: libav_deps,
)

libavutil_dep = declare_dependency(compile_args: compile_args,
    link_args: link_args + [join_paths(meson.current_source_dir(), 'libavutil/libavutil.a')],
    version: '55.28.100', sources: libav,
    dependencies: libav_deps,
)
