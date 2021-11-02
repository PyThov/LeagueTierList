
import src.LeagueTierList as LeagueTierList


def test_main():

    test = LeagueTierList.LeagueTierList(opgg=True, mobalytics=False, ugg=False)

    test_opgg(test)

    # test.build_tier_list("top")
    # test.build_tier_list("jungle")
    # test.build_tier_list("mid")
    # test.build_tier_list("bot")
    # test.build_tier_list("support")

    test.print_tier_list()
    # test.create_s_tier_table()


def test_opgg(test, flag=True):

    # TODO: Update each webscraper to initialize their dictionaries to avoid KeyErrors
    print("TESTING OP.GG")
    test.opgg.find_patch()
    # test.opgg.build_opgg("top", flag)
    # test.opgg.build_opgg("jungle", flag)
    # test.opgg.build_opgg("mid", flag)
    # test.opgg.build_opgg("adc", flag)
    # test.opgg.build_opgg("support", flag)

    return

test_main()
