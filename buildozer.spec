[app]
title = Estadisticas de futbol con IA
package.name = aifootball
package.domain = org.geonal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,plyer,urllib3,certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, VIBRATE, RECEIVE_BOOT_COMPLETED, POST_NOTIFICATIONS
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
