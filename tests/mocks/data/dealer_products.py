
from hd_google_hackathon.domain.product import DealerProduct

dealer_products = [
    # The Shade Store sells Duette as "The Shade Store Cellular Shades"
    DealerProduct(
        id="ss_duette",
        product_id="duette",
        dealer_id="dealer_1",
        brand_name="The Shade Store Cellular Shades",
        dealer_sku="SS-CELL-001"
    ),
    # Blinds To Go sells Duette as "BTG Honeycomb Architella"
    DealerProduct(
        id="btg_duette",
        product_id="duette",
        dealer_id="dealer_2",
        brand_name="BTG Honeycomb Architella",
        dealer_sku="BTG-HC-A-10"
    ),
    # The Shade Store sells Silhouette as "The Shade Store Sheer Shadings"
    DealerProduct(
        id="ss_silhouette",
        product_id="silhouette",
        dealer_id="dealer_1",
        brand_name="The Shade Store Sheer Shadings",
        dealer_sku="SS-SHEER-001"
    ),
]
