
import src.LeagueTierList as LeagueTierList


def test_main():

    test = LeagueTierList.LeagueTierList(opgg=True, mobalytics=True, ugg=True)
    # print(f"URLS: {test.urls}\n")

    test_ugg(test)
    test_opgg(test)
    test_mobalytics(test)

    # test.print_tier_lists()
    test.build_tier_list("top")
    test.build_tier_list("jungle")
    test.build_tier_list("mid")
    test.build_tier_list("bot")
    test.build_tier_list("support")

    test.print_tier_list()
    test.create_s_tier_table()

    # test.create_table('mid')

    test.commit_champs()


def test_opgg(test, flag=True):

    # TODO: Update each webscraper to initialize their dictionaries to avoid KeyErrors
    print("TESTING OP.GG")
    test.opgg.build_opgg("top", flag)
    test.opgg.build_opgg("jungle", flag)
    test.opgg.build_opgg("mid", flag)
    test.opgg.build_opgg("adc", flag)
    test.opgg.build_opgg("support", flag)

    return


def test_ugg(test, flag=True):

    print("TESTING U.GG")
    test.ugg.build_ugg("top", flag)
    test.ugg.build_ugg("jungle", flag)
    test.ugg.build_ugg("mid", flag)
    test.ugg.build_ugg("adc", flag)
    test.ugg.build_ugg("support", flag)
    test.ugg.browser.close()

    return


def test_mobalytics(test, flag=True):

    print("TESTING MOBALYTICS")
    test.mobalytics.build_mobalytics("top", flag)
    test.mobalytics.build_mobalytics("jungle", flag)
    test.mobalytics.build_mobalytics("mid", flag)
    test.mobalytics.build_mobalytics("bot", flag)
    test.mobalytics.build_mobalytics("support", flag)

    return


test_main()
