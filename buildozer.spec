[app]

title = Daily Diary
package.name = dailydiary
package.domain = org.daily

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf,otf

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 35
android.minapi = 24
android.ndk = 28c
android.ndk_api = 24
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.copy_libs = 1
android.debug_artifact = apk

[buildozer]

log_level = 2
warn_on_root = 0
