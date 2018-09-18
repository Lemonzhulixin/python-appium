import zipfile, plistlib, re

def find_plist_path(zip_file):
    name_list = zip_file.namelist()
    pattern = re.compile(r'Payload/[^/]*.app/Info.plist')
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()

def getIpaInfo(ipa_path):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_path = find_plist_path(ipa_file)
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)

    name = plist_root['CFBundleDisplayName']
    bundleID = plist_root['CFBundleIdentifier']
    version = plist_root['CFBundleShortVersionString']
    appKey = plist_root['XiaoYingAppKey']
    miniOSVersion = plist_root['MinimumOSVersion']
    print("=====getIpaInfo=========")
    print('appName: %s' % name)
    print('bundleId: %s' % bundleID)
    print('appVersion: %s' % version)
    print('appKey: %s' % appKey)
    print('miniOSVersion: %s' % miniOSVersion)
    return name, bundleID, version, appKey, miniOSVersion


if __name__ == '__main__':
    pass
    ipa_path = '../app/xiaoying.ipa'
    getIpaInfo(ipa_path)
