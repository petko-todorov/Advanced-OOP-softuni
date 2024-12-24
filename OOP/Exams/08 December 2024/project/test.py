from project.auction_house_manager_app import AuctionHouseManagerApp

manager = AuctionHouseManagerApp()
# Register artifacts
print(manager.register_artifact("RenaissanceArtifact", "Kohinoor", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Zelda", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Mona Lisa", 10000.0, 100))
print(manager.register_artifact("ContemporaryArtifact", "The Scream", 2000.0, 1000))
print(manager.register_artifact("ContemporaryArtifact", "Untitled", 32000.0, 90))
print()
# Register collectors
print(manager.register_collector("PrivateCollector", "Josh Smith"))
print(manager.register_collector("Museum", "Louvre"))
print(manager.register_collector("Museum", "Hermitage"))
print()
# Perform purchases
print(manager.perform_purchase("Josh Smith", "Mona Lisa"))
print(manager.perform_purchase("Louvre", "Kohinoor"))
print(manager.perform_purchase("Josh Smith", "Zelda"))
print(manager.perform_purchase("Josh Smith", "The Scream"))
print(manager.perform_purchase("Josh Smith", "Untitled"))
print()
# Remove artifact
print(manager.remove_artifact("The Scream"))
print(manager.remove_artifact("Nonexistent"))
print()
# Start fund-raising campaigns
print(manager.fundraising_campaigns(10000.0))
print()
# Get auction report
print(manager.get_auction_report())
print()

# Remove artifact
print(manager.remove_artifact("Untitled"))
