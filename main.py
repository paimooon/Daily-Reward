import genshinstats as gs
import os
gs.set_cookie(ltuid = int(os.environ.get('LTUID')), ltoken = os.environ.get('LTOKEN'))

info = gs.get_daily_reward_info()
print('total rewards claimed:',info[1])
print("Get Reward :", gs.claim_daily_reward()) # signed you in, returns a bool whether it succeeded
info = gs.get_daily_reward_info()
print('total rewards claimed:',info[1]) # check-in completed if increased
