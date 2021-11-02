
import src.LeagueTierList as LeagueTierList


def test_main():

    test = LeagueTierList.LeagueTierList(opgg=True, mobalytics=False, ugg=True)
    # print(f"URLS: {test.urls}\n")

    test_ugg(test)

    test.build_tier_list("top")
    test.build_tier_list("jungle")
    test.build_tier_list("mid")
    test.build_tier_list("bot")
    test.build_tier_list("support")

    test.print_tier_list()


def test_ugg(test, flag=True):

    print("TESTING U.GG")
    test.ugg.build_ugg("top", flag)
    test.ugg.build_ugg("jungle", flag)
    test.ugg.build_ugg("mid", flag)
    test.ugg.build_ugg("adc", flag)
    test.ugg.build_ugg("support", flag)
    test.ugg.browser.close()

    return


test_main()
