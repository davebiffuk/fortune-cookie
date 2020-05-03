# fortune-cookie
A simple fortune cookie app using Kivy.

## Android build and install
```
p4a apk --private $HOME/fortune_cookie   --package=uk.org.biff.fortuneapp   --window   --name "Fortune cookie"   --version 0.1 --bootstrap=sdl2 --requirements=python2,kivy

adb install unnamed_dist_1__armeabi-v7a-debug-0.1-.apk 
```
