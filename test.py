import pyupbit

access = "pDK7Fa4JgNx8E2x0xNHYAixp7XNAnrpBKOV5eU1X"          # 본인 값으로 변경
secret = "STI1rKcTUrymVnPxGCp4skq1THI6aLcMTvvey8xh"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW"))      # 보유 현금 조회
print(upbit.get_balance("KRW-BTC"))  # KRW-BTC 조회   