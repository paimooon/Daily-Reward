import genshinstats as gs
import os
gs.set_cookie(ltuid = int(os.environ.get('LTUID')), ltoken = os.environ.get('LTOKEN'))

info = gs.get_daily_reward_info()
print('total rewards claimed:',info['total_sign_day'])
print("Get Reward :", gs.sign_in()) # signed you in, returns a bool whether it succeeded
info = gs.get_daily_reward_info()
print('total rewards claimed:',info['total_sign_day']) # check-in completed if increased
