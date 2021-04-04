import genshinstats as gs
import os
gs.set_cookie(account_id = int(os.environ.get('ACCOUNT_ID')), cookie_token = os.environ.get('COOKIE_TOKEN'))

info = gs.get_daily_reward_info()
print('total rewards claimed:',info['total_sign_day'])
print(gs.sign_in()) # signed you in, returns a bool whether it succeeded
print('total rewards claimed:',info['total_sign_day']) # check-in completed if increased
