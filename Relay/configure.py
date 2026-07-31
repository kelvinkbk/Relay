'''
This file is part of Telegram Desktop,
the official desktop application for the Telegram messaging service.

For license and copyright information please follow this link:
https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL
'''
import sys, os, re, subprocess, shutil

sys.dont_write_bytecode = True
scriptPath = os.path.dirname(os.path.abspath(__file__))

candidate_cmake_paths = [
    os.path.abspath(os.path.join(scriptPath, '..', 'cmake')),
    os.path.abspath(os.path.join(scriptPath, 'cmake')),
    os.path.abspath(os.path.join(os.getcwd(), 'cmake')),
    os.path.abspath(os.path.join(os.getcwd(), '..', 'cmake')),
]
found_cmake = False
for p in candidate_cmake_paths:
    if os.path.isfile(os.path.join(p, 'run_cmake.py')):
        sys.path.insert(0, p)
        found_cmake = True
        break

if not found_cmake:
    fallback_cmake_dir = os.path.abspath(os.path.join(scriptPath, '..', 'cmake'))
    print(f"[INFO] run_cmake.py not found. Setting up cmake_helpers in {fallback_cmake_dir}...")
    if os.path.exists(fallback_cmake_dir):
        subprocess.run(['git', 'submodule', 'update', '--init', '--recursive', '--force', 'cmake'], check=False)
        if not os.path.isfile(os.path.join(fallback_cmake_dir, 'run_cmake.py')):
            shutil.rmtree(fallback_cmake_dir, ignore_errors=True)
            subprocess.run(['git', 'clone', 'https://github.com/desktop-app/cmake_helpers.git', fallback_cmake_dir], check=False)
    else:
        subprocess.run(['git', 'clone', 'https://github.com/desktop-app/cmake_helpers.git', fallback_cmake_dir], check=False)
    sys.path.insert(0, fallback_cmake_dir)

import run_cmake

import pathlib
for cmake_base in [os.path.abspath(os.path.join(scriptPath, '..', 'cmake')), os.path.abspath(os.path.join(scriptPath, 'cmake'))]:
    qt_plugins_cmake = pathlib.Path(cmake_base) / 'external' / 'qt' / 'qt_static_plugins' / 'CMakeLists.txt'
    if qt_plugins_cmake.is_file():
        try:
            ptxt = qt_plugins_cmake.read_text(encoding='utf-8')
            target_str = 'add_checked_subdirectory(kimageformats)\ntarget_link_libraries(external_qt_static_plugins\nPUBLIC\n    desktop-app::external_qt_static_plugins_kimageformats\n)'
            if target_str in ptxt and 'if (NOT WIN32)' not in ptxt:
                ptxt = ptxt.replace(
                    target_str,
                    'if (NOT WIN32)\nadd_checked_subdirectory(kimageformats)\ntarget_link_libraries(external_qt_static_plugins\nPUBLIC\n    desktop-app::external_qt_static_plugins_kimageformats\n)\nendif()'
                )
                qt_plugins_cmake.write_text(ptxt, encoding='utf-8')
                print(f"[INFO] Patched {qt_plugins_cmake} to skip kimageformats on Windows")
        except Exception as pe:
            print(f"[WARN] Failed patching qt_static_plugins: {pe}")

    ffmpeg_cmake = pathlib.Path(cmake_base) / 'external' / 'ffmpeg' / 'CMakeLists.txt'
    if ffmpeg_cmake.is_file():
        try:
            ftxt = ffmpeg_cmake.read_text(encoding='utf-8')
            if 'dav1d_candidates' not in ftxt:
                dav1d_block = '''file(GLOB dav1d_candidates
    "${libs_loc}/local/lib/dav1d.lib"
    "${libs_loc}/local/lib/libdav1d.a"
    "${libs_loc}/dav1d/builddir-debug/src/dav1d.lib"
    "${libs_loc}/dav1d/builddir-debug/src/libdav1d.a"
    "${libs_loc}/dav1d/builddir-release/src/dav1d.lib"
    "${libs_loc}/dav1d/builddir-release/src/libdav1d.a"
    "${libs_loc}/dav1d/libdav1d.a"
    "${libs_loc}/ffmpeg/libdav1d.a"
    "${libs_loc}/libdav1d.a"
    "${libs_loc}/dav1d.lib"
)
foreach(dav1d_lib ${dav1d_candidates})
    if (EXISTS "${dav1d_lib}")
        target_link_libraries(external_ffmpeg INTERFACE "${dav1d_lib}")
        break()
    endif()
endforeach()
'''
                ftxt += '\n' + dav1d_block + '\n'
                ffmpeg_cmake.write_text(ftxt, encoding='utf-8')
                print(f"[INFO] Patched {ffmpeg_cmake} to link dav1d static library")
        except Exception as fe:
            print(f"[WARN] Failed patching ffmpeg CMakeLists: {fe}")

candidate_build_paths = [
    os.path.abspath(os.path.join(scriptPath, 'build')),
    os.path.abspath(os.path.join(scriptPath, '..', 'build')),
    os.path.abspath(os.path.join(os.getcwd(), 'build')),
    os.path.abspath(os.path.join(os.getcwd(), 'Relay', 'build')),
]
for p in candidate_build_paths:
    if os.path.isfile(os.path.join(p, 'qt_version.py')):
        sys.path.insert(0, p)
        break
import qt_version

executePath = os.getcwd()
def finish(code):
    global executePath
    os.chdir(executePath)
    sys.exit(code)

def error(message):
    print('[ERROR] ' + message)
    finish(1)

if sys.platform == 'win32' and 'COMSPEC' not in os.environ:
    error('COMSPEC environment variable is not set.')

scriptName = os.path.basename(scriptPath)

arguments = sys.argv[1:]

officialTarget = ''
officialTargetFile = scriptPath + '/build/target'
if os.path.isfile(officialTargetFile):
    with open(officialTargetFile, 'r') as f:
        for line in f:
            officialTarget = line.strip()

arch = ''
if officialTarget in ['win', 'uwp']:
    arch = 'x86'
elif officialTarget in ['win64', 'uwp64']:
    arch = 'x64'
elif officialTarget in ['winarm', 'uwparm']:
    arch = 'arm'
if not qt_version.resolve(arch):
    error('Unsupported platform.')

if 'qt6' in arguments:
    arguments.remove('qt6')

if officialTarget != '':
    officialApiIdFile = scriptPath + '/../../DesktopPrivate/custom_api_id.h'
    if not os.path.isfile(officialApiIdFile):
        error('DesktopPrivate/custom_api_id.h not found.')
    with open(officialApiIdFile, 'r') as f:
        for line in f:
            apiIdMatch = re.search(r'ApiId\s+=\s+(\d+)', line)
            apiHashMatch = re.search(r'ApiHash\s+=\s+"([a-fA-F\d]+)"', line)
            if apiIdMatch:
                arguments.append('-DTDESKTOP_API_ID=' + apiIdMatch.group(1))
            elif apiHashMatch:
                arguments.append('-DTDESKTOP_API_HASH=' + apiHashMatch.group(1))
    if arch != '':
        arguments.append(arch)

finish(run_cmake.run(scriptName, arguments))
