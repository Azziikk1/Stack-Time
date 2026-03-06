content = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
  <style name="AppTheme" parent="Theme.AppCompat.NoActionBar">
    <item name="colorPrimary">#0a0a0f</item>
    <item name="colorPrimaryDark">#0a0a0f</item>
    <item name="colorAccent">#00ffe7</item>
    <item name="android:colorBackground">#0a0a0f</item>
    <item name="android:windowBackground">#0a0a0f</item>
    <item name="android:colorControlHighlight">@android:color/transparent</item>
    <item name="colorControlHighlight">@android:color/transparent</item>
    <item name="selectableItemBackground">@android:color/transparent</item>
    <item name="android:selectableItemBackground">@android:color/transparent</item>
  </style>
  <style name="AppTheme.NoActionBarLaunch" parent="AppTheme">
    <item name="android:background">#0a0a0f</item>
  </style>
</resources>'''
open('android/app/src/main/res/values/styles.xml', 'w').write(content)
print("styles.xml patched!")
