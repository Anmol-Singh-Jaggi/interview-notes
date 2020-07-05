from model.AuctionSystem import AuctionSystem


def test1():
    auction_system: AuctionSystem = AuctionSystem()
    auction_system.add_buyer("buyer1")
    auction_system.add_buyer("buyer2")
    auction_system.add_buyer("buyer3")
    auction_system.add_seller("seller1")
    auction_system.create_auction("a1", 10, 50, 1, "seller1")
    auction_system.create_bid("buyer1", "a1", 17)
    auction_system.create_bid("buyer2", "a1", 15)
    auction_system.create_bid("buyer2", "a1", 19)
    auction_system.create_bid("buyer3", "a1", 19)
    auction_system.close_auction("a1")
    profit = auction_system.get_profit("seller1")
    print(profit)


def test2():
    auction_system: AuctionSystem = AuctionSystem()
    auction_system.add_buyer("buyer2")
    auction_system.add_buyer("buyer3")
    auction_system.add_seller("seller2")
    auction_system.create_auction("a2", 5, 20, 2, "seller2")
    auction_system.create_bid("buyer3", "a2", 25)
    auction_system.create_bid("buyer2", "a2", 5)
    auction_system.withdraw_bid("buyer2", "a2")
    auction_system.close_auction("a2")
    profit = auction_system.get_profit("seller2")
    print(profit)


def main():
    test1()


if __name__ == "__main__":
    main()
