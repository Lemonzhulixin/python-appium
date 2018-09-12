from Base.BaseAndroidPhone import getPhoneInfo
from Base.BaseIosPhone import get_ios_PhoneInfo
from Base.BaseStatistics import countSum, countInfo, countSumDevices

def statistics_result(**kwargs):
    countSum(kwargs["result"])

    print('Platform:', kwargs["platformName"])
    if kwargs["platformName"] == 'android':
        print('Device:', kwargs["devices"])
        get_phone = getPhoneInfo(kwargs["devices"])
        phone_name = get_phone["brand"] + "_" + get_phone["model"] + "_" + "android" + "_" + get_phone["release"]

        countInfo(result=kwargs["result"], testInfo=kwargs["testInfo"], caseName=kwargs["caseName"],
                  phoneName=phone_name,
                  driver=kwargs["driver"], logTest=kwargs["logTest"], devices=kwargs["devices"],
                  testCase=kwargs["testCase"],
                  testCheck=kwargs["testCheck"])
        countSumDevices(kwargs["devices"], kwargs["result"], phone_name=phone_name)
    elif kwargs["platformName"] == 'iOS':
        print('Device:', kwargs["devices"])
        get_phone = get_ios_PhoneInfo(kwargs["devices"])
        phone_name = get_phone["device"] + "_" + get_phone["release"] + "_" + "iOS" + "_" + get_phone["duid"]

        countInfo(result=kwargs["result"], testInfo=kwargs["testInfo"], caseName=kwargs["caseName"],
                  phoneName=phone_name,
                  driver=kwargs["driver"], logTest=kwargs["logTest"], devices=kwargs["devices"],
                  testCase=kwargs["testCase"],
                  testCheck=kwargs["testCheck"])
        countSumDevices(kwargs["devices"], kwargs["result"], phone_name=phone_name)

