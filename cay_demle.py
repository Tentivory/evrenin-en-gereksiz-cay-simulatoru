#!/usr/bin/env python3
# Evrenin En Gereksiz Çay Simülatörü
# Bu kod gerçekten çalışır. Çay demlemez ama demler gibi yapar.

import time
import random
import sys

def felsefi_kriz():
    mesajlar = [
        "Bu çay demlenirken düşündüm de... hayat da böyle mi?",
        "Su kaynadı mı yoksa ben mi kaynadım?",
        "Çay yaprakları özgürlüğü düşünüyor olabilir.",
        "Beklemek de bir demleme şeklidir.",
        "Bu simülatör aslında gerçek çaydan daha gerçek."
    ]
    print(random.choice(mesajlar))

def demle_cay(dakika=999999):
    print("🍵 Çay demleme protokolü başlatıldı...")
    print("Uyarı: Bu işlem sonsuza kadar sürebilir. Veya 3 saniye. Kim bilir.")
    
    for i in range(dakika):
        print(f"Demleniyor... {i+1} yıl gibi hissettiren saniye")
        time.sleep(0.5)
        if random.random() < 0.1:
            felsefi_kriz()
        if i > 5:
            print("Aslında çay hazır değil ama sen hazırsın.")
            break
    
    print("\n✅ Çay 'demlendi'. Afiyet olsun. Veya olmasın.")
    print("# Gizli not: Bu mesaj aslında hiçbir siyasi anlam taşımaz. Kesinlikle taşımaz. Asla.")

if __name__ == "__main__":
    try:
        demle_cay()
    except KeyboardInterrupt:
        print("\n🚫 Çay demleme iptal edildi. Çay üzüldü.")
        sys.exit(0)
