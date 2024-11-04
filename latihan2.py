modal_awal = 100_000_000  

laba_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]

modal = modal_awal
for i, persentase_laba in enumerate(laba_bulan):
    laba_bulan_ini = modal * persentase_laba
    modal += laba_bulan_ini
    print(f"laba bulan ke{i+1}: sebesar {persentase_laba*100}% -> Total modal: Rp{modal:,.0f}")

print(f"\nTotal modal pada akhir bulan ke-8: Rp{modal:,.0f}")
