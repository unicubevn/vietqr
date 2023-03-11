from vietqrlib import VietQR
# --------------------------

vietQRString = VietQR.genQRString(merchant_id="660704060000129",
                                  acq=VietQR.getBincode('VIB'),
                                  amount="50000",
                                  service_code="QRIBFTTA",
                                  ipn_url="abc"
                                  )
print(f"{vietQRString}")
